import requests
import logging

logging.basicConfig(filename='open-source.txt',
                    level=logging.INFO, format='%(asctime)s - %(message)s')

response = requests.get(
    "https://api.github.com/search/repositories?q=language:python+stars:%3E1&sort=stars&order=desc")
response.raise_for_status()

data = response.json()["items"]

logging.info("GitHub Repositories with Python language:")

for repo in data:
    owner_url = repo["owner"]["html_url"]
    logging.info(f"Open-source Projects repository URL: {owner_url}")
logging.info("Logging completed.")
