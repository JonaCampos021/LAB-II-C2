import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('Balon_oro.csv')

# Mostrar las columnas del DataFrame para identificar las que queremos usar
print(df.columns)


# Ordenar los jugadores por el número de goles en orden descendente
top_goleadores = df.sort_values(by='Performance-Gls', ascending=False).head(5)

# Crear la gráfica de barras
x = top_goleadores.plot.bar(x='player', y=['Performance-Gls', 'Performance-Ast'], rot=45)

# Añadir un título y etiquetas a la gráfica
plt.title('Top 5 jugadores con más goles y asistencias')
plt.xlabel('Jugador')
plt.ylabel('Cantidad')

# Mostrar la gráfica
plt.show()
