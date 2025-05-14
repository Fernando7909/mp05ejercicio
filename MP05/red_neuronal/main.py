# Importar las librerías necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. Cargar el dataset "Airline Passengers"
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv'
df = pd.read_csv(url, usecols=[1])  # Se utiliza la columna "Passengers"
data = df.values.astype('float32')

# Visualizar los datos originales
plt.figure(figsize=(10, 4))
plt.plot(data, label="Número de pasajeros")
plt.title("Datos de pasajeros aéreos (1949-1960)")
plt.xlabel("Meses")
plt.ylabel("Número de pasajeros")
plt.legend()
plt.show()

# 2. Preprocesamiento: Escalar los datos
scaler = MinMaxScaler(feature_range=(0, 1))
data_scaled = scaler.fit_transform(data)

# 3. Crear el dataset con ventanas de datos (look_back)
def create_dataset(dataset, look_back=12):
    """
    Genera un conjunto de datos en el que cada entrada es una ventana
    de 'look_back' meses y la salida es el valor del mes siguiente.
    """
    X, y = [], []
    for i in range(len(dataset) - look_back):
        X.append(dataset[i:(i + look_back), 0])
        y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(y)

look_back = 12  # Usamos 12 meses (1 año) para capturar la estacionalidad anual
X, y = create_dataset(data_scaled, look_back)

# 4. Dividir en conjuntos de entrenamiento y prueba (80% entrenamiento, 20% prueba)
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# 5. Definir y compilar el modelo MLP (red densa)
model = Sequential()
model.add(Dense(50, input_dim=look_back, activation='relu'))  # Capa oculta con 50 neuronas
model.add(Dense(25, activation='relu'))
model.add(Dense(1))                                           # Capa de salida para predecir un valor
model.compile(optimizer='adam', loss='mean_squared_error')

# 6. Entrenar el modelo
history = model.fit(X_train, y_train, epochs=50, batch_size=16, validation_data=(X_test, y_test), verbose=1)

# 7. Realizar predicciones
y_pred = model.predict(X_test)

# Invertir la escala para visualizar los resultados en sus valores originales
y_test_inv = scaler.inverse_transform(y_test.reshape(-1, 1))
y_pred_inv = scaler.inverse_transform(y_pred)

# 8. Visualizar la predicción vs. el valor real
plt.figure(figsize=(10, 4))
plt.plot(y_test_inv, label="Valor Real")
plt.plot(y_pred_inv, label="Predicción", linestyle='--')
plt.title("Predicción de pasajeros aéreos con una red MLP")
plt.xlabel("Meses (en el conjunto de prueba)")
plt.ylabel("Número de pasajeros")
plt.legend()
plt.show()