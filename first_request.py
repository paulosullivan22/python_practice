from requests import get
from random import choice

url = 'https://icanhazdadjoke.com/search'
userRequest = input('Let me tell you a joke. Give me a topic: ')

def generateJoke(userRequest):
    response = get(
        url,
        headers={"Accept": "application/json"},
        params={"term": userRequest}
    )

    data = response.json()['results']
    length = len(data)

    if length > 1:
        print(f'I\'ve got {length} jokes about {userRequest}. Here\'s one:')
        print(choice(data)['joke'])
    elif length == 1:
        print(f'I\'ve got one joke about {userRequest}. Here it is:')
        print(data[0]['joke'])
    else:
        print(f'Sorry I don\'t have any jokes about {userRequest}. Please try again.')

generateJoke(userRequest)
