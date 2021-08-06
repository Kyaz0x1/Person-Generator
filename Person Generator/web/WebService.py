import requests
import json

from types import SimpleNamespace

class WebService:

    def gen_person(data: dict):
        response = requests.post('https://www.4devs.com.br/ferramentas_online.php', data = data)
        person = json.loads(response.content, object_hook = lambda d: SimpleNamespace(**d))
        return person