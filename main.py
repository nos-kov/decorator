from decorator_param import logger

import requests

@logger('main.log')
def try_call():
        
    request = requests.get("http://www.yandex.ru/")
    response = request.json
    text = str(response)
    if 'Response' in text:
        cut = text.find("[")
        return 'Status is: ' + text[cut+1:cut+4]


if __name__ == '__main__':

    try_call()