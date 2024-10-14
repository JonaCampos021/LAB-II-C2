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

# Análisis del gráfico:
# 1. Comparación Visual: La gráfica de barras permite comparar fácilmente el número de goles y asistencias de los cinco mejores jugadores.
# 2. Identificación de Estrellas: Los jugadores que destacan en ambos aspectos (goles y asistencias) son indicativos de su rendimiento general y contribución al equipo.
# 3. Tendencias de Juego: Si un jugador tiene muchos más goles que asistencias, puede ser un finalizador nato; si las cifras son más equilibradas, puede ser un creador de juego.
# 4. Valor para el Equipo: Comprender la contribución de cada jugador en términos de goles y asistencias puede ayudar a los clubes a tomar decisiones estratégicas en transferencias y alineaciones.


