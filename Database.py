# %%
import sqlite3
import csv

def create_pronosticos_table():
    conn = sqlite3.connect("Clima.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS pronosticos(
                   id INTEGER PRIMARY KEY,
                   fecha TEXT NOT NULL,
                   pronostico TEXT ,
                   temperatura_maxima INTEGER,
                   temperatura_minima INTEGER,
                   probabilidad_lluvia INTEGER,
                   viento_dia INTEGER,
                   direccion_viento_dia TEXT ,
                   viento_noche INTEGER,
                   direccion_viento_noche TEXT ,	
                   humedad_dia_porcentaje INTEGER,
                   humedad_noche_porcentaje INTEGER,
                   indice_UV_dia TEXT ,	
                   indice_UV_noche TEXT ,	
                   amanecer	TEXT,
                   puesta_solar TEXT,	
                   salida_lunar	TEXT,
                   puesta_lunar	TEXT,
                   fase_lunar TEXT 
                   )
                   """)
    
    conn.commit()
    conn.close()


# %%
def read_csv_file(csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def insert_data_to_pronosticos_table(data):
    conn = sqlite3.connect("Clima.db")
    cursor = conn.cursor()

    for row in data:
        cursor.execute("""
            INSERT INTO pronosticos (fecha, pronostico,	temperatura_maxima, temperatura_minima, probabilidad_lluvia, viento_dia, direccion_viento_dia, viento_noche, direccion_viento_noche, humedad_dia_porcentaje, humedad_noche_porcentaje, indice_UV_dia, indice_UV_noche, amanecer, puesta_solar, salida_lunar, puesta_lunar, fase_lunar)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (row["Fecha"], row["Pronostico"], row["Temperatura maxima"], row["Temperatura minima"], row["Probabilidad de lluvia"], row["Viento en el dia"],row["Direccion viento dia"], row["Viento en la noche"], row["Direccion viento noche"], row["Humedad dia"], row["Humedad noche"], row["Indice UV dia"], row["Indice UV noche"], row["Amanecer"], row["Puesta solar"], row["Salida lunar"], row["Puesta lunar"], row["Fase lunar"]))

    conn.commit()
    conn.close()

# %%
if __name__ == "__main__":
    csv_file = "./data/The-Weather-Channel-WebScrap-13-08-2023.csv"
    data_to_insert = read_csv_file(csv_file)
    insert_data_to_pronosticos_table(data_to_insert)

# %%
if __name__ == "__main__":
    create_pronosticos_table()
# %%