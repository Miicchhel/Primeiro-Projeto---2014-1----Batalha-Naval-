#coding: utf-8

print ('Do you like video games? yep?! Then you can to play with us')

def inicio():
    print ('-'*35,' Have Fun ','-'*113)
        
#Perguntando se o usuario deseja, ou nao, configurar o jogo.
    nome=input('Digite seu nome: ')
    n=input("Deseja configurar o jogo ou quer jogar com nossas regras? ('S' ou 'N') ")
    n.upper()
    if n=='S' or n=='s':
        #Colocamos aqui o codigo de abrir o arquivo (config.txt)
        Config= open("config.txt",)
        Config.seek(11)
        Config.read(1)
        dimensao = Config
        dimensao.seek(20)
        quantidade_D_Navios = dimensao.read(1)
        dimensao.seek(20)
        erros = dimensao.read(1)
        dimensao.close()
        print (dimensao) 

    elif n=='N' or n=='n':
        #Colocamos aqui o codigo de abrir o arquivo (grid.txt)
        Grid= open("grid.txt",r)
        Grid.seek(18)
        erros = Grid.read(18)and Grid.read(19)
        grid.readline() 
        Grid.close()
        
        print ('abrindo arquivo "grid.txt" ')

inicio()
