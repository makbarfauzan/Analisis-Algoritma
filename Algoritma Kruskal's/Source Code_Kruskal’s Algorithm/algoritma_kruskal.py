# Muhamad Akbar Fauzan 23343075
# Program Pencarian Pohon Rentang Minimum dengan Algoritma Kruskal

class HimpunanTerpisah:
    def __init__(self, jumlah_simpul):
        self.induk = [i for i in range(jumlah_simpul)]  # Inisialisasi setiap simpul sebagai induk dirinya sendiri
        self.peringkat = [0] * jumlah_simpul  # Peringkat untuk optimasi penggabungan

    def cari(self, simpul):
        if self.induk[simpul] != simpul:
            self.induk[simpul] = self.cari(self.induk[simpul])  # Path Compression
        return self.induk[simpul]

    def gabung(self, simpul1, simpul2):
        akar1 = self.cari(simpul1)
        akar2 = self.cari(simpul2)

        if akar1 != akar2:
            if self.peringkat[akar1] > self.peringkat[akar2]:
                self.induk[akar2] = akar1
            elif self.peringkat[akar1] < self.peringkat[akar2]:
                self.induk[akar1] = akar2
            else:
                self.induk[akar2] = akar1
                self.peringkat[akar1] += 1

def kruskal(jumlah_simpul, sisi):
    sisi.sort(key=lambda x: x[2])  # Urutkan sisi berdasarkan bobot
    himpunan = HimpunanTerpisah(jumlah_simpul)
    pohon_rentang = []

    for simpul1, simpul2, bobot in sisi:
        if himpunan.cari(simpul1) != himpunan.cari(simpul2):  # Cek apakah simpul dalam komponen berbeda
            himpunan.gabung(simpul1, simpul2)
            pohon_rentang.append((simpul1, simpul2, bobot))

    return pohon_rentang

# Contoh penggunaan                                                 
sisi = [                                                            
    (0, 1, 10),  # Sisi antara simpul 0 dan 1 dengan bobot 10       
    (0, 2, 6),   # Sisi antara simpul 0 dan 2 dengan bobot 6        
    (0, 3, 5),   # Sisi antara simpul 0 dan 3 dengan bobot 5        
    (1, 3, 15),  # Sisi antara simpul 1 dan 3 dengan bobot 15       
    (2, 3, 4)    # Sisi antara simpul 2 dan 3 dengan bobot 4        
]                                                                   
                                                    
# visualisasi dalam bentuk graf
#    (10)
#  0 ----- 1
#  | \     |
# (6) (5) (15)
#  |     \ |
#  2 ----- 3
#     (4)
                                                                    
jumlah_simpul = 4  # Jumlah simpul dalam graf
hasil_mst = kruskal(jumlah_simpul, sisi)

print("Pohon Rentang Minimum:")
for simpul1, simpul2, bobot in hasil_mst:
    print(f"{simpul1} -- {simpul2} == {bobot}")


# visualisasi hasil program dalam bentuk graf
#    (10)
#  0 ----- 1
#    \     
#     (5) 
#        \ 
#  2 ----- 3
#     (4)
