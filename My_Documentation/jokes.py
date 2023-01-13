import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKES FUNMIOFLIFE!")
header= colored(header, color='red')
print(header)

user_input = input("what would you like to saerch for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
        url, 
        headers = {"Accept": "application/json"},
        params={"term":user_input}
).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}.  Here's one:")
    print(choice(results) ["jokes"])
elif num_jokes == 1:
    print(f"I found {num_jokes} jokes about {user_input}")
    print(results [0] ['joke'])
else:
    print(f"Sorry,could't find a joke with your term: {user_input}")

