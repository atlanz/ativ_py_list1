number = int(input("Informe um numero de 3 caracteres: "))
centena = number // 100
dezena = (number % 100) // 10
unidade = (number % 10) 
print (number, '\ncentena: ',centena, '\ndezena: ',dezena, '\nunidade: ',unidade)