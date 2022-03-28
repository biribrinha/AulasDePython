#utilizar dois valores e informar qual valor é maior#

# a = int(input('primeiro valor'))
# b = int(input('segundo valor'))
# c = int(input('terceiro valor'))

#é possível definir o início e fim de um bloco com a identação#
# if a > b and a > c:
#     print('o maior número é {}' .format(a))
# elif b > a and b > c:
#     print('o maior número é {}' .format(b))
# else:
#     print('o maior númro é {}' ,format(c))
#
# print('final do programa') #vai imprimir na tela idependente se A é maior q B#




#transformar em centavos#

# a = int(input('transforme qualquer numero em centavos'))
# b = 100 #para converter um numero inteiro pra centavos, sempre dividir por 100#
#
# centavo = a / b
# centavo = str(centavo)
# print(type(centavo))
#
# print('R$' + centavo + ' centavos')


#ver se o número é par#
# a = int(input('Primeiro valor: '))
# b = int(input('Segudo valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print ('foi digitado um número par')
# else:
#     print('nenhum numero par foi digitado')


#ver notas bimestrais, tirar media, e se foi inserida corretamente#

# a = int(input('primeiro bimestre: '))
# b = int(input('segundo bimestre: '))
# c = int(input('terceiro bimestre: '))
# d = int(input('quarto bimestre: '))
#
# media = (a + b + c + d) / 4
#
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}' .format(media))
# else:
#     print('foi informado alguma nota errada')


    #outra forma de fazer#


a = int(input('primeiro bimestre: '))
if a > 10:
    a = int(input('as notas são de 0 a 100. Tente novamente'))
b = int(input('segundo bimestre: '))
if b > 10:
    b = int(input('as notas são de 0 a 100. Tente novamente'))
c = int(input('terceiro bimestre: '))
if c > 10:
    c = int(input('as notas são de 0 a 100. Tente novamente'))
d = int(input('quarto bimestre: '))
if d > 10:
    d = int(input('as notas são de 0 a 100. Tente novamente'))


media = (a + b + c + d) / 4

print('media: {}' .format(media))






