from requests import *
 
def token_hash(a, b):
  r = requests.post('https://dc1-2021.glitch.me/getHash', data={'rm': a, 'senha': b})
  print("Esse é o seu token: \n", r.text)
 
print("Bem-vindo ao acesso para o Webservice do DC1-2021 FIAP! \n")
 
rm=str(input("Nos informe o seu RM: "))
pswd=str(input("Nos informe a sua senha: "))
 
token_hash(rm, pswd)
