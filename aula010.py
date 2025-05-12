#usuario indica a tabuada que ele quer, onde inicia e onde acaba
# e o programa imprime a tabuada:

tabuada = int(input('Digite a tabuada que você quer: ')) #qual tabuada sera utilizada.
inicio = int(input('Digite onde iniciara a tabuada: ')) #em qual numero inicia a tabuada.
fim = int(input('Digite onde terminará a tabuada: ')) #em qual numero termina a tabuada.

for n in range(inicio,fim+1):
    print(f'{tabuada} x {n} = {tabuada*n}') #ou print('{} x {} = {}'.format(tabuada, n, tabuada*n))

continuar = input('Deseja continuar? (s/n): ') #se o usuario quer continuar ou não.

while continuar == 's':
    tabuada = int(input('Digite a tabuada que você quer: '))
    inicio = int(input('Digite onde iniciara a tabuada: '))
    fim = int(input('Digite onde terminará a tabuada: '))

    for n in range(inicio,fim+1):
        print(f'{tabuada} x {n} = {tabuada*n}') #ou print('{} x {} = {}'.format(tabuada, n, tabuada*n))

    continuar = input('Deseja continuar? (s/n): ')