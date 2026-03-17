# Desafio_final_DIO_SECURITY


README:

- 📘 **Descrição da atividade** (contexto educacional e objetivos).
- 🔐 **Ransomware simulado** (criptografa arquivos e gera mensagem de resgate).
- 🔓 **Script de descriptografia** (restaura os arquivos e atualiza a mensagem).
- ⌨️ **Keylogger simulado** (captura teclas, gera logs e envia por e-mail).

Com base nisso, aqui está o **README.md consolidado** para o seu repositório no GitHub:

---

# 🛡️ Laboratório de Cibersegurança em Python

Este repositório contém a implementação prática de **malwares simulados** em Python — **Ransomware** e **Keylogger** — desenvolvidos em ambiente controlado e com fins **exclusivamente educacionais**.

O objetivo é compreender como essas ameaças digitais funcionam, como exploram vulnerabilidades e, principalmente, como podemos **detectar, mitigar e nos proteger** delas no mundo real.

---

## 🚀 Descrição do Desafio

Este projeto faz parte de um laboratório de cibersegurança, onde foram implementados:

- **Ransomware Simulado**

  - Criptografa arquivos de uma pasta alvo.
  - Gera mensagem de resgate (`LEIA-ME.txt`).
  - Script complementar para **descriptografar** e restaurar os arquivos.
- **Keylogger Simulado**

  - Captura teclas digitadas em diferentes janelas.
  - Salva registros em arquivos `.txt`.
  - Implementa envio automático dos logs por e-mail.
- **Reflexão sobre Defesa**

  - Medidas de prevenção e proteção contra malwares.
  - Importância de antivírus, firewall, sandboxing e conscientização do usuário.

---

## 📂 Estrutura do Repositório

```
/RansomwareDIO1
│── RW_DIO.py            # Script de criptografia (ransomware simulado)
│── DescptRW_DIO.py       # Script de descriptografia
│── chave.key             # Chave de criptografia gerada
│── LEIA-ME.txt           # Mensagem de resgate/recuperação
│── arquivos_teste/       # Pasta com arquivos simulados
│── img/                  # imagens do laboratório

/keylogger
│── keylogger.pyw         # Script de captura de teclas
│── CAPTURAS/             # Pasta com logs gerados
│── img/                  # imagens do laboratório
│── senha_py_email.txt    # Senha simulada para envio de e-mail
```

---

## 🔐 Ransomware Simulado

- Utiliza a biblioteca `cryptography` (Fernet).
- Criptografa todos os arquivos da pasta alvo, exceto os listados em `arquivos_excluidos`.
- Cria um arquivo `LEIA-ME.txt` com instruções simuladas de resgate.
- Script complementar (`DescptRW_DIO.py`) permite restaurar os arquivos com a chave correta.

⚠️ **Atenção:** este código é apenas uma simulação didática. Nunca utilize fora de ambientes controlados.

---

## ⌨️ Keylogger Simulado

- Utiliza a biblioteca `keyboard` para capturar teclas.
- Registra entradas em arquivos `.txt` organizados por janela ativa.
- Implementa envio automático dos logs por e-mail a cada 120 segundos.

⚠️ **Atenção:** este código é apenas para fins educacionais. Não deve ser usado em sistemas reais sem consentimento.

---

## 🛡️ Reflexão sobre Defesa

Para se proteger contra malwares como ransomware e keylogger:

- **Antivírus e Antimalware**: detectam e bloqueiam comportamentos suspeitos.
- **Firewall**: impede conexões não autorizadas.
- **Sandboxing**: executa programas em ambientes isolados.
- **Backup Regular**: garante recuperação de dados sem depender de resgate.
- **Conscientização do Usuário**: evita cliques em links maliciosos e uso de senhas fracas.

---

## ▶️ Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/seuusuario/laboratorio-ciberseguranca.git
   ```
2. Crie um ambiente virtual e instale dependências:

   ```bash
   pip install cryptography keyboard pywin32
   ```
3. Execute os scripts em ambiente controlado:

   - **Ransomware**: `python RW_DIO.py`
   - **Descriptografia**: `python DescptRW_DIO.py`
   - **Keylogger**: `python keylogger.pyw`

---

## 📌 Objetivo Educacional

Este projeto é parte de um laboratório de estudos em cibersegurança.
Ele demonstra, na prática, como malwares funcionam e como podemos nos defender.
Não deve ser utilizado para fins maliciosos.

---

## ⚖️ Aviso Legal

Este repositório tem **propósito exclusivamente educacional**.
O autor não se responsabiliza por usos indevidos do código aqui disponibilizado.
Nunca execute estes scripts em sistemas reais ou sem consentimento explícito.

---
