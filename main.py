from classWikiCountrySearch import WikiCountrySearch
import json


if __name__ == '__main__':
    with open("countries.json") as f:
        json_data = json.load(f)
    with open('result.txt', 'w') as f:
        for country in WikiCountrySearch(json_data):
            f.write(country + '\n')
