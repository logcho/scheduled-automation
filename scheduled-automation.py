import time
import subprocess
from datetime import datetime, timedelta

def scheduled_automation():
    # Get user-defined interval and duration
    try:
        interval = int(input("Enter interval in seconds between runs: "))
        duration = int(input("Enter total run time in minutes: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    stop_time = datetime.now() + timedelta(minutes=duration)
    print(f"Automation will stop at {stop_time.strftime('%H:%M:%S')}")

    try:
        while datetime.now() < stop_time:
            subprocess.run(["python3", "hello-world.py"])
            print(f"Waiting {interval} seconds... (Press Ctrl+C to stop early)")
            time.sleep(interval)

        print("Scheduled end time reached. Exiting.")
    except KeyboardInterrupt:
        print("\nDetected interruption. Do you want to quit? (y/n): ", end="")
        response = input().strip().lower()
        if response == 'y':
            print("Exiting gracefully.")
        else:
            print("Resuming...")
            scheduled_automation()

if __name__ == "__main__":
    scheduled_automation()
