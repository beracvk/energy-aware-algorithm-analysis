import time
import psutil

def measure(func, *args):
    process = psutil.Process()

    start_time = time.time()
    start_cpu = process.cpu_times()

    result = func(*args)

    end_time = time.time()
    end_cpu = process.cpu_times()

    elapsed_time = end_time - start_time
    cpu_time = (end_cpu.user + end_cpu.system) - (start_cpu.user + start_cpu.system)

    return elapsed_time, cpu_time, result
