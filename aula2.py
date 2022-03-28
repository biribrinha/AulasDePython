#no phyton não é preciso declarar variável, só colocar ela direto e o seu valor#


a = int(input('Coloque o primeiro valor: '))
#input pro usuário inserir na tela#
b = int(input('Coloque o segundo valor: '))

#input é um tipo string, por isso o int abraça tudo, convertendo
# o input e possibilitando a soma#

soma = a + b

subtracao = a - b

multiplicacao = a * b

divisao = a / b

resto = a % b




# soma = str(soma)
# subtracao = str(subtracao)
# multiplicacao = str(multiplicacao)
# divisao= str(divisao)
# resto= str (resto)
#
# print(type(soma))
# print(type(subtracao))
# print(type(multiplicacao))
# print(type(divisao))
# print(type(resto))
#
#
#
# print('soma: '
#       + soma)
# print('subtração:'
#       +  subtracao)
# print('multiplicação:'
#       + multiplicacao)
# print('divisão:'
#       +divisao)
# print('resto:'
#       +resto)


#jeito mais prático de fazer#


# print('soma: {}'
#       .format(soma))

#duas contas na mesma linha#

# print('soma: {}. '
#       'subtração {}'
#       .format(soma, subtracao))
 #aparece:#
# soma: 15. subtração 5 #

#todas as contas em um print#
resultado =('soma: {}. \nsubtração {}. \nmultiplicação {}. \ndivisão {}. \nresto {}'
      .format(soma, subtracao, multiplicacao, divisao, resto))


print (resultado)





