# -*- coding: utf-8 -*-
"""euros_a_yuan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F7pv44npgTe2oQz_6rHEhphxWD3v2VFZ
"""

import tensorflow as tf
import numpy as np

euros= np.array([1, 5, 20, 27,34], dtype= float)
yuan = np.array([7.7449, 38.7245, 154.898, 209.1123, 263.3266], dtype= float)

#capa =  tf.keras.layers.Dense(units=1, input_shape=[1])
#modelo = tf.keras.Sequential([capa])
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
  loss='mean_squared_error'
)

print("comenzando entrenamiento...")
hilstorial = modelo.fit(euros, yuan, epochs=1000, verbose=False)
print("Modelo entrenado!!!")

import matplotlib.pyplot as plt
plt.xlabel("euros")
plt.ylabel("yuan")
plt.plot(hilstorial.history["loss"])

print("Realizar una predicción")
resultado = modelo.predict([25])
print("Te sale en " + str(resultado) + "yuan")

modelo.save('euros_a_yuan.h5')

!ls

!pip install tensorflowjs

!mkdir conversiondinero

!tensorflowjs_converter --input_format keras euros_a_yuan.h5 conversiondinero

!ls conversiondinero