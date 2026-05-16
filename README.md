# Pencarian Rute Terpendek Menggunakan Algoritma Dijkstra

Project ini merupakan implementasi Algoritma Dijkstra menggunakan bahasa Python untuk mencari rute terpendek antar lokasi di Kota Bandung. Setiap lokasi direpresentasikan sebagai node pada graph, sedangkan jarak antar lokasi disimpan sebagai bobot (weight) pada edge.

Program memungkinkan pengguna untuk memasukkan lokasi awal dan lokasi tujuan secara interaktif, kemudian sistem akan menghitung:

* Jarak terpendek antar lokasi
* Rute terbaik yang dapat dilalui

## Fitur

* Implementasi Algoritma Dijkstra
* Input lokasi awal dan tujuan secara interaktif
* Menampilkan rute tercepat dan total jarak
* Mendukung pencarian berulang menggunakan looping
* Menggunakan struktur data graph berbasis dictionary
* Validasi input lokasi

## Teknologi yang Digunakan

* Python
* Library `heapq` untuk optimasi priority queue

## Contoh Output

```bash id="w2ql5s"
Masukkan lokasi awal : Pasteur
Masukkan lokasi tujuan : Sarijadi

=== HASIL PENCARIAN ===
Jarak terpendek dari Pasteur ke Sarijadi: 4.0 km
Rute: Pasteur -> Mulyasari -> Sukagalih -> Sarijadi
```

## Algoritma

Project ini menggunakan Algoritma Dijkstra, yaitu algoritma greedy yang digunakan untuk mencari jalur terpendek pada graph berbobot secara efisien.

## Tujuan Project

Project ini dibuat untuk mempelajari dan mengimplementasikan:

* Struktur data graph
* Algoritma shortest path
* Priority queue
* Simulasi pencarian rute pada dunia nyata menggunakan Python
