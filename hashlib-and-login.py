import hashlib

usuarios = []

usuario = {

    "name": "Clark Kent",
    "username" : "kent",
    "password" : "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2"

}

usuarios.append(usuario)

usuario = {

    "name": "Bruce Wayne",
    "username" : "wayne",
    "password" : "0bf3116d14ceeb7b8859abb9f5b90a7747913185930fed774a949cc8777a990a"

}

usuarios.append(usuario)

usuario = {

    "name": "Christopher Walker",
    "username" : "walker",
    "password" : "db7e65b576f6b3db9041cbddff92f9a4b7253b795aab817d3f348977b014cd83"

}

usuarios.append(usuario)

user=str(input("Nos informe o seu usuário: "))
password=input("Senha: ").encode('utf-8')
password_hash=hashlib.sha256(password).hexdigest()

for i in usuarios:
  if i['username']==user and i['password']==password_hash:
    print("{} logado!" .format(i['name']))
    break
else:
  print("Usário/senha inválidos")