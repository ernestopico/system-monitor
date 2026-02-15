import psutil
import time

def get_system_usage():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "uptime_seconds": time.time() - psutil.boot_time()
    }
