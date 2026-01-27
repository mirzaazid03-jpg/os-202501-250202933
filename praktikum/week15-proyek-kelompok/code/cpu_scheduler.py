#!/usr/bin/env python3
"""
CPU Scheduling Simulator - FCFS & SJF
Modul A untuk Proyek Sistem Operasi
"""

import csv
import json
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Process:
    """Representasi proses CPU"""
    pid: str
    arrival_time: int
    burst_time: int
    waiting_time: int = 0
    turnaround_time: int = 0
    completion_time: int = 0
    start_time: int = 0

class CPUScheduler:
    """Simulator CPU Scheduling untuk FCFS dan SJF"""
    
    def __init__(self, processes: List[Process]):
        self.processes = processes
        self.results = []
    
    def fcfs(self) -> List[Process]:
        """First Come First Serve scheduling"""
        # Sort by arrival time
        sorted_processes = sorted(self.processes, key=lambda x: x.arrival_time)
        current_time = 0
        results = []
        
        for proc in sorted_processes:
            # Start time is max of current time or arrival time
            start_time = max(current_time, proc.arrival_time)
            waiting_time = start_time - proc.arrival_time
            completion_time = start_time + proc.burst_time
            turnaround_time = completion_time - proc.arrival_time
            
            result = Process(
                pid=proc.pid,
                arrival_time=proc.arrival_time,
                burst_time=proc.burst_time,
                waiting_time=waiting_time,
                turnaround_time=turnaround_time,
                completion_time=completion_time,
                start_time=start_time
            )
            results.append(result)
            current_time = completion_time
        
        self.results = results
        return results
    
    def sjf(self) -> List[Process]:
        """Shortest Job First scheduling (non-preemptive)"""
        processes = [Process(p.pid, p.arrival_time, p.burst_time) 
                    for p in self.processes]
        current_time = 0
        results = []
        completed = 0
        n = len(processes)
        is_completed = [False] * n
        
        while completed < n:
            # Find processes that have arrived
            available = []
            for i, proc in enumerate(processes):
                if not is_completed[i] and proc.arrival_time <= current_time:
                    available.append((i, proc))
            
            if not available:
                # No process available, jump to next arrival
                next_arrival = min(proc.arrival_time for i, proc in enumerate(processes) 
                                 if not is_completed[i])
                current_time = next_arrival
                continue
            
            # Select shortest job
            idx, shortest = min(available, key=lambda x: x[1].burst_time)
            
            start_time = current_time
            waiting_time = start_time - shortest.arrival_time
            completion_time = start_time + shortest.burst_time
            turnaround_time = completion_time - shortest.arrival_time
            
            result = Process(
                pid=shortest.pid,
                arrival_time=shortest.arrival_time,
                burst_time=shortest.burst_time,
                waiting_time=waiting_time,
                turnaround_time=turnaround_time,
                completion_time=completion_time,
                start_time=start_time
            )
            results.append(result)
            
            current_time = completion_time
            is_completed[idx] = True
            completed += 1
        
        self.results = results
        return results
    
    def calculate_metrics(self) -> Dict[str, float]:
        """Hitung metrik rata-rata"""
        if not self.results:
            return {}
        
        avg_waiting = sum(p.waiting_time for p in self.results) / len(self.results)
        avg_turnaround = sum(p.turnaround_time for p in self.results) / len(self.results)
        
        return {
            'avg_waiting_time': round(avg_waiting, 2),
            'avg_turnaround_time': round(avg_turnaround, 2),
            'total_processes': len(self.results)
        }
    
    def print_results(self, algorithm: str):
        """Cetak hasil scheduling ke terminal"""
        print(f"\n{'='*80}")
        print(f"HASIL SCHEDULING - {algorithm}")
        print(f"{'='*80}")
        
        # Header
        print(f"{'PID':<8} {'Arrival':<10} {'Burst':<8} {'Start':<8} {'Completion':<12} {'Waiting':<10} {'Turnaround':<12}")
        print(f"{'-'*80}")
        
        # Data
        for proc in sorted(self.results, key=lambda x: x.pid):
            print(f"{proc.pid:<8} {proc.arrival_time:<10} {proc.burst_time:<8} "
                  f"{proc.start_time:<8} {proc.completion_time:<12} "
                  f"{proc.waiting_time:<10} {proc.turnaround_time:<12}")
        
        # Metrics
        metrics = self.calculate_metrics()
        print(f"\n{'-'*80}")
        print(f"METRIK PERFORMA:")
        print(f"  Average Waiting Time     : {metrics['avg_waiting_time']} ms")
        print(f"  Average Turnaround Time  : {metrics['avg_turnaround_time']} ms")
        print(f"  Total Processes          : {metrics['total_processes']}")
        print(f"{'='*80}\n")
        
        # Gantt Chart
        self.print_gantt_chart()
    
    def print_gantt_chart(self):
        """Cetak Gantt Chart sederhana"""
        print("GANTT CHART:")
        sorted_results = sorted(self.results, key=lambda x: x.start_time)
        
        # Timeline
        chart = "|"
        timeline = "|"
        
        for proc in sorted_results:
            width = proc.burst_time * 2
            chart += f" {proc.pid:^{width}} |"
            timeline += f"{proc.start_time:^{width+2}}|"
        
        print(chart)
        print(timeline[:-1] + f"{sorted_results[-1].completion_time}")
        print()
    
    def export_csv(self, filename: str):
        """Export hasil ke CSV"""
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['PID', 'Arrival Time', 'Burst Time', 'Start Time', 
                           'Completion Time', 'Waiting Time', 'Turnaround Time'])
            
            for proc in sorted(self.results, key=lambda x: x.pid):
                writer.writerow([proc.pid, proc.arrival_time, proc.burst_time,
                               proc.start_time, proc.completion_time,
                               proc.waiting_time, proc.turnaround_time])
        
        print(f"✓ Hasil disimpan ke: {filename}")

def load_from_csv(filename: str) -> List[Process]:
    """Load proses dari file CSV"""
    processes = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            proc = Process(
                pid=row['pid'],
                arrival_time=int(row['arrival_time']),
                burst_time=int(row['burst_time'])
            )
            processes.append(proc)
    return processes

def create_sample_data(filename: str = 'data/sample_processes.csv'):
    """Buat sample data untuk testing"""
    import os
    os.makedirs('data', exist_ok=True)
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['pid', 'arrival_time', 'burst_time'])
        writer.writerow(['P1', 0, 5])
        writer.writerow(['P2', 1, 3])
        writer.writerow(['P3', 2, 8])
        writer.writerow(['P4', 3, 6])
    
    print(f"✓ Sample data dibuat: {filename}")

def main():
    """Main program"""
    print("\n" + "="*80)
    print(" CPU SCHEDULING SIMULATOR - FCFS & SJF ".center(80, "="))
    print("="*80 + "\n")
    
    # Menu
    print("MENU:")
    print("1. Load dari CSV file")
    print("2. Input manual")
    print("3. Gunakan sample data")
    print("0. Exit")
    
    choice = input("\nPilih menu (0-3): ").strip()
    
    if choice == '0':
        print("Terima kasih!")
        return
    
    processes = []
    
    if choice == '1':
        filename = input("Masukkan nama file CSV: ").strip()
        try:
            processes = load_from_csv(filename)
            print(f"✓ Loaded {len(processes)} processes dari {filename}")
        except Exception as e:
            print(f"✗ Error: {e}")
            return
    
    elif choice == '2':
        n = int(input("Jumlah proses: "))
        for i in range(n):
            print(f"\nProses {i+1}:")
            pid = input("  PID: ").strip() or f"P{i+1}"
            arrival = int(input("  Arrival Time: "))
            burst = int(input("  Burst Time: "))
            processes.append(Process(pid, arrival, burst))
    
    elif choice == '3':
        create_sample_data()
        processes = load_from_csv('data/sample_processes.csv')
        print(f"✓ Loaded {len(processes)} sample processes")
    
    else:
        print("Pilihan tidak valid!")
        return
    
    if not processes:
        print("Tidak ada proses untuk dijadwalkan!")
        return
    
    # Pilih algoritma
    print("\nALGORITMA:")
    print("1. FCFS (First Come First Serve)")
    print("2. SJF (Shortest Job First)")
    print("3. Keduanya")
    
    algo_choice = input("\nPilih algoritma (1-3): ").strip()
    
    if algo_choice in ['1', '3']:
        scheduler = CPUScheduler(processes)
        scheduler.fcfs()
        scheduler.print_results("FCFS")
        
        export = input("Export hasil ke CSV? (y/n): ").lower()
        if export == 'y':
            scheduler.export_csv('results_fcfs.csv')
    
    if algo_choice in ['2', '3']:
        scheduler = CPUScheduler(processes)
        scheduler.sjf()
        scheduler.print_results("SJF")
        
        export = input("Export hasil ke CSV? (y/n): ").lower()
        if export == 'y':
            scheduler.export_csv('results_sjf.csv')

if __name__ == "__main__":
    main()