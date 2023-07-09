from eth_account import Account
import json


def encrypt(password):
    print('Start encrypting keys...')
    encrypted_keys = []

    with open('keys.txt', 'r') as file:
        keys = [row.strip() for row in file]

    for key in keys:
        encrypted = Account.encrypt(key, password, kdf=None, iterations=None)
        encrypted_keys.append(encrypted)

    with open('ids.txt', 'w') as file:
        for encrypted_key in encrypted_keys:
            identifier = encrypted_key['id']
            file.write(identifier + '\n')

    with open("vault.json", "w") as file:
        data = {'vault': encrypted_keys}
        json_data = json.dumps(data)
        file.write(json_data)

    print('All keys have been encrypted and stored in result.json, identifiers are in ids.txt')


def decrypt(password):
    with open('keys.txt', 'r') as file:
        identifiers = [row.strip() for row in file]

    with open('vault.json', 'r') as file:
        json_object = json.load(file)

    keys = []
    for identifier in identifiers:
        wallets = json_object['vault']
        for wallet in wallets:
            if wallet['id'] == identifier:
                key = Account.decrypt(wallet, password).hex()
                keys.append(key)

    return keys


if __name__ == '__main__':
    password_input = int(input('Password: '))
    encrypt(password_input)
