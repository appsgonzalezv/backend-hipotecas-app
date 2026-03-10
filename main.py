import os
import subprocess
from fastapi import FastAPI
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# Forzamos la ruta absoluta de la carpeta de navegadores
current_dir = os.path.dirname(os.path.abspath(__file__))
browser_folder = os.path.join(current_dir, "pw-browsers")
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = browser_folder

app = FastAPI()

@app.get("/api/hipotecas")
def obtener_hipotecas():
    url = "https://www.economiaresponsablefinanzas.com/hipotecas/las-mejores-ofertas-hipotecarias/"
    
    try:
        with sync_playwright() as p:
            # Lanzamos el navegador asegurándonos de que use la ruta configurada
            navegador = p.chromium.launch(headless=True)
            contexto = navegador.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            pagina = contexto.new_page()
            pagina.goto(url, wait_until="networkidle", timeout=30000)
            html_content = pagina.content()
            navegador.close()

        soup = BeautifulSoup(html_content, 'html.parser')
        ofertas_fijas = []
        tablas = soup.find_all('table')
        if tablas:
            filas = tablas[0].find_all('tr')
            for fila in filas[1:]: 
                columnas = fila.find_all('td')
                if len(columnas) >= 3:
                    banco = columnas[0].text.strip()
                    tin = columnas[1].text.strip()
                    tae = columnas[2].text.strip()
                    ofertas_fijas.append({"banco": banco, "tin": tin, "tae": tae})
                    
        if not ofertas_fijas:
            ofertas_fijas = [
                {"banco": "Banco Santander (Backup)", "tin": "2.60%", "tae": "2.95%"},
                {"banco": "BBVA (Backup)", "tin": "2.75%", "tae": "3.15%"},
                {"banco": "Evo Banco (Backup)", "tin": "2.45%", "tae": "2.85%"}
            ]
        return {"status": "success", "data": ofertas_fijas}

    except Exception as e:
        # Si falla, devolvemos el error exacto para diagnosticar
        return {"status": "error", "message": str(e), "data": []}
