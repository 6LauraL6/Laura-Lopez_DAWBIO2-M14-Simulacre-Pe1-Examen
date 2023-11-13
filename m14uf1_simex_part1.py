import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from urllib.request import urlretrieve


# Contingut original.
filepath: str = "incidence-rate-2021-raw.csv"

# Et donem el contingut ja preprocessat, a partir de la q3.
filepath_q3: str = "incidence-rate-2021-new.csv"

def q0_read_raw_data():
    df_orig = pd.read_csv(filepath, sep=';', decimal=".")
    print(df_orig.iloc[0])
    return df_orig

def q0_read_correct_data():
    df_orig = pd.read_csv(filepath_q3, sep=';', decimal=".")
    # print(df_orig.iloc[0])
    return df_orig

# Pregunta 1. Mostra la següent info: 
#               El número de files en total 
#               Informació sobre totes les columnes
#               Les 20 primeres files 
def q1_basic_info(df: pd.DataFrame):
    print("Pregunta 1.")
    print(f"Numero total de filas:,{len(df)}")
    print(f"Info columnas:\n{df.info()}")
    print(f"Las 20 primera filas: \n{df.head(20)}")
# Pregunta 2. Preprocessament dataframe.
#               Mostra els valors únics del camp DENOMINATOR
#               Crea un nou dataframe que:
#                 Elimina la columna DISEASE_DESCRIPTION
#                 De la columna 'GROUP' només volem les files 
#                   que tinguin el valor 'COUNTRIES'
#                 De la columna 'DENOMINATOR' Només tingui el valor
#                   'per 1,000,000 total population'.
#                   per tal d'unificar criteris.
#               Guarda-ho en un fitxer anomenat:
#                  incidence-rate-2021-new.csv
def q2_preprocessing(df: pd.DataFrame):
    print("Pregunta 2")
    df_new = df
    df['DENOMINATOR'].unique()# mostra els valors únics del camp DENOMINATOR
    
    #Crea un nou dataframe
    df_new=df[df['GROUP'] == 'COUNTRIES']
    df_new =df_new[df_new['DENOMINATOR'] == 'per 1,000,000 total population' ]
    
    #Elimina la columna DISEASE_DESCRIPTION
    df_new =df_new.drop(columns='DISEASE_DESCRIPTION')
    
    #Guarda-ho en un fitxer 
    df_new.to_csv("incidence-rate-2021-new.csv",sep=';', decimal='.', index=False)
    
    return df_new

# Pregunta 3. Analitzem NaN i outliers.
#               Mostra els valors NaN que hi ha en cada columna.
#               Mostra el nom, enfermetat, inc_rate i any de les 10 files que tenen valors més
#               alts d'INCIDENCE_RATE.
def q3_outliers(df_new: pd.DataFrame):
    # Mostrar los valores NaN por columna
    print("Pregunta 3")
    print(df_new.isnull().sum())
    #Mostra el nom, enfermetat, inc_rate i any de les 10 files
    top_10_incidence = df_new.nlargest(10,'INCIDENCE_RATE')[['NAME', 'DISEASE', 'INCIDENCE_RATE', 'YEAR']]  
    print(top_10_incidence)
    print("TODO")
    return df_new

# Pregunta 4. Gràfic distribució casos enfermetats.
#               Mostra un gràfic plotbox o similar dels casos d'enfermetats d'un país
#               (el que et toqui) agrupats per enfermetats.
def q4_grafic_distribucio(df_new: pd.DataFrame, country_name, filename):
    # Filtrar el DataFrame por el país deseado
    df_country = df_new[df_new['NAME'] == country_name]

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df_country, x='DISEASE', y='INCIDENCE_RATE')
    plt.title(f'Distribución de la tasa de incidencia por enfermedad en {country_name}')
    plt.xlabel('Enfermedad')
    plt.ylabel('Tasa de Incidencia')
    plt.xticks(rotation=45)
    plt.savefig(filename) 
    
    print("TODO")


if __name__ == "__main__":
    df = q0_read_raw_data()
    q1_basic_info(df)
    df_new = q2_preprocessing(df)
    df_new = pd.read_csv(filepath, sep=';', decimal=".")
    q3_outliers(df_new)
    q4_grafic_distribucio(df_new,'Afghanistan', 'grafico_incidencia_afghanistan.png')