
from pprint import pprint

import requests



class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        #headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        url_to_load = data.get('href')
        return url_to_load

    def upload_file_to_disk(self, disk_file_path: str, filename: str):
        url_to_load = self._get_upload_link(disk_file_path=disk_file_path)
        response = requests.put(url_to_load, data=open(filename, 'rb'))
        # response.raise_for_status()
        if response.status_code == 201:
            print("Success")



if __name__=='__main__':
    TOKEN = " "
    uploader = YaUploader(token=TOKEN)
    uploader.upload_file_to_disk('netology/text22.03.txt', '123.txt')

    # for item in data['items']:
    #     print(item['mime_type'])
