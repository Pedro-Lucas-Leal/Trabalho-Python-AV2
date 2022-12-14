def Converter(horas, minutos):
    if horas >= 0 and horas < 12 or horas == 24 and minutos >= 0 and minutos < 60:
        if horas == 24 and minutos >= 0 and minutos < 60:
            horas = 0
        Imprimir(horas, minutos, A)
    elif horas >= 12 and horas < 24 and minutos >= 0 and minutos < 60:
        if horas > 12:
            horas = horas - 12
        Imprimir(horas, minutos, P)
    else:
        Imprimir(horas, minutos, 0)

def Imprimir(horas, minutos, nomenclatura):
    if nomenclatura == A:
        print(f'{horas}:{minutos} {A}')
    elif nomenclatura == P:
        print(f'{horas}:{minutos} {P}')
    else:
        print("Horário inválido, tente novamente colocando a hora de 0 à 24 e os minutos de 0 à 59.")

while True:
    horas = int(input("Insira a hora no modelo 24h: "))
    minutos = int(input("Agora coloque os minutos: "))
    A = 'A.M.'
    P = 'P.M.'
    if horas >= 0 and minutos >= 0:
        Converter(horas, minutos)
    else:
        break
