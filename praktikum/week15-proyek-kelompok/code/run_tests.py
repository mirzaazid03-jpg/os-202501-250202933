# File: data/sample_processes.csv
"""
pid,arrival_time,burst_time
P1,0,5
P2,1,3
P3,2,8
P4,3,6
"""

# File: data/test_case_1.csv
"""
pid,arrival_time,burst_time
P1,0,10
P2,0,5
P3,0,8
"""

# File: data/test_case_2.csv
"""
pid,arrival_time,burst_time
P1,0,7
P2,2,4
P3,4,1
P4,5,4
"""

# File: run_tests.py
"""
Script untuk menjalankan semua test cases secara otomatis
"""

from cpu_scheduler import CPUScheduler, Process, create_sample_data, load_from_csv
import os

def run_all_tests():
    """Jalankan semua test cases"""
    
    print("="*80)
    print(" AUTOMATED TESTING - CPU SCHEDULER ".center(80, "="))
    print("="*80 + "\n")
    
    # Create sample data jika belum ada
    if not os.path.exists('data'):
        os.makedirs('data')
        create_sample_data()
    
    # Test Case 1: Sample data default
    print("\n" + "="*80)
    print("TEST CASE 1: Sample Data Default")
    print("="*80)
    
    processes = [
        Process('P1', 0, 5),
        Process('P2', 1, 3),
        Process('P3', 2, 8),
        Process('P4', 3, 6)
    ]
    
    print("\n--- FCFS ---")
    scheduler_fcfs = CPUScheduler(processes)
    scheduler_fcfs.fcfs()
    scheduler_fcfs.print_results("FCFS")
    
    print("\n--- SJF ---")
    scheduler_sjf = CPUScheduler(processes)
    scheduler_sjf.sjf()
    scheduler_sjf.print_results("SJF")
    
    # Test Case 2: Semua proses datang bersamaan
    print("\n" + "="*80)
    print("TEST CASE 2: Semua Proses Arrival Time = 0")
    print("="*80)
    
    processes2 = [
        Process('P1', 0, 10),
        Process('P2', 0, 5),
        Process('P3', 0, 8)
    ]
    
    print("\n--- FCFS ---")
    scheduler2_fcfs = CPUScheduler(processes2)
    scheduler2_fcfs.fcfs()
    scheduler2_fcfs.print_results("FCFS")
    
    print("\n--- SJF ---")
    scheduler2_sjf = CPUScheduler(processes2)
    scheduler2_sjf.sjf()
    scheduler2_sjf.print_results("SJF")
    
    # Test Case 3: Gap antar arrival time
    print("\n" + "="*80)
    print("TEST CASE 3: Ada Gap Waktu Antar Proses")
    print("="*80)
    
    processes3 = [
        Process('P1', 0, 7),
        Process('P2', 2, 4),
        Process('P3', 4, 1),
        Process('P4', 5, 4)
    ]
    
    print("\n--- FCFS ---")
    scheduler3_fcfs = CPUScheduler(processes3)
    scheduler3_fcfs.fcfs()
    scheduler3_fcfs.print_results("FCFS")
    
    print("\n--- SJF ---")
    scheduler3_sjf = CPUScheduler(processes3)
    scheduler3_sjf.sjf()
    scheduler3_sjf.print_results("SJF")
    
    # Comparison Summary
    print("\n" + "="*80)
    print(" PERBANDINGAN HASIL ".center(80, "="))
    print("="*80)
    
    print("\nTest Case 1:")
    metrics_fcfs_1 = scheduler_fcfs.calculate_metrics()
    metrics_sjf_1 = scheduler_sjf.calculate_metrics()
    print(f"  FCFS - Avg WT: {metrics_fcfs_1['avg_waiting_time']}, Avg TAT: {metrics_fcfs_1['avg_turnaround_time']}")
    print(f"  SJF  - Avg WT: {metrics_sjf_1['avg_waiting_time']}, Avg TAT: {metrics_sjf_1['avg_turnaround_time']}")
    
    print("\nTest Case 2:")
    metrics_fcfs_2 = scheduler2_fcfs.calculate_metrics()
    metrics_sjf_2 = scheduler2_sjf.calculate_metrics()
    print(f"  FCFS - Avg WT: {metrics_fcfs_2['avg_waiting_time']}, Avg TAT: {metrics_fcfs_2['avg_turnaround_time']}")
    print(f"  SJF  - Avg WT: {metrics_sjf_2['avg_waiting_time']}, Avg TAT: {metrics_sjf_2['avg_turnaround_time']}")
    
    print("\nTest Case 3:")
    metrics_fcfs_3 = scheduler3_fcfs.calculate_metrics()
    metrics_sjf_3 = scheduler3_sjf.calculate_metrics()
    print(f"  FCFS - Avg WT: {metrics_fcfs_3['avg_waiting_time']}, Avg TAT: {metrics_fcfs_3['avg_turnaround_time']}")
    print(f"  SJF  - Avg WT: {metrics_sjf_3['avg_waiting_time']}, Avg TAT: {metrics_sjf_3['avg_turnaround_time']}")
    
    print("\n" + "="*80)
    print("TESTING SELESAI!")
    print("="*80 + "\n")

if __name__ == "__main__":
    run_all_tests()