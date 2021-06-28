import requests

username = input("Write your github username:\n")

response = requests.get(f"https://api.github.com/users/{username}/repos")

projects = response.json()

for project in projects:
    print(f"Project Name: {project['name']}\nProject URL: {project['html_url']}")