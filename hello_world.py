import time
import os


while True:
    print("Hello my fantastic world!!")
    print(f"Your secret is '{os.getenv('EXAMPLE_SECRET')}'.", flush=True)
    time.sleep(10)
