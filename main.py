from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hipotecas")
def obtener_hipotecas():
    # Base de datos completa a marzo de 2026
    datos_reales = [
        {"banco": "Unicaja", "tin": "1,90%", "tae": "N/D", "fecha": "02/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "Caixabank", "tin": "2,00%", "tae": "N/D", "fecha": "07/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "BBVA", "tin": "2,00%", "tae": "N/D", "fecha": "07/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "Unicaja", "tin": "2,10%", "tae": "N/D", "fecha": "02/03/2026", "vinculaciones": "Sin vinculaciones"},
        {"banco": "Kutxabank", "tin": "2,10%", "tae": "N/D", "fecha": "03/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "BBVA", "tin": "2,10%", "tae": "N/D", "fecha": "05/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "Caixabank", "tin": "2,10%", "tae": "N/D", "fecha": "06/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "Santander", "tin": "2,11%", "tae": "N/D", "fecha": "03/03/2026", "vinculaciones": "N"},
        {"banco": "Abanca", "tin": "2,15%", "tae": "N/D", "fecha": "03/03/2026", "vinculaciones": "N+SH"},
        {"banco": "Santander", "tin": "2,19%", "tae": "N/D", "fecha": "02/03/2026", "vinculaciones": "N+SH+S protección de pagos"},
        {"banco": "Unicaja", "tin": "2,20%", "tae": "N/D", "fecha": "02/03/2026", "vinculaciones": "N+SH"},
        {"banco": "BBVA", "tin": "2,20%", "tae": "N/D", "fecha": "04/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "Caixabank", "tin": "2,20%", "tae": "N/D", "fecha": "05/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "BBVA", "tin": "2,20%", "tae": "N/D", "fecha": "05/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "Ibercaja", "tin": "2,25%", "tae": "N/D", "fecha": "02/03/2026", "vinculaciones": "N+SH"},
        {"banco": "Ibercaja", "tin": "2,30%", "tae": "N/D", "fecha": "05/03/2026", "vinculaciones": "N+SH"},
        {"banco": "Unicaja", "tin": "2,30%", "tae": "N/D", "fecha": "06/03/2026", "vinculaciones": "N+SH"},
        {"banco": "Caixabank", "tin": "2,35%", "tae": "N/D", "fecha": "03/03/2026", "vinculaciones": "N"},
        {"banco": "Caja Rural Jaén", "tin": "2,35%", "tae": "N/D", "fecha": "07/03/2026", "vinculaciones": "N+SH"},
        {"banco": "Caixabank", "tin": "2,45%", "tae": "N/D", "fecha": "03/03/2026", "vinculaciones": "Sin vinculaciones"},
        {"banco": "Abanca", "tin": "2,50%", "tae": "N/D", "fecha": "05/03/2026", "vinculaciones": "N+SH+SV"},
        {"banco": "Unicaja", "tin": "2,90%", "tae": "N/D", "fecha": "04/03/2026", "vinculaciones": "Sin vinculaciones"},
        {"banco": "BBVA", "tin": "2,90%", "tae": "N/D", "fecha": "03/03/2026", "vinculaciones": "Sin vinculaciones"},
        {"banco": "Caixabank", "tin": "3,10%", "tae": "N/D", "fecha": "06/03/2026", "vinculaciones": "Sin vinculaciones"},
        {"banco": "BBVA", "tin": "3,10%", "tae": "N/D", "fecha": "06/03/2026", "vinculaciones": "Sin vinculaciones"},
        {"banco": "Kutxabank", "tin": "3,10%", "tae": "N/D", "fecha": "07/03/2026", "vinculaciones": "Sin vinculaciones"},
        {"banco": "Santander", "tin": "3,20%", "tae": "N/D", "fecha": "04/03/2026", "vinculaciones": "Sin vinculaciones"},
        {"banco": "Ibercaja", "tin": "3,25%", "tae": "N/D", "fecha": "04/03/2026", "vinculaciones": "Sin vinculaciones"},
        {"banco": "Unicaja", "tin": "3,30%", "tae": "N/D", "fecha": "07/03/2026", "vinculaciones": "Sin vinculaciones"},
        {"banco": "Abanca", "tin": "3,50%", "tae": "N/D", "fecha": "06/03/2026", "vinculaciones": "Sin vinculaciones"}
    ]
    
    return {
        "status": "success",
        "tipo": "Fijo",
        "mes": "Marzo 2026",
        "data": datos_reales
    }
