import requests


def check_site_pudim():
    url = 'http://www.pudim.com.br/'
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except Exception as erro:
        return False


if not check_site_pudim():
    print('\033[31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[33mConsegui acessar o site Pudim com sucesso!\033[m')


