def somar(a, b):
  soma = a + b
  print(soma)

def multiplicar(a, b):
  multiplica=a*b
  print(multiplica)

def dividir(a, b):
  dividi=a/b
  print(dividi)

print(" Seja bem-vindo a calculadora da FIAP! ")
valor1 = float(input("\nQual o primeiro valor? \n"))
valor2 = float(input("\nQual o segundo valor?\n"))
opcao=-1
while opcao!=4:
 print("\n Qual operação gostaria de fazer \n 1 - Somar \n 2 - Multiplicar \n 3 - Dividir \n 4 - Sair")
 opcao=(int(input("Escolha a sua opção: ")))
 if opcao==1:
  somar(valor1, valor2)
 elif opcao==2:
  multiplicar(valor1, valor2)
 elif opcao==3:
  dividir(valor1, valor2)