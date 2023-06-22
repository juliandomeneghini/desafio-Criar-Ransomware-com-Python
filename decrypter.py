import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


def decrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        iv = file.read(16)  # Leitura do vetor de inicialização (IV)
        ciphertext = file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)


if __name__ == '__main__':
    decryption_key = get_random_bytes(16)  # Chave de descriptografia de 16 bytes (128 bits)
    directory = '/home/kali/projeto-ransonware/'  # Diretório que contém os arquivos criptografados

    for filename in os.listdir(directory):
        if filename.endswith('_criptografado.txt'):
            input_file = os.path.join(directory, filename)
            decrypted_file = os.path.join(directory, filename.replace('_criptografado.txt', '_descriptografado.txt'))

            decrypt_file(decryption_key, input_file, decrypted_file)
            print("Arquivo descriptografado gerado:", decrypted_file)
