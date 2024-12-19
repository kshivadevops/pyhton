import psutil

def monitor_cpu():
    print(f"CPU usage: {psutil.cpu_percent()}%")
    print(f"Memory usage: {psutil.virtual_memory().percent}%")

monitor_cpu()import logging

logging.basicConfig(level=logging.INFO,logging.info("Monitoring CPU usage...")
logging.info(f"CPU usage: {psutil.cpu_percent()}%")
logging.info(f"Memory usage: {psutil.virtual_memory().percent}%")
def monitor_cpu():
    logging.info("Monitoring CPU usage...")
    cpu_usage = psutil.cpu_percent()
    logging.info(f"CPU usage: {cpu_usage}%")
    logging.info("Monitoring memory usage...")
    memory_usage = psutil.virtual_memory().percent
    logging.info(f"Memory usage: {memory_usage}%")

monitor_cpu()
monitor_cpu()def monitor_system_resources():
    logging.info("Monitoring system resources...")
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    logging.info(f"CPU usage: {cpu_usage}%")
    logging.info(f"Memory usage: {memory_usage}%")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    while True:
        monitor_system_resources()