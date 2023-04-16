import requests

class Show_Joke:

    # URLs for getting a ramdon joke
    CHUCK_URL='https://api.chucknorris.io/jokes/random'
    DAD_URL='https://icanhazdadjoke.com/'

    def chuck(self):
        response = requests.get(self.CHUCK_URL).json()
        return response['value']

    def dad(self):
        headers={'Accept':'application/json'}
        response = requests.get(self.DAD_URL,headers=headers).json()
        return response['joke']
    