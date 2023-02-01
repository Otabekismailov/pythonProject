'''
1-merchant
2-client

merchant
-product qoshish
    -name
    -price
-product ochirish

client
-product sotib olish
-product izlash

homework
working with files
register (id, first name, username, password, is_client)

login
    -botir
    -01 (bcrypt)

client, merchant - balance(history), check balance
client, merchant - my products

'''
import json
from typing import Optional


def write_file(file_name: str, data):
    with open(f'data/{file_name}', 'w') as file:
        json.dump(data, file, indent=2)


def read_file(file_name: str) -> list:
    with open(f'data/{file_name}') as file:
        users = json.load(file)
    return users


def user_exists(username: str) -> bool:
    users: list = read_file('users.json')
    for user in users:
        if user['username'] == username:
            return True
    return False


def find_user(username):
    users: list = read_file('users.json')
    for user in users:
        if user['username'] == username:
            return user
    return None


def login(username, password) -> tuple:
    if user_exists(username):
        user = find_user(username)
        if user and user['password'] == password:
            return user, True
    return None, False


def register(first_name: str, username: str, password: str, is_client: bool):
    users: list = read_file('users.json')
    users.append({
        'id': len(users) + 1,
        'first_name': first_name,
        'username': username,
        'balance': 15000,
        'is_client': is_client,
        'password': password,
    })
    write_file('users.json', users)


def main():
    current_user: Optional[dict] = None

    while True:
        menu = '''
1. login
2. register
'''

        merchant_menu = '''
1. Add product
2. Remove product
3. Check my balance
4. My product
5. History
'''

        client_menu = '''
1. Purchase product
2. Search product
3. Check my balance
4. My bought product
'''
        if current_user:
            if current_user['is_client']:
                welcome = 'Haridor'
                menu = client_menu
            else:
                menu = merchant_menu
                welcome = 'Sotuvchi'
            menu = '0. Logout' + menu
            print(f'Xush kelibsiz {welcome}!')
        key = input(menu)
        match key:
            case '0':
                current_user = None
            case '1':
                username = input('username kiriting: ')
                password = input('parolni kiriting: ')
                user, is_logged = login(username, password)
                if is_logged:
                    current_user = user
                else:
                    print('Parol yoki username xato ! ')
            case '2':
                first_name = input('Ismingizni kiriting: ')
                is_client = input('Haridormisiz ? (yes/no y/n): ')
                username = input('Username kiriting: ')
                password = input('Parolni kiriting: ')
                if user_exists(username):
                    print('Bunday username bor')
                else:
                    register(first_name, username, password, is_client.startswith('y'))
                    print('Register successfully !')

if __name__ == '__main__':
    main()
