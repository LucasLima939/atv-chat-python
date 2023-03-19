totalDias = ''
while(totalDias == ''):
    anos = input("Há quantos anos você fuma?....: ")

    try: 
        totalDias = int(anos) * 30 * 12
    except:
        print("<<< Por favor, digite o valor inteiro em anos >>>")
        
gastoUnitario = ''
while(gastoUnitario == ''):
    gasto = input("Quanto você gasta por maço? Ex: 11.99....: ")

    try:
        gastoUnitario = float(gasto)
    except:
        print("<<< Por favor, digite um valor numérico >>>")

consumoDiario = ''
while(consumoDiario == ''):
    consumo = input("Quantos maços você fuma por dia?....: ")

    try:
        consumoDiario = float(consumo)
    except:
        print("<<< Por favor, digite um valor numérico >>>")

gastoTotal = totalDias * gastoUnitario * consumoDiario

if(gastoTotal < 20000):
    print("Com o valor R$ {:.2f}, você poderia ter dado entrada em um carro.".format(gastoTotal))
elif(gastoTotal < 50000):
    print("Com o valor R$ {:.2f}, você poderia ter comprado um carro popular usado.".format(gastoTotal))
else:
    print("Com o valor R$ {:.2f}, você poderia ter comprado um carro zero.".format(gastoTotal))