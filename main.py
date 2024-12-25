import requests


response = requests.get(
    "https://api.github.com/search/repositories?q=language:python+stars:%3E1&sort=stars&order=desc")
response.raise_for_status()

data = response.json()["items"]

with open("open-source.txt", "w", encoding="utf-8") as file:
    file.write("Open source GitHub Repositories with Python language:\n\n")
    for repo in data:
        owner_url = repo["owner"]["html_url"]
        description = repo["description"]
        name = repo["name"]
        file.write(f" \n Name: {name}\n Description: {
                   description}\n Owner url: {owner_url} \n\n")
        file.write(
            "-------------------------------------------------------------------------------------------------------------------\n\n")
