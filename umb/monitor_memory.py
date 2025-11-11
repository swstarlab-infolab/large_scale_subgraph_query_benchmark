import psutil
import time
import sys

def monitor_system_memory(log_file="system_memory_usage.log", interval=0.5):
    """
    Monitors the system-wide memory usage and logs it to a file.
    """
    try:
        with open(log_file, "w") as f:
            f.write("Time(s)\tTotal(MB)\tUsed(MB)\tAvailable(MB)\tPercentage(%)\n")
            start_time = time.time()

            while True:
                mem_info = psutil.virtual_memory()
                elapsed_time = time.time() - start_time

                # Convert bytes to MB
                total_mb = mem_info.total / (1024 ** 2)
                used_mb = mem_info.used / (1024 ** 2)
                available_mb = mem_info.available / (1024 ** 2)
                percentage = mem_info.percent

                f.write(f"{elapsed_time:.2f}\t{total_mb:.2f}\t{used_mb:.2f}\t{available_mb:.2f}\t{percentage:.2f}\n")
                f.flush()
                time.sleep(interval)
    except KeyboardInterrupt:
        print("Memory monitoring stopped.")

if __name__ == "__main__":
    q_id = int(sys.argv[1])
    log_file = f"umbra_{q_id}.log"
    monitor_system_memory(log_file)