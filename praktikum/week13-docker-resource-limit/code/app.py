#!/usr/bin/env python3
"""
Program uji untuk mengamati dampak resource limit pada Docker container
"""
import time
import sys
import psutil
import os

def print_system_info():
    """Menampilkan informasi sistem"""
    print("=" * 60)
    print("INFORMASI SISTEM")
    print("=" * 60)
    print(f"CPU Count: {psutil.cpu_count()}")
    print(f"Memory Total: {psutil.virtual_memory().total / (1024**3):.2f} GB")
    print(f"Memory Available: {psutil.virtual_memory().available / (1024**3):.2f} GB")
    print("=" * 60)
    print()

def cpu_intensive_task(duration=10):
    """
    Tugas yang menggunakan CPU secara intensif
    Args:
        duration: Durasi dalam detik
    """
    print(f"[CPU TEST] Memulai komputasi intensif selama {duration} detik...")
    start_time = time.time()
    iterations = 0
    
    while time.time() - start_time < duration:
        # Operasi matematika yang menggunakan CPU
        result = sum([i**2 for i in range(1000)])
        iterations += 1
    
    elapsed = time.time() - start_time
    print(f"[CPU TEST] Selesai!")
    print(f"  - Durasi: {elapsed:.2f} detik")
    print(f"  - Iterasi: {iterations:,}")
    print(f"  - Iterasi/detik: {iterations/elapsed:,.0f}")
    print()

def memory_intensive_task(mb_size=200, steps=10):
    """
    Tugas yang mengalokasikan memori secara bertahap
    Args:
        mb_size: Total memori yang akan dialokasikan (MB)
        steps: Jumlah langkah alokasi
    """
    print(f"[MEMORY TEST] Mengalokasikan {mb_size} MB memori dalam {steps} langkah...")
    arrays = []
    step_size = mb_size // steps
    
    try:
        for i in range(steps):
            # Alokasikan array (1 MB = 1024*1024 bytes, menggunakan array integer)
            size = step_size * 1024 * 1024 // 8  # 8 bytes per integer
            arr = [0] * size
            arrays.append(arr)
            
            mem_info = psutil.virtual_memory()
            used_mb = mem_info.used / (1024**2)
            available_mb = mem_info.available / (1024**2)
            
            print(f"  Step {i+1}/{steps}: Allocated {(i+1)*step_size} MB "
                  f"| Used: {used_mb:.0f} MB | Available: {available_mb:.0f} MB")
            time.sleep(0.5)
        
        print(f"[MEMORY TEST] Berhasil mengalokasikan {mb_size} MB")
        print(f"[MEMORY TEST] Menahan memori selama 5 detik...")
        time.sleep(5)
        print(f"[MEMORY TEST] Selesai!")
        
    except MemoryError:
        print(f"[MEMORY TEST] ERROR: Gagal mengalokasikan memori!")
        print(f"[MEMORY TEST] Memori tidak cukup setelah alokasi {len(arrays)*step_size} MB")
    except Exception as e:
        print(f"[MEMORY TEST] ERROR: {e}")
    
    print()

def monitor_resources(duration=5):
    """
    Monitor penggunaan resource secara real-time
    Args:
        duration: Durasi monitoring dalam detik
    """
    print(f"[MONITOR] Memantau penggunaan resource selama {duration} detik...")
    print("-" * 60)
    
    for i in range(duration):
        cpu_percent = psutil.cpu_percent(interval=1)
        mem_info = psutil.virtual_memory()
        mem_percent = mem_info.percent
        mem_used = mem_info.used / (1024**2)
        
        print(f"  T+{i+1}s | CPU: {cpu_percent:5.1f}% | Memory: {mem_percent:5.1f}% ({mem_used:.0f} MB)")
    
    print("-" * 60)
    print()

def main():
    print("\n" + "=" * 60)
    print("DOCKER RESOURCE LIMIT - PROGRAM UJI")
    print("=" * 60)
    print()
    
    # Tampilkan info sistem
    print_system_info()
    
    # Test 1: CPU Intensive
    print("### TEST 1: CPU INTENSIVE ###")
    cpu_intensive_task(duration=10)
    
    # Test 2: Memory Monitoring
    print("### TEST 2: RESOURCE MONITORING ###")
    monitor_resources(duration=5)
    
    # Test 3: Memory Intensive
    print("### TEST 3: MEMORY ALLOCATION ###")
    memory_intensive_task(mb_size=200, steps=10)
    
    print("=" * 60)
    print("SEMUA TEST SELESAI")
    print("=" * 60)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[INFO] Program dihentikan oleh user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan: {e}")
        sys.exit(1)