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