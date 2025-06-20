import os
import time
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def enviar_alerta(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": texto}
    requests.post(url, data=payload)

def checar_condicoes():
    # Simulação de sinal (modo agressivo: sempre alerta pra testar)
    return True

if __name__ == "__main__":
    while True:
        if checar_condicoes():
            enviar_alerta("🚨 Alerta automático: possível sinal de entrada detectado.")
        time.sleep(900)  # Espera 15 minutos
