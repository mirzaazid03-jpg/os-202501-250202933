import sys
sys.dont_write_bytecode = True

from kasir_FCFS import simulasi_kasir
from page import simulasi_lru


def garis():
    """Menampilkan garis pemisah"""
    print("=" * 60)


def jeda():
    """Memberi jeda agar user bisa membaca output"""
    input("\nTekan ENTER untuk kembali ke menu...")


def tampilkan_judul():
    garis()
    print("        MINI SIMULASI SISTEM OPERASI")
    print("   CPU Scheduling & Memory Management")
    print("   Proyek Kelompok - Sistem Operasi")
    garis()


def tampilkan_menu():
    print("\nMENU UTAMA")
    print("1. Simulasi CPU Scheduling FCFS (Kasir)")
    print("2. Simulasi Page Replacement (LRU)")
    print("3. Jalankan Semua Simulasi")
    print("0. Keluar Program")
    garis()


def menu():
    while True:
        tampilkan_judul()
        tampilkan_menu()

        pilihan = input("Masukkan pilihan Anda (0-3): ").strip()

        if pilihan == "1":
            garis()
            print("SIMULASI CPU SCHEDULING FCFS (KASIR)")
            garis()
            simulasi_kasir()
            jeda()

        elif pilihan == "2":
            garis()
            print("SIMULASI PAGE REPLACEMENT - LRU")
            garis()
            simulasi_lru()
            jeda()

        elif pilihan == "3":
            garis()
            print("MENJALANKAN SEMUA SIMULASI")
            garis()
            simulasi_kasir()
            garis()
            simulasi_lru()
            jeda()

        elif pilihan == "0":
            garis()
            print("Terima kasih telah menggunakan simulator.")
            print("Program dihentikan.")
            garis()
            break

        else:
            print("\n❌ Pilihan tidak valid!")
            print("Silakan masukkan angka antara 0 sampai 3.")
            jeda()


if __name__ == "__main__":
    menu()

