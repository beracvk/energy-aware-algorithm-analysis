import time
import psutil
from codecarbon import EmissionsTracker

def measure(func, label, *args):
    process = psutil.Process()

    tracker = EmissionsTracker(
        project_name=label,
        log_level="error"
    )
    tracker.start()

    start_time = time.perf_counter()
    start_cpu = process.cpu_times()

    result = func(*args)

    end_time = time.perf_counter()
    end_cpu = process.cpu_times()

    energy_kwh = tracker.stop()

    elapsed_time = end_time - start_time
    cpu_time = (end_cpu.user + end_cpu.system) - (start_cpu.user + start_cpu.system)

    return elapsed_time, cpu_time, energy_kwh, result
