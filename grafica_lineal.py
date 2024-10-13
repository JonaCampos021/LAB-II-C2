import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('games_ranking.csv')

# Mostrar las columnas para verificar
print(df.columns)

# Ordenar los juegos por el valor de 'rank' en orden ascendente (suponiendo que menor rank es mejor)
top_mejores_juegos = df.head(5)

# Crear la gráfica lineal con los nombres de juegos y sus respectivos ranks
plt.plot(top_mejores_juegos['game_name'], top_mejores_juegos['rank'], marker='o', label='Ranking')

# Añadir título y etiquetas
plt.title('Top 5 mejores juegos según ranking')
plt.xlabel('Juego')
plt.ylabel('Ranking')
plt.legend()

# Rotar las etiquetas del eje X para mejor legibilidad
plt.xticks(rotation=45)

# Mostrar la gráfica
plt.show()