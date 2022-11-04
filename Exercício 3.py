def Converter (horas, minutos):
    globalHoras
    globalMinutos
    if horas >= 0 and horas < 12 or horas == 24 and minutos >=0 and minutos < 60 :
        if horas == 24:
            horas = 0
        print(f'{horas}:{minutos} {A}')
    elif horas >= 12 and horas <24:
        globalHoras = horas - 12
        globalMinutos = minutos
        print(f'{globalHoras}:{minutos} {P}')
    else:
        print("Horário inválido, tente novamente colocando a hora de 0 à 24 e os minutos de 0 à 59.")
            
            
horas = 1
minutos = 1

while horas and minutos > 0:
    horas = int(input("Insira a hora no modelo 24h: "))
    minutos = int(input("Agora coloque os minutos: "))
    A = 'A.M.'
    P = 'P.M.'

    Converter(horas,minutos)
    
    
    

            
