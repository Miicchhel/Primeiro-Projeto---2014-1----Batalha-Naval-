#BATALHA NAVAL
#ALUNOS: MICHEL MELO; Welligton Luiz

continuar=("S")
while continuar == "S":

        import random

        campo_de_batalha=[]
        espelho=[]
        cord_x=0
        cord_y=0
        dimensao=int(input('Digite a dimensão do campo de batalha: '))

        #loop para caso de o usuario digitar o numero diferente da dimensao
        while dimensao < 3 :
                print (dimensao)
                dimensao=0
                dimensao=int(input(' A dimensão tem que ser maior que 3 : '))

        tiros=int(input('Deseja ter quantos Tiros: '))
        while True:
                navios= int(input("Digite a quantidade os navios: "))
                if navios > dimensao:
                        print ('Quantidade maxima de navios excedida. \nMáximo permitido é de %d' % dimensao)
                else:
                        break
        print('Tentativas restantes: %d' % tiros)


        #gera a primeira matriz ,como indicativo
        mat1= [1]*dimensao
        for matriz in range(dimensao):
            a=mat1[matriz]=['*']*dimensao
            print (a)
                
        #gera a matriz com 0(agua) e 1(navios)
        for i in range (dimensao):
                campo_de_batalha.append([])
                espelho.append([])
                for j in range(dimensao):
                    campo_de_batalha[i].append(0)
                    espelho[i].append('*')

        #adiciona os navios
        for ship in range (navios+1):
            xis=random.randint(1,dimensao)
            if xis == dimensao:
                xis-=1
            ypisilone=random.randint(1,dimensao)
            if ypisilone == dimensao:
                ypisilone-=1
            if campo_de_batalha[ypisilone][xis]==0:
                campo_de_batalha[ypisilone][xis]=1

        '''exibe o campo de batalha
        for i in range (dimensao):
            print(campo_de_batalha[i])'''
                
                        
        #loop para o usuario digitar as cordenadas e uns IF no caso de o usuario digitar uma coordenada diferente da dimensao
        while tiros > 0:
            tiros-=1
            cord_x=int(input('Digite a coordenada X: '))
            if cord_x >dimensao:
                cord_x=int(input('Digite a coordenada X novamente, menor que a dimensão:'))
            cord_x-=1
            cord_y=int(input('Digite a coordenada Y: '))
            if cord_y >dimensao:
                cord_y=int(input('Digite a coordenada Y novamente menor que a dimensão: '))
            cord_y-=1
            
            #condicional para o caso de ele acertar
            if campo_de_batalha[cord_x][cord_y] == 1:
                print('KABUM!:-D, Você ACERTOU!' )
                print('Tentativas restantes: %d' % tiros)
                print ('Restam apenas %d navios' % navios)
                espelho[cord_x][cord_y]='@'
                for x in range(dimensao):
                   print(espelho[x])
            #condicional para o caso de ele errar
            if campo_de_batalha[cord_x][cord_y] == 0:
                espelho[cord_x][cord_y]='%'
                print('splash :/ ,Você ERROU')
                print('Tentativas restantes: %d' % tiros)
                print ('Restam apenas %d navios' % navios)
                for x in range(dimensao):
                    print(espelho[x])
        continuar = input("deseja continuar ?(S/N) Deve-se digitar apenas S ou N: ")
        if continuar!="N" or "S":
                exit
