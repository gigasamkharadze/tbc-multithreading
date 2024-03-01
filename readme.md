# Multithreaded JSON Fetcher

This Python script fetches JSON data from a specified URL using multiple threads, then stores the collected data into a JSON file.

## Description

This project demonstrates a multithreaded approach to fetching JSON data from an API. It utilizes the `requests` library to make HTTP requests and `json` module to handle JSON data. The script spawns multiple threads, each responsible for fetching JSON data for a specific object ID. After fetching, the data is stored in a list and then written to a JSON file.

## Requirements

- Python 3.x
- Install the required dependencies using the provided requirements.txt file:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone or download the project repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the script using the following command:
```bash
python main.py
```
or
```bash
python3 main.py
```

# Contributions

We welcome contributions to improve this project! Feel free to fork the repository and submit pull requests with your changes. Please ensure that any contributions align with the project's goals and adhere to the coding standards. For major changes, please open an issue first to discuss the proposed changes.
