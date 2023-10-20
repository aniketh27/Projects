import requests
import sys
import time
from datetime import datetime

# Replace 'YOUR_API_KEY' with your actual VirusTotal API key
API_KEY = '839bd064c53789ce05d5a5515ca2ecf681fbd290aaedc102aaccda8fa546bdfb'

def check_hash_reputation(file_hash):
    url = f'https://www.virustotal.com/api/v3/files/{file_hash}'
    headers = {'x-apikey': API_KEY}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            if 'data' in data:
                attributes = data['data']['attributes']
                print(f'File Hash: {file_hash}')
                print(f'Reputation: {attributes["last_analysis_stats"]["malicious"]} malicious / {attributes["last_analysis_stats"]["undetected"]} undetected')
                last_analysis_date = datetime.utcfromtimestamp(attributes["last_analysis_date"]).strftime('%y-%m-%d %H:%M')
                print(f'Last Analysis Date: {last_analysis_date}')
            else:
                print(f'No data available for file hash: {file_hash}')
        else:
            print(f'Error for file hash {file_hash}:', response.status_code)
    except requests.exceptions.RequestException as e:
        print(f'Request error for file hash {file_hash}:', e)

def check_hash_reputation_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            hashes = file.readlines()

        for hashitem in hashes:
            hashitem = hashitem.strip() 
            try:
                check_hash_reputation(hashitem)
                print("-"*10)
                print()
                time.sleep(15)
            except Exception as e:
                print(f"This information is not available for {hashitem}: {e}")
                print("-"*10)
                print()
                time.sleep(15)
                continue

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading hashes from file: {e}")


HASHES_TO_CHECK = sys.argv[1]
check_hash_reputation_from_file(HASHES_TO_CHECK)
