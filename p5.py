import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-09-08/friends_info.csv"
df = pd.read_csv(url)

print("2.Primeros registros\n")
print(df.head())    

print("\n\n\n3.Dimensiones\n")
print(f"Filas: {df.shape[0]}")
print(f"Columnas: {df.shape[1]}")
print(f"Forma completa (shape): {df.shape}")

print("\n\n\n3.Nombres de las columnas\n")
print(df.columns.tolist())
print("\nTipos de datos\n")
print(df.dtypes)

print("\n\n\n4.Datos vacios y duplicados\n")
print(df.isnull().sum())
print()
duplicados = df.duplicated().sum()
print(f"Registros duplicados: {duplicados}")

print("\n\n\n5.Episodios de la temporada 3")
temp3 = df[df["season"] == 3]
print(temp3)

print("\n\n\n6.Episodios de mas de 25 millones de espect\n")
print("=" * 70)
mas_vistos = df[df["us_views_millions"] > 25]
print(mas_vistos)

print("\n\n\n7.Promedio de espectadores por temporada\n")
promedio_temp = df.groupby("season")["us_views_millions"].mean()
print(promedio_temp)

print("\n\n\n8.Top 5 episodios con mas audiencia\n")
top5 = df.sort_values("us_views_millions", ascending=False).head(5)
print(top5[["title", "us_views_millions"]])

print("\n\n\n9.Promedio de espectadores\n")
promedio_general = df["us_views_millions"].mean()
print(f"Promedio de espectadores: {promedio_general:.2f} millones")

print("\n\n\n10.Calificacion imdb mas alta\n")
max_imdb = df["imdb_rating"].max()
print(f"La calificacion mas alta es: {max_imdb}")



print("\n\n11.Grafica promedio de espectadores\n")
promedio_temp = df.groupby("season")["us_views_millions"].mean()
plt.figure(figsize=(10, 5))
promedio_temp.plot(kind="bar")
plt.title("Promedio de espectadores por temporada")
plt.xlabel("Temporada")
plt.ylabel("Espectadores")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


print("\n\n12.Grafica de 5 episodios con mayor audiencia\n")
top5 = df.sort_values("us_views_millions", ascending=True).head(5)
plt.figure(figsize=(10, 5))
plt.barh(top5["title"], top5["us_views_millions"])
plt.title("Top 5 episodios con mayor audiencia")
plt.xlabel("Espectadores")
plt.ylabel("Episodio")
plt.tight_layout()
plt.show()

print("\n13.PREGUNTAS\n")
print("Que temporada tuvo el mayor promedio de espectadores?\n")
print("La temporada con un promedio mas alto es la [2]")
print("\n\ncual fue el episodio con mayor audiencia?\n")
print("el episodio 3: The One After the Superbowl")