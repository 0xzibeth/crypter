from loguru import logger
from eth_account import Account
import json


password = 'Your password'


def encrypt():
    encrypted_keys = []

    with open('keys.txt', 'r') as f:
        keys = [row.strip() for row in f]

    for key in keys:
        encrypted = Account.encrypt(key, password, kdf=None, iterations=None)
        encrypted_keys.append(encrypted)
        id = encrypted['id']
        logger.success(f'Encrypted: {key} -> {id}')

    with open('ids.txt', 'w') as f:
        for encrypted_key in encrypted_keys:
            id = encrypted_key['id']
            f.write(id + '\n')

    with open("result.json", "w") as outfile:
        data = {}
        data['wallets'] = encrypted_keys
        json_data = json.dumps(data)
        outfile.write(json_data)

    logger.success(f'All keys have been encrypted and stored in result.json, ids are in ids.txt')


def decrypt():
    with open('ids.txt', 'r') as file:
        ids = [row.strip() for row in file]

    with open('result.json', 'r') as file:
        json_object = json.load(file)

    for id in ids:
        wallets = json_object['wallets']
        for wallet in wallets:
            if wallet['id'] == id:
                decrypted = Account.decrypt(wallet, password).hex()
                logger.success(f'Decrypted: {id} -> {decrypted}')


if __name__ == '__main__':
    encrypt()
