import pywhatkit


while True:
    print('WhatsClock')
    print('Envio de mensagem com temporizador')
    print('Número deve conter DD e DDD')
    num = input('Número: ')
    msg = input('mensagem: ')
    hora = input('hora: ')
    minuto = input('minutos: ')

    pywhatkit.sendwhatmsg({num}, {msg}, {hora},{minuto})








