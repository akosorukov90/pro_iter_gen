import requests

ADDRESS = 'https://en.wikipedia.org/w/api.php?action=opensearch&search='
PROP = '&prop=info&format=json&inprop=url'


class WikiCountrySearch:
    def __init__(self, data):
        self.countries = data
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.countries):
            self.country = self.countries[self.counter]["name"]["common"]
            url = ADDRESS + self.country + PROP
            self.response = requests.get(url)
            self.country_url = self.response.json()[3][0]
            self.result = str(self.country) + ' - ' + str(self.country_url)
            self.counter += 1
            return self.result
        else:
            raise StopIteration
