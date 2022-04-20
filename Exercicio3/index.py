print('Nomes cadastrados: Pedro, Eduardo, Carlos, Renato, Cleude, Vicente e Flavia')
print('')
print('WARNING: IF YOU PUT SOME NAME THAT DO NOT EXIST THIS APPLICATION WILL SHOW YOU AN ERRO!!!')
print('')


Pedro = ['Pedro', 2500]

Eduardo = ['Eduardo',3000]

Carlos = ['Carlos',4500]

Renato = ['Renato',2300]

Cleude = ['Cleude',6000]

Vicente = ['Vicente',700]

Flavia = ['Flavia',5500]



putName = input('Coloque o nome da pessoa desejada: ')



def chekingAndReturningTheNameAndTheSalary(input):
  print('O salario de ' + str(input[0]) + " seria de " + str(input[1]))


chekingAndReturningTheNameAndTheSalary(putName)

