import schedule
import time

def task():
    print("Task running!")

schedule.every().day.at("10:00").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)import schedule
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task():
    try:
        print("Task running!")
        # Add task logic here
    except Exception as e:
        logging.error(f"Task failed: {e}")

# Schedule task to run daily at 10:00
schedule.every().day.at("10:00").do(task)

def main():
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            logging.info("Scheduler stopped by user")
            break
        except Exception as e:
            logging.error(f"Scheduler error: {e}")

if __name__ == "__main__":
    main()