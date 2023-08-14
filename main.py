#%%
#!pip install fastapi
#!pip install pydantic
#!pip install uvicorn
# %%
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# %%
class Item(BaseModel):
    fecha : str
    pronostico : Optional[str]
    temperatura_maxima : Optional[int]
    temperatura_minima : Optional[int]
    probabilidad_lluvia : Optional[int]
    viento_dia : Optional[int]
    direccion_viento_dia : Optional[str]
    viento_noche: Optional[int]
    direccion_viento_noche : Optional[str]
    humedad_dia_porcentaje: Optional[int]
    humedad_noche_porcentaje: Optional[int]
    indice_UV_dia : Optional[str]
    indice_UV_noche : Optional[str]	
    amanecer : Optional[str]
    puesta_solar : Optional[str]	
    salida_lunar : Optional[str]
    puesta_lunar : Optional[str]
    fase_lunar : Optional[str]

app = FastAPI()

# %%
@app.post("/agregar_elemento/")
async def agregar_elemento(item: Item):
    conn = sqlite3.connect("Clima.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pronosticos (fecha, pronostico,	temperatura_maxima, temperatura_minima, probabilidad_lluvia, viento_dia, direccion_viento_dia, viento_noche, direccion_viento_noche, humedad_dia_porcentaje, humedad_noche_porcentaje, indice_UV_dia, indice_UV_noche, amanecer, puesta_solar, salida_lunar, puesta_lunar, fase_lunar) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (item.fecha, item.pronostico,item.temperatura_maxima, item.temperatura_minima, item.probabilidad_lluvia, item.viento_dia, item.direccion_viento_dia, item.viento_noche, item.direccion_viento_noche, item.humedad_dia_porcentaje, item.humedad_noche_porcentaje, item.indice_UV_dia, item.indice_UV_noche, item.amanecer, item.puesta_solar, item.salida_lunar, item.puesta_lunar, item.fase_lunar))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos agregados exitosamente."}

# %%
@app.get("/leer_elementos/")
async def leer_elementos():
    conn = sqlite3.connect("Clima.db")
    cursor = conn.cursor()
    cursor.execute("SELECT fecha, pronostico, temperatura_maxima, temperatura_minima, probabilidad_lluvia, viento_dia, direccion_viento_dia, viento_noche, direccion_viento_noche, humedad_dia_porcentaje, humedad_noche_porcentaje, indice_UV_dia, indice_UV_noche, amanecer, puesta_solar, salida_lunar, puesta_lunar, fase_lunar FROM pronosticos")
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return [{"fecha": resultado[0], "pronostico": resultado[1], "temperatura_maxima": resultado[2],"temperatura_minima":resultado[3], "probabilidad_lluvia":resultado[4], "viento_dia":resultado[5], "direccion_viento_dia":resultado[6], "viento_noche":resultado[7], "direccion_viento_noche":resultado[8], "humedad_dia_porcentaje":resultado[9], "humedad_noche_porcentaje":resultado[10], "indice_UV_dia":resultado[11], "indice_UV_noche":resultado[12], "amanecer":resultado[13], "puesta_solar":resultado[14], "salida_lunar":resultado[15], "puesta_lunar":resultado[16], "fase_lunar":resultado[17]} for resultado in resultados]
    else:
        return {"mensaje": "No se encontraron los datos."}

# %%
@app.get("/leer_elemento/{id}/")
async def leer_elemento(id: int):
    conn = sqlite3.connect("Clima.db")
    cursor = conn.cursor()
    cursor.execute("SELECT fecha, pronostico, temperatura_maxima, temperatura_minima, probabilidad_lluvia, viento_dia, direccion_viento_dia, viento_noche, direccion_viento_noche, humedad_dia_porcentaje, humedad_noche_porcentaje, indice_UV_dia, indice_UV_noche, amanecer, puesta_solar, salida_lunar, puesta_lunar, fase_lunar FROM pronosticos WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado is not None:
        return {"fecha": resultado[0], "pronostico": resultado[1], "temperatura_maxima": resultado[2],"temperatura_minima":resultado[3], "probabilidad_lluvia":resultado[4], "viento_dia":resultado[5], "direccion_viento_dia":resultado[6], "viento_noche":resultado[7], "direccion_viento_noche":resultado[8], "humedad_dia_porcentaje":resultado[9], "humedad_noche_porcentaje":resultado[10], "indice_UV_dia":resultado[11], "indice_UV_noche":resultado[12], "amanecer":resultado[13], "puesta_solar":resultado[14], "salida_lunar":resultado[15], "puesta_lunar":resultado[16], "fase_lunar":resultado[17]}
    else:
        return {"mensaje": "No se encontraron los datos solicitados."}

# %%
@app.put("/actualizar_elemento/{id}/")
async def actualizar_elemento(id: int, item: Item):
    conn = sqlite3.connect("Clima.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE pronosticos SET fecha=?, pronostico=?, temperatura_maxima=?, temperatura_minima=?, probabilidad_lluvia=?, viento_dia=?, direccion_viento_dia=?, viento_noche=?, direccion_viento_noche=?, humedad_dia_porcentaje=?, humedad_noche_porcentaje=?, indice_UV_dia=?, indice_UV_noche=?, amanecer=?, puesta_solar=?, salida_lunar=?, puesta_lunar=?, fase_lunar=? WHERE id=?", (item.fecha, item.pronostico,item.temperatura_maxima, item.temperatura_minima, item.probabilidad_lluvia, item.viento_dia, item.direccion_viento_dia, item.viento_noche, item.direccion_viento_noche, item.humedad_dia_porcentaje, item.humedad_noche_porcentaje, item.indice_UV_dia, item.indice_UV_noche, item.amanecer, item.puesta_solar, item.salida_lunar, item.puesta_lunar, item.fase_lunar, id))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos actualizados exitosamente."}

# %%
@app.delete("/eliminar_elemento/{id}/")
async def eliminar_elemento(id: int):
    conn = sqlite3.connect("Clima.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pronosticos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos eliminados exitosamente."}

# %%