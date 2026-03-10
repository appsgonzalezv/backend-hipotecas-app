from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hipotecas")
def obtener_hipotecas():
    # Base de datos actualizada a Marzo 2026
    datos_marzo = [
        {"banco": "Unicaja", "tin": "1,90%", "fecha": "02/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "Caixabank", "tin": "2,00%", "fecha": "07/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "BBVA", "tin": "2,00%", "fecha": "07/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "Unicaja", "tin": "2,10%", "fecha": "02/03/2026", "vinculaciones": "Sin vinculaciones"},
        {"banco": "Kutxabank", "tin": "2,10%", "fecha": "03/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "Santander", "tin": "2,11%", "fecha": "03/03/2026", "vinculaciones": "N"},
        {"banco": "Abanca", "tin": "2,15%", "fecha": "03/03/2026", "vinculaciones": "N+SH"},
        {"banco": "Ibercaja", "tin": "2,25%", "fecha": "02/03/2026", "vinculaciones": "N+SH"},
        {"banco": "Caja Rural Jaén", "tin": "2,35%", "fecha": "07/03/2026", "vinculaciones": "N+SH"},
        {"banco": "Abanca", "tin": "2,50%", "fecha": "05/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "Santander", "tin": "3,20%", "fecha": "04/03/2026", "vinculaciones": "Sin vinculaciones"}
        # Puedes añadir el resto siguiendo este formato
    ]
    
    return {
        "status": "success",
        "tipo": "Fijo",
        "mes": "Marzo 2026",
        "data": datos_marzo
    }
