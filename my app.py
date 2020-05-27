#Boas Vindas
print ("Seja Bem-vindo ao programa de cálculo de média do nosso concurso!!")
print ("Será uma honra te ajudar!")
print ("Nós só precisamos de algumas informações suas, só levará 1 minuto...")

#Concurso público (SOMENTE MAIORES DE IDADE)
#Apresentação para recebimento de nota
nome = str (input("Qual é o seu nome?"))
idade = str (input("Quantos anos você tem?"))
localização = (input("De que Estado você é?"))
motivo = (input("Por que você fez esse concurso?"))

#inicio do cálculo
print (nome + ", agora nós podemos conferir as sua média!")

#Definindo as notas
nota1 = float (input("Digite sua primeira nota:"))
nota2 = float (input("Digite sua segunda nota:"))
nota3 = float (input("Digite sua terceira nota:"))
nota4 = float (input("Digite sua quarta nota:"))

#Faz o cálculo da média
media = (nota1 + nota2 + nota3 + nota4)/4

#Imprime a média
print (media)

#Resposta para saber se passa ou não de ano
if media >= 7:
    print ("Parabéns, " + nome + "!! Você foi aprovado!")
else:
    print ("Infelizmente você foi reprovado")
