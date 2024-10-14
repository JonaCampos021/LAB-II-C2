import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('gym.csv')

# Contar la cantidad de cada tipo de workout
workout_counts = df['Workout_Type'].value_counts()

# Crear el gráfico circular
plt.figure(figsize=(10, 6))
plt.pie(workout_counts, labels=workout_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Tipos de Entrenamiento')
plt.axis('equal')  # Para que el gráfico sea un círculo
plt.show()

# Análisis del gráfico:
# 1. Proporciones Claras: El gráfico circular permite visualizar de manera efectiva las proporciones relativas de cada tipo de entrenamiento.
# 2. Identificación de Tendencias: Un tipo de entrenamiento que ocupa la mayor parte del gráfico podría indicar una tendencia hacia ese estilo específico.
# 3. Diversidad en los Workouts: Si varios tipos tienen porciones significativas, sugiere que los usuarios disfrutan de una variedad de actividades.
# 4. Posibles Áreas de Mejora: Un tipo de workout con representación muy baja podría ser una oportunidad para introducir nuevas clases o promociones.
# 5. Contexto Adicional: Complementar el análisis con información demográfica o de comportamiento de los usuarios podría ofrecer más insights.
