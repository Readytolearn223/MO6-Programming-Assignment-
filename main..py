#15.1 



import multiprocessing
import time
import random 
from datetime import datetime 

def worker():
    wait_time = random.random()
    time.sleep(wait_time)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current time:", current_time)

if __name__ == "__main__": 
    processes = []
    for _ in range(3):
        process = multiprocessing.Process(target=worker)
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

                
