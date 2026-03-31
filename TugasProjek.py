class Node:
    def __init__(self, nama, tanggal, nomor):
        self.nama = nama
        self.tanggal = tanggal
        self.nomor = nomor
        self.next = None

class SistemReservasi:
    def __init__(self):
        self.head = None

    def tambah_reservasi(self, nama, tanggal, nomor):
        new_node = Node(nama, tanggal, nomor)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def tampilkan(self):
        temp = self.head
        while temp:
            print(f"{temp.nama} - {temp.tanggal} - No:{temp.nomor}")
            temp = temp.next

    def hapus_reservasi(self, nama):
        temp = self.head
        prev = None

        while temp:
            if temp.nama == nama:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print("Reservasi dihapus")
                return
            prev = temp
            temp = temp.next

        print("Data tidak ditemukan")


# Contoh penggunaan
reservasi = SistemReservasi()
reservasi.tambah_reservasi("Andi", "2026-04-01", "A1")
reservasi.tambah_reservasi("Budi", "2026-04-01", "A2")

reservasi.tampilkan()
reservasi.hapus_reservasi("Andi")
reservasi.tampilkan()