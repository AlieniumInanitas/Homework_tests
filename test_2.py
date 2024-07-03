import requests
import unittest

def load_token():
    f = open('token.txt')
    token = f.read()
    f.close()
    return token

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {load_token()}'}

def create_folder(path):
    return requests.put(f'{URL}?path={path}', headers=headers)

def get_file(path):
    return requests.get(f'{URL}?path={path}', headers=headers)


class TestYandexDiskAPI(unittest.TestCase):
    def test_create_folder(self):
        self.assertEqual(create_folder("test").status_code, 201)
        self.assertEqual(create_folder("test").status_code, 409)
        self.assertEqual(get_file("test").status_code, 200)
    

if __name__ == '__main__':
    unittest.main()