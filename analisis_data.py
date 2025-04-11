# Program Analisis Data (butuh file data_penjualan.csv)
import pandas as pd
import matplotlib.pyplot as plt

# Membaca dataset
df_penjualan = pd.read_csv('data_penjualan.csv') 

# Statistik deskriptif
print("Statistik Deskriptif:\n", df_penjualan.describe())

# Rata-rata penjualan
rata_penjualan = df_penjualan['penjualan'].mean()
print(f"Rata-rata penjualan: {rata_penjualan}")

# Visualisasi
plt.hist(df_penjualan['penjualan'], bins=20, edgecolor='black')
plt.title('Distribusi Penjualan')
plt.xlabel('Penjualan')
plt.ylabel('Frekuensi')
plt.show()
