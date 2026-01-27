# Program LRU (Least Recently Used) Cache - Sosial Media
# Algoritma Pengelolaan Memory Cache

class LRUCache:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.cache = []
        self.hits = 0
        self.misses = 0
        
    def akses(self, sosmed_id, sosmed_nama):
        """Mengakses sosial media dan mengelola cache dengan algoritma LRU"""
        
        # Cek apakah sosmed sudah ada di cache (HIT)
        if sosmed_id in self.cache:
            self.hits += 1
            # Pindahkan ke depan (most recently used)
            self.cache.remove(sosmed_id)
            self.cache.insert(0, sosmed_id)
            status = "HIT"
            aksi = f"{sosmed_nama} sudah ada di cache, pindahkan ke depan"
        else:
            # MISS: sosmed tidak ada di cache
            self.misses += 1
            status = "MISS"
            
            # Jika cache penuh, hapus yang paling jarang digunakan (belakang)
            if len(self.cache) >= self.kapasitas:
                dihapus = self.cache.pop()
                aksi = f"Cache penuh! Hapus ID {dihapus}, tambahkan {sosmed_nama}"
            else:
                aksi = f"Tambahkan {sosmed_nama} ke cache"
            
            # Tambahkan di depan
            self.cache.insert(0, sosmed_id)
        
        return status, aksi, self.cache.copy()

def get_sosmed_nama(sosmed_id):
    """Mendapatkan nama sosial media berdasarkan ID"""
    sosmed_dict = {
        1: "WhatsApp",
        2: "Instagram", 
        3: "YouTube",
        4: "TikTok",
        5: "Twitter"
    }
    return sosmed_dict.get(sosmed_id, "Unknown")

def tampilkan_cache(cache):
    """Menampilkan isi cache dalam format yang mudah dibaca"""
    if not cache:
        return "[ Kosong ]"
    
    cache_nama = [get_sosmed_nama(id) for id in cache]
    return "[ " + " | ".join(cache_nama) + " ]"

def tampilkan_header():
    """Menampilkan header program"""
    print("\n" + "="*70)
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║        SIMULASI LRU CACHE - SOSIAL MEDIA                       ║")
    print("║        Least Recently Used Algorithm                          ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print("="*70)

def tampilkan_sosmed():
    """Menampilkan daftar sosial media"""
    print("\nDaftar Sosial Media:")
    print("-" * 40)
    print("1. 💬 WhatsApp")
    print("2. 📷 Instagram")
    print("3. ▶️  YouTube")
    print("4. 🎵 TikTok")
    print("5. 🐦 Twitter")
    print("-" * 40)

def simulasi_lru(urutan_akses, ukuran_cache):
    """Menjalankan simulasi LRU dengan urutan akses yang diberikan"""
    
    lru = LRUCache(ukuran_cache)
    
    print(f"\nUkuran Cache: {ukuran_cache} frame")
    print(f"Urutan Akses: {urutan_akses}")
    print("\n" + "="*70)
    print("LANGKAH-LANGKAH SIMULASI")
    print("="*70)
    
    for step, sosmed_id in enumerate(urutan_akses, 1):
        sosmed_nama = get_sosmed_nama(sosmed_id)
        status, aksi, cache_sekarang = lru.akses(sosmed_id, sosmed_nama)
        
        # Tampilkan setiap langkah
        print(f"\nLangkah {step}:")
        print(f"  Akses       : {sosmed_nama} (ID: {sosmed_id})")
        print(f"  Status      : {status}")
        print(f"  Aksi        : {aksi}")
        print(f"  Cache       : {tampilkan_cache(cache_sekarang)}")
        print("-" * 70)
    
    # Tampilkan statistik
    total_akses = len(urutan_akses)
    hit_ratio = (lru.hits / total_akses * 100) if total_akses > 0 else 0
    miss_ratio = (lru.misses / total_akses * 100) if total_akses > 0 else 0
    
    print("\n" + "="*70)
    print("STATISTIK HASIL")
    print("="*70)
    print(f"Total Akses       : {total_akses}")
    print(f"Cache HIT         : {lru.hits} ({hit_ratio:.2f}%)")
    print(f"Cache MISS        : {lru.misses} ({miss_ratio:.2f}%)")
    print(f"Hit Ratio         : {hit_ratio:.2f}%")
    print("="*70)

def main():
    tampilkan_header()
    tampilkan_sosmed()
    
    # Contoh 1: Urutan akses default
    print("\n" + "="*70)
    print("CONTOH 1: Simulasi dengan ukuran cache 3")
    print("="*70)
    urutan1 = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    simulasi_lru(urutan1, 3)
    
    # Contoh 2: Ukuran cache berbeda
    print("\n\n" + "="*70)
    print("CONTOH 2: Simulasi dengan ukuran cache 4")
    print("="*70)
    urutan2 = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    simulasi_lru(urutan2, 4)
    
    # Penjelasan algoritma
    print("\n" + "="*70)
    print("PENJELASAN ALGORITMA LRU")
    print("="*70)
    print("""
LRU (Least Recently Used) adalah algoritma pengelolaan cache yang 
menghapus data yang paling lama tidak digunakan ketika cache penuh.

Cara Kerja:
1. HIT  : Jika data sudah ada di cache, pindahkan ke posisi paling 
          depan (most recently used)
          
2. MISS : Jika data tidak ada di cache:
          - Jika cache penuh: hapus data paling belakang 
            (least recently used)
          - Tambahkan data baru di posisi paling depan

Posisi di Cache:
- Depan  = Baru saja digunakan (Most Recently Used)
- Belakang = Paling lama tidak digunakan (Least Recently Used)

Hit Ratio yang tinggi menunjukkan efisiensi cache yang baik!
    """)
    print("="*70 + "\n")

if __name__ == "__main__":
    main()