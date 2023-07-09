# Crypter
This script encrypt and decrypt keys. Feel free to use it in your scripts and automation.
The idea is to encrypt keys and keep ids of encrypted object, encrypted objects JSON and password separately. For example, you can operate with ids in any sheet or text file. However, encrypted JSON object should be on a USB flash drive and password should be ideally memorised. Once you need to decrypt some keys you can insert USB flash drive into your machine and decrypt keys on the go with like `decrypt()` function providing it your password.

# Usage
1. Install `eth_account` and `json` in any environment you prefer.
2. Put your keys in `keys.txt`.
3. Run the sript with `encrypt()` mode.
4. Clean `keys.txt`.
5. Store `vault.json` on a USB flash drive. You might want to update the path to the file in `dectypt()` fucntion.
6. Use identifiers from `ids.txt` anywhere you like with no fear of a hack.
