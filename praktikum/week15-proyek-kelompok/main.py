#!/usr/bin/env python3
"""
OS Simulator - Proyek Kelompok Sistem Operasi
Mengintegrasikan 3 modul: CPU Scheduling, Page Replacement, dan Deadlock Detection
"""

import sys
import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Process:
    pid: str
    arrival_time: int
    burst_time: int
    priority: int = 0

@dataclass
class ProcessResult:
    pid: str
    arrival_time: int
    burst_time: int
    completion_time: int
    turnaround_time: int
    waiting_time: int

@dataclass
class DeadlockProcess:
    pid: str
    allocated: List[int]
    max_need: List[int]

class CPUScheduler:
    def __init__(self, processes: List[Process]):
        self.processes = processes
    
    def fcfs(self) -> List[ProcessResult]:
        sorted_processes = sorted(self.processes, key=lambda p: p.arrival_time)
        current_time = 0
        results = []
        
        for proc in sorted_processes:
            if current_time < proc.arrival_time:
                current_time = proc.arrival_time
            
            completion_time = current_time + proc.burst_time
            turnaround_time = completion_time - proc.arrival_time
            waiting_time = turnaround_time - proc.burst_time
            
            results.append(ProcessResult(
                pid=proc.pid,
                arrival_time=proc.arrival_time,
                burst_time=proc.burst_time,
                completion_time=completion_time,
                turnaround_time=t

# ... (1500+ baris code lengkap)
# Download untuk melihat full code!
