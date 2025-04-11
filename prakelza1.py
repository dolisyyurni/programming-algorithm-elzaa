# Program Inventaris
class Item:
    def __init__(self, id_item, nama_item, jumlah_stok):
        self.id_item = id_item
        self.nama_item = nama_item
        self.jumlah_stok = jumlah_stok

    def __str__(self):
        return f"ID: {self.id_item}, Nama: {self.nama_item}, Stok: {self.jumlah_stok}"

class Inventaris:
    def __init__(self):
        self.items = {}

    def tambah_item(self, item):
        self.items[item.id_item] = item

    def kurangi_stok(self, id_item, jumlah):
        if id_item in self.items:
            item = self.items[id_item]
            if item.jumlah_stok >= jumlah:
                item.jumlah_stok -= jumlah
                return True
            else:
                print("Stok tidak cukup")
        return False

    def tampilkan_item(self):
        for item in self.items.values():
            print(item)

    def cari_item(self, id_item=None, nama_item=None):
        for item in self.items.values():
            if (id_item and item.id_item == id_item) or (nama_item and item.nama_item == nama_item):
                print(item)

# Contoh penggunaan
inventaris_program = Inventaris()
item_a = Item(1, "Laptop", 10)
item_b = Item(2, "Smartphone", 20)
inventaris_program.tambah_item(item_a)
inventaris_program.tambah_item(item_b)
inventaris_program.tampilkan_item()
inventaris_program.kurangi_stok(1, 3)
inventaris_program.cari_item(nama_item="Laptop")

# Program QuickSort dan Binary Search
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Contoh penggunaan
arr_angka = [12, 4, 7, 9, 3, 15, 8, 6]
print("Array sebelum diurutkan:", arr_angka)
arr_terurut = quicksort(arr_angka)
print("Array setelah diurutkan:", arr_terurut)

target_angka = 9
hasil = binary_search(arr_terurut, target_angka)
if hasil != -1:
    print(f"Elemen {target_angka} ditemukan pada indeks {hasil}")
else:
    print(f"Elemen {target_angka} tidak ditemukan.")

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

# Program Tower of Hanoi
def tower_of_hanoi(n, from_peg, to_peg, aux_peg):
    if n == 1:
        print(f"Move disk 1 from {from_peg} to {to_peg}")
        return
    tower_of_hanoi(n - 1, from_peg, aux_peg, to_peg)
    print(f"Move disk {n} from {from_peg} to {to_peg}")
    tower_of_hanoi(n - 1, aux_peg, to_peg, from_peg)

# Contoh penggunaan
jumlah_cakram = 3
tower_of_hanoi(jumlah_cakram, 'A', 'C', 'B')

# Program KNN dengan scikit-learn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Memuat dataset Iris
iris = load_iris()
X, y = iris.data, iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model dan pelatihan
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

# Prediksi
y_prediksi = knn_model.predict(X_test)

# Akurasi
akurasi = accuracy_score(y_test, y_prediksi)
print(f"Akurasi KNN: {akurasi * 100:.2f}%")
