# 📌 Sistem Reservasi Menggunakan Queue (Linked List)

## 📖 Deskripsi

Proyek ini merupakan implementasi **struktur data Queue (Antrian)** menggunakan **Linked List** dalam sistem reservasi.

Program ini dibuat untuk memenuhi tugas **UTS Struktur Data Semester Genap 2025/2026**.

Sistem ini digunakan untuk mengelola data reservasi pelanggan secara terurut berdasarkan waktu masuk (FIFO - First In First Out).

### ❓ Rumusan Masalah

1. Bagaimana konsep queue dapat digunakan dalam sistem reservasi?
2. Bagaimana linked list membantu dalam implementasi queue?
3. Bagaimana sistem ini dapat mengelola data reservasi secara efisien?

---

## 🎯 Studi Kasus

Kasus yang digunakan adalah **Sistem Reservasi Restoran**.

Dalam sistem ini:

* Pelanggan yang melakukan reservasi lebih dulu akan dilayani lebih dulu
* Data reservasi disimpan dalam bentuk antrian

Data yang disimpan:

* Nama pelanggan
* Tanggal reservasi
* Nomor meja

---



---

## 💡 Solusi

Solusi yang digunakan adalah:

* Menggunakan **Queue (FIFO)** untuk mengatur urutan reservasi
* Menggunakan **Linked List** agar data bersifat dinamis
* Menyediakan operasi:

  * Tambah data (enqueue)
  * Hapus data (dequeue)
  * Tampilkan data

---

## 📚 Landasan Teori

Struktur data adalah cara untuk menyimpan dan mengelola data agar dapat digunakan secara efisien.

Queue adalah struktur data yang menggunakan prinsip **FIFO (First In First Out)**, dimana data yang pertama masuk akan keluar terlebih dahulu.

Linked List adalah struktur data dinamis yang terdiri dari node yang saling terhubung melalui pointer.

Implementasi queue menggunakan linked list memungkinkan penambahan dan penghapusan data dilakukan dengan efisien tanpa batasan ukuran tetap.

---

## 🔄 Desain Sistem

### Alur Sistem:

Input → Proses → Output

* Input: Data reservasi (nama, tanggal, nomor)
* Proses:

  * Tambah ke antrian (enqueue)
  * Hapus dari antrian (dequeue)
  * Menampilkan data
* Output:

  * Daftar reservasi


---

## ▶️ Cara Menjalankan

1. Jalankan program Python
2. Tambahkan data dengan fungsi `enqueue`
3. Hapus data dengan `dequeue`
4. Tampilkan data dengan `display`

---

## 📊 Contoh Output

```
Andi - 2026-04-01 - No:A1
Budi - 2026-04-01 - No:A2

Menghapus: Andi

Budi - 2026-04-01 - No:A2
```

---

## ✅ Kelebihan

* Data terurut sesuai antrian (FIFO)
* Dinamis (tidak terbatas)
* Mudah dikelola

---

## ❌ Kekurangan

* Akses data harus berurutan
* Membutuhkan memori lebih

---

## 🏁 Kesimpulan

Sistem reservasi berbasis queue menggunakan linked list mampu mengelola data secara terurut dan efisien.

Konsep FIFO sangat cocok digunakan dalam sistem reservasi karena mencerminkan urutan pelayanan di dunia nyata.

---

## 👥 Anggota Kelompok

* I Komang Galang Prabawa
* I Nyoman Gede Gata Atmaja
* I.B.Gede Ambara Sindu Negara
