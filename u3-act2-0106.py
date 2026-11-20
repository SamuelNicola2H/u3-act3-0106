import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Samuel Nicola   NC=0106

# Problema 9: Cryptos (Nombre, símbolo, es de código abierto, año creación)

btc = ['Bitcoin', 'BTC', True, 2009]
eth = ['Ethereum', 'ETH', True, 2015]
sol = ['Solana', 'SOL', True, 2020]
ada = ['Cardano', 'ADA', True, 2017]
xrp = ['Ripple', 'XRP', False, 2012]

lista_de_cryptos = [btc, eth, sol, ada, xrp]

df_cryptos = pd.DataFrame(lista_de_cryptos, columns=["Nombre", "Simbolo", "Codigo_abierto", "Año"])

print(df_cryptos)

# Grafica de lineas
plt.plot(df_cryptos["Nombre"], df_cryptos["Año"])
plt.title("Grafica Cryptos 0106")
plt.xlabel("Nombre de las Cryptos")
plt.ylabel("Año de creación")
plt.show()

# Creamos una grafica de puntos
plt.scatter(df_cryptos["Nombre"], df_cryptos["Año"])
plt.title("Grafica de puntos Cryptos 0106")
plt.show()

# Grafica de barras
plt.bar(df_cryptos["Nombre"], df_cryptos["Año"])
plt.title("Grafica de barras Cryptos 0106")
plt.xlabel("Las Cryptos")
plt.ylabel("Año de creación")
plt.show()

# Ordenar la grafica de barras de manera descendente
# De la mas grande a la pequeña
df_rs_ordenar = df_cryptos.sort_values("Año", ascending=False)

plt.bar(df_rs_ordenar["Nombre"], df_rs_ordenar["Año"])
plt.title("Grafica Cryptos 0106")
plt.show()

# Coloreando la grafica
plt.bar(df_rs_ordenar["Nombre"], df_rs_ordenar["Año"],
        color=["b", "g", "c", "m", "y"])

plt.title("Grafica Cryptos 0106")
plt.show()

# Grafica de pastel
plt.pie(df_cryptos["Año"], labels=df_cryptos["Nombre"])
plt.title("Grafica de pastel Cryptos SAMUEL NICOLA 0106")
plt.show()