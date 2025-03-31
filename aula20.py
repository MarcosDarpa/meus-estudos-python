valor1 = input("Digite o primeiro valor: ")
valor2 = input("Digite o primeiro valor: ")

valor1 = int(valor1)
valor2 = int(valor2)

if valor1 > valor2:
    print(f"O primeiro valor {valor1} é maior que o segundo valor {valor2}")
elif valor1 == valor2:
    print('Os valores são iguais!')
elif valor1 < valor2:
    print(f'O segundo valor {valor2} é maior que o primeiro valor {valor1}')
else:
    print('Error: Digite um valor válido!')
