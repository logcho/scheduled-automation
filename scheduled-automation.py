import time
import subprocess

def run_hello_every_minute():
    while True:
        subprocess.run(["python3", "hello-world.py"])  # or "python3" if needed
        time.sleep(60)

if __name__ == "__main__":
    run_hello_every_minute()
