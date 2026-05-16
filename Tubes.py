import heapq

# List semua lokasi
locations = [
    "Dago", "Ciumbuleuit", "Sukakarya", "Pasteur", "Jln Cibogo",
    "Babakan Jeruk 1", "Jln Hercules", "Jl Unpar 1", "Mulyasari", "Setramurni",
    "Pajajaran", "Pasir Kaliki", "Gunung Batu", "Setra Indah", "Cipedes",
    "Sukajadi", "Sukaraja", "Sarijadi", "Jl Istana Raya", "Sukagalih"
]

# Graph yang berisi jarak antar lokasi
graph = {
    "Dago": {
        "Ciumbuleuit": 4.2, "Sukakarya": 7.2, "Pasteur": 3.8, "Jln Cibogo": 7.1, "Babakan Jeruk 1": 7.0, 
        "Jln Hercules": 7.6, "Jl Unpar 1": 7.3, "Mulyasari": 6.0, "Setramurni": 6.8, "Pajajaran": 6.8, 
        "Pasir Kaliki": 5.2, "Gunung Batu": 9.2, "Setra Indah": 6.1, "Cipedes": 5.0, "Sukajadi": 5.5, 
        "Sukaraja": 8.9, "Sarijadi": 8.6, "Jl Istana Raya": 6.4, "Sukagalih": 6.5
    },
    "Ciumbuleuit": {"Dago": 4.2, "Sukakarya": 8.8, "Pasteur": 5.7, "Jln Cibogo": 8.9, "Babakan Jeruk 1": 8.7, 
        "Jln Hercules": 8.8, "Jl Unpar 1": 10.0, "Mulyasari": 8.0, "Setramurni": 7.0, 
        "Pajajaran": 9.5, "Pasir Kaliki": 7.9, "Gunung Batu": 11.9, "Setra Indah": 7.3, 
        "Cipedes": 7.2, "Sukajadi": 8.5, "Sukaraja": 12.5, "Sarijadi": 7.6, "Jl Istana Raya": 9.1, "Sukagalih": 8.1
    },
    "Sukakarya": {"Dago": 7.2, "Ciumbuleuit": 8.8, "Pasteur": 3.7, "Jln Cibogo": 1.3, "Babakan Jeruk 1": 0.26, 
        "Jln Hercules": 1.7, "Jl Unpar 1": 1.4, "Mulyasari": 1.3, "Setramurni": 1.9, "Pajajaran": 3.3, 
        "Pasir Kaliki": 3.9, "Gunung Batu": 3.6, "Setra Indah": 1.4, "Cipedes": 1.9, "Sukajadi": 1.9, 
        "Sukaraja": 3.2, "Sarijadi": 2.9, "Jl Istana Raya": 4.3, "Sukagalih": 0.75
    },
    "Pasteur": {
        "Dago": 3.8, "Ciumbuleuit": 5.7, "Sukakarya": 3.7, "Jln Cibogo": 4.7, "Babakan Jeruk 1": 3.0,
        "Jln Hercules": 4.3, "Jl Unpar 1": 4.9, "Mulyasari": 1.8, "Setramurni": 3.4, "Pajajaran": 4.3,
        "Pasir Kaliki": 3.1, "Gunung Batu": 6.9, "Setra Indah": 2.7, "Cipedes": 1.7, "Sukajadi": 1.3,
        "Sukaraja": 6.4, "Sarijadi": 5.0, "Jl Istana Raya": 3.9, "Sukagalih": 2.2
    },
    "Jln Cibogo": {
        "Pasteur": 4.7, "Dago": 7.1, "Ciumbuleuit": 8.9, "Sukakarya": 1.3, "Babakan Jeruk 1": 1.8,
        "Jln Hercules": 0.35, "Jl Unpar 1": 0.9, "Mulyasari": 2.6, "Setramurni": 2.5, "Pajajaran": 2.8,
        "Pasir Kaliki": 4.6, "Gunung Batu": 3.0, "Setra Indah": 3.2, "Cipedes": 3.9, "Sukajadi": 2.6,
        "Sukaraja": 2.7, "Sarijadi": 1.8, "Jl Istana Raya": 5.0, "Sukagalih": 2.9
    },
    "Babakan Jeruk 1": {
        "Pasteur": 3.0, "Jln Cibogo": 1.8, "Dago": 7.0, "Ciumbuleuit": 8.7, "Sukakarya": 0.26,
        "Jln Hercules": 2.0, "Jl Unpar 1": 1.7, "Mulyasari": 1.7, "Setramurni": 2.2, "Pajajaran": 3.6,
        "Pasir Kaliki": 3.6, "Gunung Batu": 3.8, "Setra Indah": 1.3, "Cipedes": 2.0, "Sukajadi": 1.6,
        "Sukaraja": 3.5, "Sarijadi": 3.1, "Jl Istana Raya": 4.1, "Sukagalih": 0.8
    },
    "Jln Hercules": {
        "Pasteur": 4.3, "Jln Cibogo": 0.35, "Babakan Jeruk 1": 2.0, "Dago": 7.6, "Ciumbuleuit": 8.8,
        "Sukakarya": 1.7, "Jl Unpar 1": 0.55, "Mulyasari": 2.6, "Setramurni": 2.3, "Pajajaran": 2.8,
        "Pasir Kaliki": 4.5, "Gunung Batu": 3.0, "Setra Indah": 3.0, "Cipedes": 3.8, "Sukajadi": 2.5,
        "Sukaraja": 2.7, "Sarijadi": 1.6, "Jl Istana Raya":5.0, "Sukagalih": 2.9
    },

    "Jl Unpar 1": {
        "Pasteur": 4.9, "Jln Cibogo": 0.9, "Babakan Jeruk 1": 1.7, "Jln Hercules": 0.55, "Dago": 7.3,
        "Ciumbuleuit": 10.0, "Sukakarya": 1.4, "Mulyasari": 2.3, "Setramurni": 2.8, "Pajajaran": 2.4,
        "Pasir Kaliki": 4.2, "Gunung Batu": 2.6, "Setra Indah": 3.2, "Cipedes": 3.5, "Sukajadi": 2.2,
        "Sukaraja": 2.3, "Sarijadi": 2.1, "Jl Istana Raya": 4.6, "Sukagalih": 2.5
    },
    "Mulyasari": {
        "Pasteur": 1.8, "Jln Cibogo": 2.6, "Babakan Jeruk 1": 1.7, "Jln Hercules": 2.6, "Jl Unpar 1": 2.3,
        "Dago": 6.0, "Ciumbuleuit": 8.0, "Sukakarya": 1.3, "Setramurni": 2.9, "Pajajaran": 4.1,
        "Pasir Kaliki": 3.3, "Gunung Batu": 4.9, "Setra Indah": 1.1, "Cipedes": 1.1, "Sukajadi": 0.5,
        "Sukaraja": 4.6, "Sarijadi": 3.2, "Jl Istana Raya": 3.7, "Sukagalih": 0.5
    },
    "Setramurni": {
        "Pasteur": 3.4, "Jln Cibogo": 2.5, "Babakan Jeruk 1": 2.2, "Jln Hercules": 2.3, "Jl Unpar 1": 2.8,
        "Mulyasari": 2.9, "Dago": 6.8, "Ciumbuleuit": 7.0, "Sukakarya": 1.9, "Pajajaran": 5.0,
        "Pasir Kaliki": 5.6, "Gunung Batu": 5.2, "Setra Indah": 1.9, "Cipedes": 2.8, "Sukajadi": 3.0,
        "Sukaraja": 4.9, "Sarijadi": 1.0, "Jl Istana Raya": 6, "Sukagalih": 2.0
    },
    "Pajajaran": {
        "Pasteur": 4.3, "Jln Cibogo": 2.8, "Babakan Jeruk 1": 3.6, "Jln Hercules": 2.8, "Jl Unpar 1": 2.4,
        "Mulyasari": 4.1, "Setramurni": 5.0, "Dago": 6.8, "Ciumbuleuit": 9.5, "Sukakarya": 3.6,
        "Pasir Kaliki": 3.1, "Gunung Batu": 5.2, "Setra Indah": 2.7, "Cipedes": 2.7, "Sukajadi": 3.4,
        "Sukaraja": 4.9, "Sarijadi": 2.7, "Jl Istana Raya": 2.7, "Sukagalih": 4.3
    },
    "Pasir Kaliki": {
        "Pasteur": 3.1, "Jln Cibogo": 4.6, "Babakan Jeruk 1": 3.6, "Jln Hercules": 4.5, "Jl Unpar 1": 4.2,
        "Mulyasari": 3.3, "Setramurni": 5.6, "Pajajaran": 3.1, "Dago": 5.2, "Ciumbuleuit": 7.9,
        "Sukakarya": 3.6, "Gunung Batu": 6.8, "Setra Indah": 3.4, "Cipedes": 3.5, "Sukajadi": 3.7,
        "Sukaraja": 5.8, "Sarijadi": 2.2, "Jl Istana Raya": 2.4, "Sukagalih": 4.3
    },
        "Gunung Batu": {
        "Pasteur": 6.9, "Jln Cibogo": 3.3, "Babakan Jeruk 1": 3.8, "Jln Hercules": 3.0, "Jl Unpar 1": 2.6,
        "Mulyasari": 4.9, "Setramurni": 5.2, "Pajajaran": 5.2, "Pasir Kaliki": 6.8, "Dago": 9.2,
        "Ciumbuleuit": 11.9, "Sukakarya": 3.0, "Setra Indah": 4.7, "Cipedes": 5.0, "Sukajadi": 4.7,
        "Sukaraja": 5.8, "Sarijadi": 3.6, "Jl Istana Raya": 4.0, "Sukagalih": 4.0
    },
    "Setra Indah": {
        "Pasteur": 2.7, "Jln Cibogo": 3.2, "Babakan Jeruk 1": 3.0, "Jln Hercules": 3.3, "Jl Unpar 1": 3.5,
        "Mulyasari": 1.7, "Setramurni": 1.9, "Pajajaran": 2.7, "Pasir Kaliki": 3.4, "Gunung Batu": 4.7,
        "Dago": 6.1, "Ciumbuleuit": 7.3, "Sukakarya": 2.7, "Cipedes": 1.4, "Sukajadi": 1.6,
        "Sukaraja": 4.6, "Sarijadi": 0.8, "Jl Istana Raya": 0.8, "Sukagalih": 0.8
    },
    "Cipedes": {
        "Pasteur": 1.7, "Jln Cibogo": 3.9, "Babakan Jeruk 1": 3.2, "Jln Hercules": 3.8, "Jl Unpar 1": 3.5,
        "Mulyasari": 1.1, "Setramurni": 2.8, "Pajajaran": 2.7, "Pasir Kaliki": 3.5, "Gunung Batu": 5.0,
        "Setra Indah": 1.4, "Dago": 5.0, "Ciumbuleuit": 7.2, "Sukakarya": 1.9, "Sukajadi": 1.4,
        "Sukaraja": 3.7, "Sarijadi": 1.2, "Jl Istana Raya": 1.2, "Sukagalih": 1.2
    },
    "Sukajadi": {
        "Pasteur": 2.6, "Jln Cibogo": 3.2, "Babakan Jeruk 1": 3.3, "Jln Hercules": 3.8, "Jl Unpar 1": 3.2,
        "Mulyasari": 1.6, "Setramurni": 3.0, "Pajajaran": 3.4, "Pasir Kaliki": 3.7, "Gunung Batu": 4.7,
        "Setra Indah": 1.6, "Cipedes": 1.4, "Dago": 5.5, "Ciumbuleuit": 8.5, "Sukakarya": 1.9,
        "Sukaraja": 4.7, "Sarijadi": 1.6, "Jl Istana Raya": 2.6, "Sukagalih": 1.7
    },
    "Sukaraja": {
        "Pasteur": 6.4, "Jln Cibogo": 2.7, "Babakan Jeruk 1": 3.5, "Jln Hercules": 2.7, "Jl Unpar 1": 3.2,
        "Mulyasari": 4.6, "Setramurni": 4.9, "Pajajaran": 4.9, "Pasir Kaliki": 5.8, "Gunung Batu": 5.8,
        "Setra Indah": 4.6, "Cipedes": 3.7, "Sukajadi": 4.7, "Dago": 8.9, "Ciumbuleuit": 9.9,
        "Sukakarya": 3.5, "Sarijadi": 2.2, "Jl Istana Raya": 3.5, "Sukagalih": 3.7
    },
    "Sarijadi": {
        "Pasteur": 5.0, "Jln Cibogo": 1.8, "Babakan Jeruk 1": 1.3, "Jln Hercules": 1.6, "Jl Unpar 1": 2.1,
        "Mulyasari": 3.2, "Setramurni": 1.0, "Pajajaran": 2.7, "Pasir Kaliki": 2.2, "Gunung Batu": 3.6,
        "Setra Indah": 0.8, "Cipedes": 1.2, "Sukajadi": 1.6, "Sukaraja": 2.2, "Dago": 8.6,
        "Ciumbuleuit": 10.1, "Sukakarya": 3.1, "Jl Istana Raya": 2.2, "Sukagalih": 1.0
    },
    "Jl Istana Raya": {
        "Pasteur": 3.9, "Jln Cibogo": 2.9, "Babakan Jeruk 1": 2.0, "Jln Hercules": 2.9, "Jl Unpar 1": 3.2,
        "Mulyasari": 3.3, "Setramurni": 2.6, "Pajajaran": 2.7, "Pasir Kaliki": 2.4, "Gunung Batu": 4.0,
        "Setra Indah": 0.8, "Cipedes": 1.2, "Sukajadi": 2.6, "Sukaraja": 3.5, "Sarijadi": 2.2,
        "Dago": 6.4, "Ciumbuleuit": 9.1, "Sukakarya": 2.9, "Sukagalih": 1.2
    },
    "Sukagalih": {
        "Pasteur": 2.2, "Jln Cibogo": 2.9, "Babakan Jeruk 1": 0.8, "Jln Hercules": 2.9, "Jl Unpar 1": 2.5,
        "Mulyasari": 0.5, "Setramurni": 2.5, "Pajajaran": 4.3, "Pasir Kaliki": 4.3, "Gunung Batu": 4.0,
        "Setra Indah": 0.8, "Cipedes": 1.2, "Sukajadi": 1.7, "Sukaraja": 3.7, "Sarijadi": 1.0,
        "Jl Istana Raya": 1.2, "Dago": 6.0, "Ciumbuleuit": 7.5, "Sukakarya": 2.9
    }
}


# =========================
# ALGORITMA DIJKSTRA
# =========================
def dijkstra(graph, start, goal):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        # Jika tujuan ditemukan
        if node == goal:
            return (cost, path)

        # Cek tetangga
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    queue,
                    (cost + graph[node][neighbor], neighbor, path)
                )

    return (float("inf"), [])

# =========================
# PROGRAM UTAMA (LOOP)
# =========================
while True:

    print("\n==============================")
    print("      PENCARIAN RUTE")
    print("==============================")

    # Tampilkan daftar lokasi
    print("\nDaftar Lokasi:")
    for lokasi in graph.keys():
        print("-", lokasi)

    # Input user
    start = input("\nMasukkan lokasi awal : ")
    goal = input("Masukkan lokasi tujuan : ")

    # Validasi input
    if start not in graph:
        print(f"\nLokasi awal '{start}' tidak ditemukan!")
    elif goal not in graph:
        print(f"\nLokasi tujuan '{goal}' tidak ditemukan!")
    else:
        # Hitung jalur terpendek
        cost, path = dijkstra(graph, start, goal)

        # Output hasil
        print("\n=== HASIL PENCARIAN ===")
        print(f"Jarak terpendek dari {start} ke {goal}: {cost} km")
        print("Rute:", " -> ".join(path))

    # Tanya ulang
    ulang = input("\nApakah ingin mencari rute lagi? (y/n): ").lower()

    if ulang != 'y':
        print("\nTerima kasih telah menggunakan program!")
        break