import requests
import time
from datetime import datetime
import sys

API_KEY = '839bd064c53789ce05d5a5515ca2ecf681fbd290aaedc102aaccda8fa546bdfb'

def check_ip_reputation(ip_address):
    url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip_address}'
    headers = {'x-apikey': API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        if response.status_code == 200:
            data = response.json()
            if 'data' in data:
                attributes = data['data']['attributes']
#                print(attributes)
                print(f'IP Address: {ip_address}')
                print(f'Reputation: {attributes["last_analysis_stats"]["malicious"]} malicious / {attributes["last_analysis_stats"]["undetected"]} undetected')
                print(f'ISP: {attributes["as_owner"]}')
                last_analysis_date = datetime.utcfromtimestamp(attributes["last_analysis_date"]).strftime('%y-%m-%d %H:%M')
                print(f'Last Analysis Date: {last_analysis_date}')
            else:
                print(f'No data available for IP address: {ip_address}')
        else:
            print(f'Error for IP address {ip_address}:', response.status_code)
    except requests.exceptions.RequestException as e:
        print('Request error:', e)

def check_ip_reputation_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            ips = file.readlines()

        for ip in ips:
            ip = ip.strip() 
            try:
                check_ip_reputation(ip)
                print("-"*10)
                print()
                time.sleep(15)
            except Exception as e:
                print(f"This information is not available for {ip}: {e}")
                print("-"*10)
                print()
                time.sleep(15)
                continue

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading IPs from file: {e}")
      

IPs_TO_CHECK = sys.argv[1]
check_ip_reputation_from_file(IPs_TO_CHECK)
