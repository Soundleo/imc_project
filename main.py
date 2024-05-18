print ('calculadora de IMC\n')

nome = input('Informe o seu nome:\n')
altura = str(input('Informe a sua altura\n')).replace(',','.')
altura = float(altura)
peso = str(input('Informe o seu peso:\n ')).replace(',','.')
peso = float(peso)
imc = peso/altura**2

if imc >= 35:
    print(f'Você {nome} está comendo igual uma capivara raivosa, o seu IMC é {imc:,.2f}.')
elif imc >= 30:
    print(f'Você {nome} está comendo igual uma capivara com fome, o seu IMC é {imc}.')
elif imc >= 25:
    print(f'Você {nome} está comendo igual uma capivara, o seu IMC é {imc}.')
elif imc >= 18.5:
    print(f'Parabéns {nome} o seu IMC é {imc}.')
else :
    print(f'Você {nome} está omendo igual um peixe, o seu IMC é {imc}.')

