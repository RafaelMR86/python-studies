import hashlib

#Criando uma lista vazia chamada “usuários”

usuarios = []

#Criando um usuário como dicionário com name, username e password

usuario = {

    "name": "Clark Kent",

    "username" : "kent",

    "password" : "6c70795dc50a2d6765a44bceda2699c48a8e81effe3f9e7cf3b6f8bb34ccb5b2"

}

# Inclui este usuário na lista usuários

usuarios.append(usuario)

#Criando um usuário como dicionário com name, username e password
usuario = {

    "name": "Bruce Wayne",

    "username" : "wayne",

    "password" : "0bf3116d14ceeb7b8859abb9f5b90a7747913185930fed774a949cc8777a990a"

}

# Inclui este usuário na lista usuários

usuarios.append(usuario)


#Criando um usuário como dicionário com name, username e password
usuario = {

    "name": "Christopher Walker",

    "username" : "walker",

    "password" : "db7e65b576f6b3db9041cbddff92f9a4b7253b795aab817d3f348977b014cd83"

}

# Inclui este usuário na lista usuários

usuarios.append(usuario)

# Solicita o nome e senha do usuário. Assim que recebe a senha já peço para transformar em bytes

user=str(input("Nos informe o seu usuário: "))
password=input("Senha: ").encode('utf-8')

# Criando uma nova variável que receba a senha anterior transformada em bytes e já transforme na criptografia SHA256 em hexadecimal

password_hash=hashlib.sha256(password).hexdigest()

#Criando loop para a lista usuários. Aqui se utiliza a lista + dict para que possa ler todos os valores internos com um break caso ache o correto.
for i in usuarios:
  if i['username']==user and i['password']==password_hash:
    print("{} logado!" .format(i['name']))
    break
else:
  print("Usário/senha inválidos")