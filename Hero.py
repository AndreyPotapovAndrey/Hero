from pprint import pprint

import requests

TOKEN = " "


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://akabab.github.io/superhero-api/api/all.json'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        # headers = self.get_headers()
        response = requests.get(files_url, headers=headers)


        heroes = []
        for hero in response.json():
            # print(hero)
            if hero['name'] in ['Hulk', 'Captain America', 'Thanos']:
                heroes.append(
                    {'id': hero['id'], 'name': hero['name'], 'intelligence': hero['powerstats']['intelligence']})
                # print(heroes)
        max_intelligence = max(heroes, key=lambda x: x['intelligence'])['name']
        print(f'Самый умный среди супергероев - {max_intelligence}')



if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
ya.get_files_list()
