import requests

response = requests.get(
    "https://api.github.com/search/repositories?q=language:python+stars:%3E1&sort=stars&order=desc")
response.raise_for_status()

data = response.json()["items"]

for repo in data:
    owner_url = repo["owner"]["html_url"]
    print(owner_url)
