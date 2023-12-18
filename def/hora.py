import requests
import os
from datetime import datetime
import pytz
import time


fuso_horario = pytz.timezone('America/Sao_Paulo')


hora_atual = datetime.now(fuso_horario)

print("Fuso horário:", hora_atual.tzinfo)
print("Hora local:", hora_atual.hour)



while True: 

    

    if hora_atual.hour == 13:
        requests.get('https://tudoemnuvem.com/asaas/get_logs')
    

    time.sleep(3600)