
""" Obtención de datos: Lea el archivo "generos_musicales.csv". El mismo debe contiene 4 columnas: Nombre, Edad (entre 12 y 75), País y 
Género musical (Electrónica, Jazz, Rock, Pop, Cumbia)."""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')


generos_mus = pd.read_csv("generos_musicales.csv")
print("\nEncuesta de géneros musicales\n", generos_mus)

#Cantidad de personas para cada género musical
cantidad_generos = generos_mus["Género musical"].value_counts()
print("\n", cantidad_generos, "\n")

#Cantidad de personas mayores de 35 años que escuchan rock
mayores35_rock = generos_mus[(generos_mus["Género musical"] == "Rock") & (generos_mus['Edad'] > 35)]
print("\n", mayores35_rock, "\n")
print("\nCantidad de personas mayores de 35 años que escuchan rock: ", len(mayores35_rock), "\n")


#País en donde más se escucha el genero Pop
genero_pop = generos_mus[generos_mus['Género musical'].isin(['Pop'])]
print("Países en donde se escucha el género musical POP: \n", genero_pop, "\n")

print("\nPaís en donde más se escucha el género musical POP: \n", genero_pop["País"].mode(), "\n")


#País en donde más se escucha el genero Jazz
genero_jazz = generos_mus[generos_mus['Género musical'].isin(['Jazz'])]
print("Países en donde se escucha el género musical JAZZ: \n", genero_jazz, "\n")

print("\nPaís en donde más se escucha el género musical JAZZ: \n", genero_jazz["País"].mode(), "\n")

#Géneros musicales que escuchan personas entre 25 y 55 años
mayores25_menores55 = generos_mus[(generos_mus['Edad'] > 25) & (generos_mus['Edad'] < 55)]
print("\nGéneros musicales que escuchan personas entre 25 y 55 años: \n", mayores25_menores55, "\n")


#Géneros musicales que escuchan personas menores de 25 y mayores 55 años
menores25_mayores55 = generos_mus[(generos_mus['Edad'] < 25) & (generos_mus['Edad'] > 55)]
print("\nGéneros musicales que escuchan personas menores de 25 y mayores a 55 años: \n", menores25_mayores55, "\n")


colores = ["lemonchiffon", "orange", "bisque", "gold", "mistyrose"]
explode = [0.1, 0.1, 0.1, 0.1, 0.1]

mayores25_menores55["Género musical"].value_counts().plot.pie(autopct="%1.1f%%", colors = colores, explode = explode, shadow = True)

plt.title ("\nAnálisis de género musical según la edad\n", fontsize = 16, fontweight = 'bold')
plt.show()

categorias = mayores25_menores55["Género musical"].unique()
cantidades = []

for categoria in categorias:
  df_aux = mayores25_menores55.groupby("Género musical").get_group(categoria)
  cantidades.append(len(df_aux))

cantidades = np.array(cantidades)
porcentajes = cantidades / cantidades.sum() * 100.0

fig, ax = plt.subplots(figsize=(15,15))
plt.bar(categorias, porcentajes, color = "lightcyan", linewidth = 1.5, edgecolor = "orchid", alpha = 0.70)

for bar in ax.patches:
  ax.text(bar.get_x() + bar.get_width() / 2,
          bar.get_height() / 2 + bar.get_y(),
          round(bar.get_height()), ha = 'center',
          color = 'deeppink', weight = 'bold', size = 11)

plt.title("\nAnálisis de género musical según la edad\n", fontsize = 16, fontweight = 'bold')
plt.xlabel("\nGéneros musicales\n")
plt.ylabel("\nPorcentaje de personas (%)\n")
plt.grid(linestyle='-', linewidth=0.25, alpha=0.3)
plt.show()
