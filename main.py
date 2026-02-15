from monitor.system_info import get_system_usage
from monitor.process_analyzer import get_top_processes

def main():
    print("\n=== SYSTEM MONITOR ===")
    usage = get_system_usage()

    print(f"CPU Usage: {usage['cpu_percent']}%")
    print(f"Memory Usage: {usage['memory_percent']}%")
    print(f"Uptime: {usage['uptime_seconds']:.2f} seconds")

    print("\n=== TOP PROCESSES (CPU) ===")
    for p in get_top_processes(sort_by="cpu"):
        print(f"{p['name']} (PID {p['pid']}): {p['cpu_percent']}% CPU")

    print("\n=== TOP PROCESSES (MEMORY) ===")
    for p in get_top_processes(sort_by="memory"):
        print(f"{p['name']} (PID {p['pid']}): {p['memory_percent']}% MEM")

if __name__ == "__main__":
    main()
