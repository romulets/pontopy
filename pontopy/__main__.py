import sys
import requests
import json
import uuid
import os
from configparser import ConfigParser

TOKEN = None
CLIENT_ID = None
UID = None
PATH = None

def main():
    if len(sys.argv) < 3:
        credenciais = carregar_credenciais()
        login = credenciais['login']
        password = credenciais['password']
    else:
        login = sys.argv[1]
        password = sys.argv[2]
    bater_ponto(login, password)
    salvar_credenciais(login, password)


def salvar_credenciais(login, password):
    config = ConfigParser()
    config['DEFAULT'] = {
        'login': login,
        'password': password
    }
    with open(os.path.dirname(sys.argv[0]) + '/../credenciais.ini', 'w') as configfile:
        config.write(configfile)


def carregar_credenciais():
    login = None
    password = None
    try:
        with open(os.path.dirname(sys.argv[0]) + '/../credenciais.ini') as configile:
            config = ConfigParser()
            config.read_file(configile)
            login = config['DEFAULT']['login']
            password = config['DEFAULT']['password']
    except IOError:
        login = input('Login: ')
        password = input('Senha: ')
    finally:
        return {
            'login': login,
            'password': password
        }


def bater_ponto(login, passoword):
    global UID
    UID = login
    realizar_login(login, passoword)
    registrar_ponto()


def realizar_login(login, password):
    response = requests.post('https://api.pontomaisweb.com.br/api/auth/sign_in', {
        'login': login,
        'password': password
    })
    if response.status_code != 201:
        print('Não foi possível realizar o login.')
        sys.exit(1)
    data = json.loads(response.text)
    global TOKEN, CLIENT_ID
    TOKEN = data['token']
    CLIENT_ID = data['client_id']


def registrar_ponto():
    payload = {
        'time_card': {
            'latitude': -25.4337302,
            'longitude': -49.2808763,
            'address': 'Alameda Dr. Carlos de Carvalho, 625 - Centro, Curitiba - PR, Brasil',
            'reference_id': None,
            'original_latitude': -25.4337302,
            'original_longitude': -49.2808763,
            'original_address': 'Alameda Dr. Carlos de Carvalho, 625 - Centro, Curitiba - PR, Brasil',
            'location_edited': False,
            'accuracy': 50
        },
        'path': '/meu_ponto/registro_de_ponto',
        '_device': {
            'manufacturer': None,
            'model': None,
            'uuid': None,
            'version': None
        },
        '_appVersion': '0.10.26'
    }
    headers = {
        'token-type': 'Bearer',
        'uid': UID,
        'uuid': str(uuid.uuid4()),
        'access-token': TOKEN,
        'Api-Version': '2',
        'client': CLIENT_ID
    }
    response = requests.post('https://api.pontomaisweb.com.br/api/time_cards/register', json.dumps(payload),
                             headers=headers)
    if response.status_code != 200:
        print('Não foi possível registrar o ponto')
        sys.exit(2)
    print('Ponto registrado com sucesso!')


if __name__ == '__main__':
    main()
