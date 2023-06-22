# Desafio Dio -  Criando um Ransomware com Python

# Criptografador e Descriptografador de Arquivos TXT
Este é um projeto que consiste em um criptografador e descriptografador de arquivos TXT. O objetivo é permitir a criptografia de arquivos de texto dentro de um diretório específico, bem como a sua posterior descriptografia.

# Funcionalidades:

* Criptografador de Arquivos TXT: O programa irá percorrer um diretório definido pelo usuário e buscará todos os arquivos com extensão ".txt". Em seguida, aplicará um algoritmo de criptografia nos arquivos encontrados, tornando o conteúdo ilegível. Os arquivos originais não serão afetados e permanecerão no diretório.

* Descriptografador de Arquivos TXT: Este recurso permite a restauração dos arquivos criptografados para o seu estado original. O programa buscará no diretório definido os arquivos criptografados e aplicará um algoritmo de descriptografia, recuperando o conteúdo legível dos arquivos TXT.

## Como usar
* Defina o diretório: Informe o diretório no qual os arquivos TXT estão localizados. Certifique-se de especificar o caminho completo do diretório, por exemplo: C:\caminho\para\diretorio.

* Criptografar arquivos: Execute a função de criptografia para que o programa percorra o diretório definido e criptografe todos os arquivos TXT encontrados. Os arquivos originais não serão alterados ou removidos.

* Descriptografar arquivos: Utilize a função de descriptografia para buscar os arquivos criptografados no diretório definido e restaurá-los para o estado original. Os arquivos descriptografados serão salvos no mesmo diretório com o conteúdo legível.

## Requisitos:
* Python 3.x ou superior.
* Biblioteca os: Fornece funcionalidades para interagir com o sistema operacional, como manipulação de arquivos e diretórios.
* Biblioteca Crypto.Cipher do pacote pycryptodome: Fornece classes para criptografia e descriptografia usando algoritmos criptográficos.
* Biblioteca Crypto.Util.Padding do pacote pycryptodome: Fornece funções para realizar o preenchimento (padding) de dados criptografados.
* BibliotecaCrypto.Random do pacote pycryptodome: Fornece funções para gerar números aleatórios criptograficamente seguros.

## Clone este repositório para o seu ambiente local:
* https://github.com/juliandomeneghini/desafio-Criar-Ransomware-com-Python.git

## Instale as dependências necessárias:

* pip install -r requirements.txt

## Configuração
* Não há necessidade de configuração adicional para executar o programa.

## Siga as instruções exibidas no console para selecionar a opção desejada (criptografar ou descriptografar arquivos) e fornecer o diretório correto.

# Aviso
Certifique-se de fazer backup dos arquivos originais antes de criptografá-los, pois a descriptografia só será possível se você possuir os arquivos criptografados. O programa não se responsabiliza por quaisquer perdas de dados.

# Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma "issue" ou enviar um "pull request" com melhorias, correções de bugs ou novos recursos.
