import requests
import json

try:
    response = requests.get('https://remoteok.com/api')
    response.raise_for_status()  # Raises an exception for bad status codes
    jobs = response.json()
    
    with open('data/raw_jobs.json', 'w') as f:
        json.dump(jobs[1:], f, indent=4)  # More efficient than dumps + write
        print("Raw Jobs Fetched Successfully")
        
except requests.RequestException as e:
    print(f"Error fetching data: {e}")
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")
except IOError as e:
    print(f"Error writing file: {e}")