import json
import requests
import time
import threading

URL = 'https://dummyjson.com/products/'
DATA = []


def get_json(url, object_id):
    print(f"Getting data for object {object_id} with thread {threading.current_thread().name}")
    complete_url = url + str(object_id)
    response = requests.get(complete_url)
    DATA.append(response.json())
    print(f"Data for object {object_id} has been added to the list, thread {threading.current_thread().name} is done.")


if __name__ == '__main__':
    start_time = time.perf_counter()
    threads = []
    for i in range(1, 101):
        thread = threading.Thread(target=get_json, args=(URL, i))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    with open('data.json', 'w') as file:
        json.dump(DATA, file, indent=4)
    end_time = time.perf_counter()
    print(f"Time taken: {end_time - start_time} seconds")
