import requests

mentors = requests.get("https://hackbulgaria.com/hackfmi/api/mentors/").json()
public_teams = requests.\
    get("https://hackbulgaria.com/hackfmi/api/public-teams/").json()
skills = requests.get("https://hackbulgaria.com/hackfmi/api/skills/").json()
