import psutil

def get_top_processes(limit=5, sort_by="cpu"):
    processes = []

    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            processes.append(proc.info)
        except psutil.NoSuchProcess:
            continue

    key = "cpu_percent" if sort_by == "cpu" else "memory_percent"
    processes.sort(key=lambda p: p[key], reverse=True)

    return processes[:limit]
