from cryptography.fernet import Fernet
import os

# 1. Ler a chave salva
with open("chave.key", "rb") as chave_file:
    key = chave_file.read()

fernet = Fernet(key)

# 2. Definir a pasta alvo
pasta_alvo = "RansomwareDIO1"

# 3. Lista de arquivos que NÃO devem ser descriptografados
arquivos_excluidos = ["chave.key", "RW_DIO.py", "DescptRW_DIO.py", "LEIA-ME.txt"]

# 4. Percorrer todos os arquivos da pasta
for root, dirs, files in os.walk(pasta_alvo):
    for nome_arquivo in files:
        if nome_arquivo in arquivos_excluidos:
            continue  # pula os arquivos críticos

        caminho_arquivo = os.path.join(root, nome_arquivo)

        # Ler conteúdo criptografado
        with open(caminho_arquivo, "rb") as file:
            dados_criptografados = file.read()

        # Descriptografar
        dados_originais = fernet.decrypt(dados_criptografados)

        # Restaurar o mesmo arquivo
        with open(caminho_arquivo, "wb") as file:
            file.write(dados_originais)

# 5. Atualizar o LEIA-ME.txt com mensagem de recuperação
mensagem_recuperacao = """
✅ SEUS ARQUIVOS FORAM RESTAURADOS ✅

Todos os arquivos da pasta foram descriptografados com sucesso.
Este exercício faz parte de um LABORATÓRIO DIDÁTICO de cibersegurança.

Objetivo: compreender como ransomwares funcionam e como se defender.
Nunca utilize este código fora de ambientes controlados e educacionais.
"""

with open(os.path.join(pasta_alvo, "LEIA-ME.txt"), "w", encoding="utf-8") as aviso:
    aviso.write(mensagem_recuperacao)



print("✅ Todos os arquivos da pasta foram restaurados!")