hora1 = int(input("digite a hora da primeira entrada: "))
minuto1 = int(input("digite os minutos da primeira entrada: "))
hora2 = int(input("digite a hora da segunda entrada: "))
minuto2 = int(input("digite os minutos da segunda entrada: "))

soma_horas = hora1 + hora2
soma_minutos = minuto1 + minuto2

if soma_minutos >= 60:
        soma_horas += 1
        soma_minutos -=60
if soma_horas >=12 and soma_horas >24:
    soma_horas -=12
    soma_horas-= 24



else:
    print("hora inválida")
print(f"{soma_horas}:{soma_minutos}")