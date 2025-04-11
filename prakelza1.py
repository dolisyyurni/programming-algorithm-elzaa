print("Nama: Elza Zahwana Putri")
print("NPM: 2417031061")
print("Kelas: A")
print("Mata Kuliah: Algoritma & Pemrograman")
print("Materi III: LATIHAN ALGORITMA & PEMROGRAMAN PYTHON (PEMROGRAMAN PYTHON: Identifier)")

nama    = input("\nMasukkan nama Anda: ")
umur    = int(input("Masukkan umur Anda (tahun): "))
tinggi  = float(input("Masukkan tinggi badan Anda (cm): "))
berat   = float(input("\nMasukkan berat badan Anda (kg): "))

# Menghitung umur dalam bulan
umur_dalam_bulan = umur * 12
# Menghitung BMI
tinggi_m = tinggi / 100  # Konversi tinggi ke meter
bmi = berat / (tinggi_m ** 2)

# Menampilkan output dengan format yang rapi
print("\nOutput:")
print(f"Nama: {nama}")
print(f"Umur dalam bulan: {umur_dalam_bulan}")
print(f"BMI: {bmi:.2f}")

# 1. Program untuk menentukan bilangan prima
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Cek faktor dari 2 hingga akar n
        if n % i == 0:
         return False
    return True

angka = int(input("\nMasukkan angka: "))
if is_prime(angka):
    print(f"{angka} adalah bilangan prima.")
else:
    print(f"{angka} bukan bilangan prima.")

# 2. Program untuk menampilkan angka Fibonacci ke-n
def fibonacci(n):
    if n <= 0:
        return "Input harus lebih dari 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

n_fib = int(input("\nMasukkan nilai n untuk Fibonacci: "))
print(f"Bilangan Fibonacci ke-{n_fib} adalah {fibonacci(n_fib)}")

# 3. Program untuk menampilkan semua angka genap dari 1 hingga N
N = int(input("\nMasukkan nilai N: "))
print(f"Angka genap dari 1 hingga {N}:")
for i in range(2, N + 1, 2):  # Loop untuk angka genap
    print(i, end=" ")
print()

# Fungsi untuk mencari nilai terbesar dan terkecil dalam sebuah list
def find_max_min(numbers):
    return max(numbers), min(numbers)

# Fungsi untuk menghitung rata-rata list
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Fungsi untuk membalik urutan list
def reverse_list(numbers):
    return numbers[::-1]

# Meminta pengguna memasukkan angka-angka dalam bentuk list
input_numbers = list(map(int, input("Masukkan angka-angka (pisahkan dengan spasi): ").split()))

# Memanggil fungsi
nilai_terbesar, nilai_terkecil = find_max_min(input_numbers)
rata_rata = calculate_average(input_numbers)
list_terbalik = reverse_list(input_numbers)

# Menampilkan hasil
print(f"\nNilai terbesar: {nilai_terbesar}")
print(f"Nilai terkecil: {nilai_terkecil}")
print(f"Rata-rata: {rata_rata:.2f}")
print(f"List terbalik: {list_terbalik}")

# 1. Membaca dan menampilkan isi file teks
def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\nIsi file:")
            print(content)
    except FileNotFoundError:
        print("File tidak ditemukan.")

# 2. Meminta input dari pengguna dan menyimpannya ke dalam file
def write_to_file(filename):
    with open(filename, "a") as file:  # "a" untuk menambah data tanpa menghapus yang lama
        nama = input("Masukkan nama: ")
        umur = input("Masukkan umur: ")
        file.write(f"{nama}, {umur}\n")
        print("Data telah disimpan.")

# 3. Menghitung jumlah baris dalam file teks
def count_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            print(f"\nJumlah baris dalam file: {len(lines)}")
    except FileNotFoundError:
        print("File tidak ditemukan.")

# Program utama
file_name = "data.txt"  # Nama file yang digunakan

while True:
    print("\nPilih operasi:")
    print("1. Baca isi file")
    print("2. Tambah data ke file")
    print("3. Hitung jumlah baris dalam file")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1-4): ")
    
    if pilihan == "1":
        read_file(file_name)
    elif pilihan == "2":
        write_to_file(file_name)
    elif pilihan == "3":
        count_lines(file_name)
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

from datetime import datetime

# 1. Kelas Mahasiswa
class Mahasiswa:
    def __init__(self, nama, umur, jurusan):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur} tahun")
        print(f"Jurusan: {self.jurusan}\n")

# 2. Kelas Mobil
class Mobil:
    def __init__(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna

    def hitung_umur(self):
        tahun_sekarang = datetime.now().year
        return tahun_sekarang - self.tahun
    def tampilkan_info(self):
        print(f"Mobil {self.merk} ({self.warna}), Tahun {self.tahun}")
        print(f"Umur mobil: {self.hitung_umur()} tahun\n")

# 3. Kelas BankAccount
class BankAccount:
    def __init__(self, saldo_awal):
        self.saldo = saldo_awal

    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Setor: {jumlah}")
        print(f"Saldo setelah setor: {self.saldo}")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak cukup!")
        else:
            self.saldo -= jumlah
            print(f"Tarik: {jumlah}")
            print(f"Saldo setelah tarik: {self.saldo}")

    def tampilkan_saldo(self):
        print(f"Saldo saat ini: {self.saldo}\n")

# ==== PROGRAM UTAMA ====
# Contoh penggunaan kelas Mahasiswa
mhs1 = Mahasiswa("Budi", 21, "Teknik Informatika")
mhs1.tampilkan_info()

# Contoh penggunaan kelas Mobil
mobil1 = Mobil("Toyota", 2015, "Hitam")
mobil1.tampilkan_info()

# Contoh penggunaan kelas BankAccount
akun = BankAccount(10000)
print(f"Saldo awal: {akun.saldo}\n")
akun.setor(5000)
akun.tarik(3000)
akun.tampilkan_saldo()

import math

# Input angka dari pengguna
angka = float(input("Masukkan angka: "))

# Hitung akar kuadrat dan logaritma
akar_kuadrat = math.sqrt(angka)
logaritma = math.log(angka)

# Tampilkan hasil
print(f"\nAkar kuadrat dari {angka} adalah: {akar_kuadrat:.2f}")
print(f"Logaritma natural (ln) dari {angka} adalah: {logaritma:.2f}")

from datetime import datetime

# Ambil waktu saat ini
waktu_sekarang = datetime.now()

# Format tanggal & waktu
tanggal = waktu_sekarang.strftime("%d-%m-%Y")
waktu = waktu_sekarang.strftime("%H:%M:%S")

# Tampilkan hasil
print(f"Tanggal hari ini: {tanggal}")
print(f"Waktu sekarang: {waktu}")

import random

# Generate angka acak antara 1-100
angka_rahasia = random.randint(1, 100)
tebakan = None

print("Tebak angka antara 1 dan 100!")

# Loop sampai tebakan benar
while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan tebakan Anda: "))
    
    if tebakan < angka_rahasia:
        print("Terlalu kecil! Coba lagi.")
    elif tebakan > angka_rahasia:
        print("Terlalu besar! Coba lagi.")

print(f"Selamat! Anda menebak angka {angka_rahasia} dengan benar.")

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Contoh penggunaan
angka = [12, 3, 45, 23, 7]
print(f"List sebelum sorting: {angka}")

# Menggunakan Bubble Sort
sorted_bubble = bubble_sort(angka.copy())
print(f"List setelah sorting (Bubble Sort): {sorted_bubble}")

# Menggunakan Insertion Sort
sorted_insertion = insertion_sort(angka.copy())
print(f"List setelah sorting (Insertion Sort): {sorted_insertion}")

# Linear Search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Mengembalikan indeks saat ditemukan
    return -1  # Jika tidak ditemukan

# Binary Search (hanya bisa digunakan pada list yang sudah terurut)
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Jika tidak ditemukan

# Contoh penggunaan
angka = [12, 3, 45, 23, 7]
sorted_angka = sorted(angka)  # Harus diurutkan dulu sebelum Binary Search

print(f"\nList setelah sorting: {sorted_angka}")

# Input angka yang dicari
cari = int(input("Masukkan angka yang ingin dicari: "))

# Pencarian dengan Linear Search
index_linear = linear_search(angka, cari)
if index_linear != -1:
    print(f"Angka {cari} ditemukan pada indeks {index_linear} (Linear Search)")
else:
    print(f"Angka {cari} tidak ditemukan (Linear Search)")

# Pencarian dengan Binary Search
index_binary = binary_search(sorted_angka, cari)
if index_binary != -1:
    print(f"Angka {cari} ditemukan pada indeks {index_binary} (Binary Search)")
else:
    print(f"Angka {cari} tidak ditemukan (Binary Search)")

# Bubble Sort untuk Nama
def bubble_sort_nama(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Linear Search untuk mencari nama
def cari_nama(arr, nama):
    for i in range(len(arr)):
        if arr[i].lower() == nama.lower():
            return i
    return -1

# Contoh list nama
nama_list = ["Zain", "Andi", "Budi", "Citra", "Dewi"]
print(f"Nama sebelum sorting: {nama_list}")

# Sorting nama
sorted_nama = bubble_sort_nama(nama_list.copy())
print(f"Nama setelah sorting: {sorted_nama}")

# Input nama yang dicari
cari = input("Masukkan nama yang ingin dicari: ")

# Pencarian
index_nama = cari_nama(sorted_nama, cari)
if index_nama != -1:
    print(f"Nama {cari} ditemukan pada indeks {index_nama}")
else:
    print(f"Nama {cari} tidak ditemukan")


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form["nama"]
        return render_template("welcome.html", nama=nama)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask
app = Flask(__name__)

app.route("/", methods=["GET", "POST"])