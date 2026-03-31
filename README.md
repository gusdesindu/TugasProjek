# 📌 Sistem Reservasi dengan Linked List

## 📖 Deskripsi

Proyek ini merupakan implementasi sederhana dari **struktur data Linked List** dalam bentuk **sistem reservasi**.
Program ini dibuat untuk memenuhi tugas mata pelajaran Struktur Data.

Sistem ini memungkinkan pengguna untuk:

* Menambahkan data reservasi
* Menampilkan daftar reservasi
* Menghapus data reservasi

---

## 🎯 Latar Belakang

Sistem reservasi sering digunakan dalam kehidupan sehari-hari seperti:

* Reservasi restoran
* Booking hotel
* Pemesanan tiket

Karena data reservasi sering berubah (ditambah dan dihapus), maka digunakan **Linked List** yang bersifat dinamis dan fleksibel.

---

## 🧩 Konsep yang Digunakan

Linked List adalah struktur data yang terdiri dari node, dimana setiap node memiliki:

* Data (nama, tanggal, nomor)
* Pointer ke node berikutnya

Keunggulan:

* Tidak perlu ukuran tetap
* Mudah menambah dan menghapus data

---

## 📂 Studi Kasus

Contoh kasus: **Reservasi Restoran**

Setiap pelanggan memiliki data:

* Nama
* Tanggal reservasi
* Nomor meja

Sistem dapat:

* Menambahkan reservasi baru
* Menampilkan semua reservasi
* Menghapus reservasi tertentu

---

## ❓ Rumusan Masalah

1. Bagaimana menyimpan data reservasi secara dinamis?
2. Bagaimana menambahkan data tanpa mengganggu data lain?
3. Bagaimana menghapus data dengan efisien?
4. Bagaimana menampilkan seluruh data reservasi?

---

## ⚙️ Implementasi Program

```python
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

# Contoh penggunaan
reservasi = SistemReservasi()
reservasi.tambah_reservasi("Andi", "2026-04-01", "A1")
reservasi.tambah_reservasi("Budi", "2026-04-01", "A2")

reservasi.tampilkan()
reservasi.hapus_reservasi("Andi")
reservasi.tampilkan()
```

---

## ▶️ Cara Menjalankan Program

1. Pastikan Python sudah terinstall
2. Jalankan file program
3. Output akan tampil di terminal

---

## 📊 Contoh Output

```
Andi - 2026-04-01 - No:A1
Budi - 2026-04-01 - No:A2

Reservasi dihapus

Budi - 2026-04-01 - No:A2
```

---

## ✅ Kelebihan

* Struktur data dinamis
* Mudah menambah dan menghapus data
* Efisien untuk data yang sering berubah

---

## ❌ Kekurangan

* Tidak bisa akses langsung (harus traversal)
* Menggunakan memori lebih banyak

---

## 🏁 Kesimpulan

Linked List sangat cocok digunakan dalam sistem reservasi karena fleksibel dan efisien dalam mengelola data yang dinamis.

---

## 👥 Anggota Kelompok

* Orang 1
* Orang 2
* Orang 3

---

## 📌 Catatan

Proyek ini dibuat untuk keperluan pembelajaran dan pengenalan struktur data Linked List.
