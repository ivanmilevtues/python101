import requests

mentors = requests.get("https://hackbulgaria.com/hackfmi/api/mentors/")
public_teams = requests.\
    get("https://hackbulgaria.com/hackfmi/api/public-teams/")
skills = requests.get("https://hackbulgaria.com/hackfmi/api/skills/")
