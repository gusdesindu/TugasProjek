# 📌 Sistem Reservasi Menggunakan Queue (Linked List)

## 📖 Deskripsi

Proyek ini merupakan implementasi **struktur data Queue (Antrian)** menggunakan **Linked List** dalam sebuah sistem reservasi.

Sistem ini menerapkan konsep **FIFO (First In First Out)**, dimana data yang masuk pertama akan diproses atau dihapus terlebih dahulu.

### Alasan Memilih Sistem Ini
Sistem reservasi menggunakan Queue (Linked List) dipilih karena sesuai dengan konsep antrian di dunia nyata, khususnya pada restoran yang menerapkan prinsip FIFO (First In First Out).

Selain itu, penggunaan Linked List membuat penyimpanan data menjadi lebih dinamis dan efisien, sehingga cocok untuk mengelola data reservasi yang terus bertambah.

Sistem ini juga membantu memahami penerapan langsung struktur data dalam kasus nyata serta mudah untuk dikembangkan lebih lanjut.

### 🎯 Studi Kasus

Studi kasus yang digunakan adalah **Sistem Reservasi Restoran**.

Dalam sistem ini:

* Pelanggan melakukan reservasi meja
* Data disimpan dalam bentuk antrian
* Pelanggan yang lebih dulu reservasi akan diproses lebih dulu

Data yang disimpan:

* Nama pelanggan
* Tanggal reservasi
* Nomor meja

### ❓ Rumusan Masalah

1. Bagaimana konsep queue dapat diterapkan dalam sistem reservasi?
2. Bagaimana linked list digunakan untuk mengimplementasikan queue?
3. Bagaimana sistem dapat mengelola data reservasi secara efisien?

### 💡 Solusi

Solusi yang digunakan dalam sistem ini adalah:

* Menggunakan **Queue (FIFO)** untuk mengatur urutan reservasi
* Menggunakan **Linked List** agar data bersifat dinamis
* Mengimplementasikan operasi utama queue:

  * Enqueue (tambah data)
  * Dequeue (hapus data depan)
  * Peek (melihat data terdepan)
  * Display (menampilkan seluruh data)

---

## 📚 Landasan Teori

Struktur data merupakan cara untuk mengorganisasi data agar dapat diproses secara efisien dalam suatu sistem. Struktur data sangat penting dalam pengembangan program karena mempengaruhi kinerja dan efisiensi pengolahan data.

Queue adalah struktur data linear yang menggunakan prinsip **FIFO (First In First Out)**, yaitu data yang pertama masuk akan menjadi data pertama yang keluar. Konsep ini banyak diterapkan dalam sistem antrian seperti reservasi dan pelayanan pelanggan.

Linked List merupakan struktur data dinamis yang terdiri dari node yang saling terhubung. Setiap node memiliki data dan pointer ke node berikutnya, sehingga memudahkan proses penambahan dan penghapusan data tanpa batasan ukuran.

#### 📖 Daftar Pustaka

1. Rosa A.S., dan M. Shalahuddin. 2018. *Rekayasa Perangkat Lunak Terstruktur dan Berorientasi Objek*. Bandung: Informatika.

2. Abdul Kadir. 2014. *Dasar Pemrograman*. Yogyakarta: Andi.

3. Wahana Komputer. 2015. *Struktur Data dengan Python*. Semarang: Andi Publisher.

---

## 🔄 Desain Sistem

### Alur Sistem:

Input → Proses → Output

* **Input:** Data reservasi (nama, tanggal, nomor)
* **Proses:**

  * Enqueue (menambah data)
  * Dequeue (menghapus data depan)
  * Peek (melihat data depan)
  * Display (menampilkan data)
* **Output:** Daftar reservasi

---



# Contoh penggunaan
reservasi = QueueReservasi()

reservasi.enqueue("Andi", "2026-04-01", "A1")
reservasi.enqueue("Budi", "2026-04-01", "A2")
reservasi.enqueue("Citra", "2026-04-01", "A3")

reservasi.display()
reservasi.peek()
reservasi.dequeue()
reservasi.display()
```

---

## ▶️ Cara Menjalankan

1. Pastikan Python sudah terinstall
2. Jalankan file program
3. Gunakan fungsi:

   * `enqueue()` untuk menambah data
   * `dequeue()` untuk menghapus data depan
   * `peek()` untuk melihat data terdepan
   * `display()` untuk menampilkan semua data

---

## 📊 Contoh Output

```
Reservasi ditambahkan
Reservasi ditambahkan
Reservasi ditambahkan

Daftar Reservasi:
Andi - 2026-04-01 - No:A1
Budi - 2026-04-01 - No:A2
Citra - 2026-04-01 - No:A3

Data terdepan: Andi - 2026-04-01 - No:A1

Menghapus: Andi

Daftar Reservasi:
Budi - 2026-04-01 - No:A2
Citra - 2026-04-01 - No:A3
```

---

## ✅ Kelebihan

* Menggunakan prinsip FIFO (adil sesuai urutan)
* Struktur dinamis (tidak terbatas)
* Operasi lebih efisien dengan pointer head dan rear

---

## ❌ Kekurangan

* Tidak bisa akses data secara langsung
* Membutuhkan memori tambahan untuk pointer

---

## 🏁 Kesimpulan

Sistem reservasi berbasis Queue menggunakan Linked List dapat mengelola data secara terurut dan efisien.

Konsep FIFO sangat sesuai dengan sistem reservasi karena mencerminkan urutan pelayanan di dunia nyata.

Semua operasi utama queue (enqueue, dequeue, peek, display) telah berhasil diimplementasikan.

---

## 👥 Anggota Kelompok

* I Komang Galang Prabawa
* I Nyoman Gede Gata Atmaja
* I.B.Gede Ambara Sindu Negara
