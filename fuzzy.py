
'''
Aluno: Gabriel de Souza Nogueira da Silva

Introduçao sobre o problema:
1-Regras utilizadas:
    1° pressao media aperta freio

    2° pressao alta , velocidade alta, rodas alta, aperta freio

    3° pressao alta , velocidade alta, rodas baixa, libera freio

     4° pressao baixa, libera freio
2- funçoes utilizadas:
    Input:
        Modelo pressao
        1- -0.6x+30  [0,50]
        2- 30 - abs((x-50)*3/2) [30,70]
        3- 0.6x-30 [50,100]

        Modelo vel rodas
        1- -0.5x+30 [0,60]
        2- 30-abs((x-50)) [20,80]
        3- 0.5x-20 [40,100]

        Modelo vel carro 
        1- -0.5x+30 [0,60]
        2- 30-abs((x-50)) [20,80]
        3- 0.5x-20 [40,100]
    Output
        Modelo freio
        aperta freio - 0.3x
        libera freio - -0.3x+30
    Obs: para facilitar a vizualizaçao das retas foi utilizado como
    maximo o valor de 30 ao inves de 1 porem nos calculos essa unidade 
    é convertida e a resposta sai corretamente.
'''
import math
import time

p = int(input("Digite a Pressao do freio: "))
vc = int(input("Digite a Velocidade do carro: "))
vr = int(input("Digite a Velocidade das rodas: "))

def pressao_freio():
    #Definindo as regras de input da pressao.
    L = -0.6*p+30
    M = 30-abs((p-50)*3/2)
    H = 0.6*p-30
    if L<0:
        L=0
    if M<0:
        M=0
    if H<0:
        H=0
    p1 = [L/30,M/30,H/30]#divide por 30 para os valores ficarem entre 0 e 1 como ja foi considerado la em cima
    return p1

def vel_rodas():
    #Definindo as regras de input da velocidade das rodas.
    S = -0.5*vr+30
    M = 30-abs((vr-50))
    F = 0.5*vr-20
    if S<0:
        S=0
    if M<0:
        M=0
    if F<0:
        F=0        
    p = [S/30,M/30,F/30]#divide por 30 para os valores ficarem entre 0 e 1 como ja foi considerado la em cima
    return p

def vel_carro():
    #Definindo as regras de input da velocidade do carro.  
    S = -0.5*vc+30
    M = 30-abs((vc-50))
    F = 0.5*vc-20
    if S<0:
        S=0
    if M<0:
        M=0
    if F<0:
        F=0
    p = [S/30,M/30,F/30]#divide por 30 para os valores ficarem entre 0 e 1 como ja foi considerado la em cima
    return p

def regra1():
#definiçao da regra1 :pressao media aperta freio
    pressao = pressao_freio()                    
    return pressao[1]

def regra2():
#definiçao da regra2 :pressao alta , velocidade alta, rodas alta, aperta freio    
    presao_freio = [pressao_freio()[2],vel_carro()[2],vel_rodas()[2]]
    return sorted(presao_freio)[0]#organiza o vetor do menor para o maior por isso pegamos a posiçao 0

def regra3():
#pressao alta , velocidade alta, rodas baixa, libera freio
    presao_freio = [pressao_freio()[2],vel_carro()[2],vel_rodas()[0]]
    return sorted(presao_freio)[0]#organiza o vetor do menor para o maior por isso pegamos a posiçao 0

def regra4():
#pressao baixa, libera freio
    pressao = pressao_freio()                    
    return pressao[0]

def libera_freio():
    soma = regra3() + regra4()#soma pois utiliza o metodo dos slides
    soma = soma*30#Multiplica por 30 para novamente entrar no padrao das retas porem isso nao muda o resultado
    return soma

def aperta_freio():
    soma = regra1() + regra2()#soma pois utiliza o metodo dos slides
    soma = soma*30#Multiplica por 30 para novamente entrar no padrao das retas porem isso nao muda o resultado
    return soma

def pa(valor_x):#funçao final, ela dara o valor da reta final para apertar o freio
    #definindo o valor da funçao que rege o dominio do aperta freio
    valor_a = aperta_freio()
    if valor_x >= 0 and valor_x <= 10*valor_a/3:
        pa_valor1 = 0.3*valor_x
    else:
        pa_valor1 = valor_a
    #definindo o valor da funçao que rege o dominio do libera freio
    valor_l = libera_freio()
    if valor_x >= 0 and valor_x <= ((-10)*valor_l + 300)/3:
        pa_valor2 = valor_l
    else:
        pa_valor2 = (-0.3)*valor_x + 30
    #O maior valor entre as duas funçoes é o que domina na funçao final logo é retornado o maior valor para
    #um mesmo ponto para compor a reta final

    if pa_valor1 >= pa_valor2:
        #print(round(pa_valor1/30,2))
        return pa_valor1
        
    else:
        #print(round(pa_valor2/30,2))
        return pa_valor2    

def output():
    #utilizando a formula do centro de gravidade temos:
    c1 = 0
    c2 = 0
    for k in range(0,101, 1):#roda de 0 a 100 ao passo de 1 em 1
        c1 = c1 + (pa(k)*k)
     
    for k in range(0,101,1):#roda de 0 a 100 ao passo de 1 em 1
        c2 = c2 + (pa(k))
        
    c = c1/c2
    print(c)
    return c #valor com que o freio deve ser apertado dps de se ter analizado as regras

output()