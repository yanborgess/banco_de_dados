from database import db, Usuario, Anuncio

db.connect('freelancers.db')

db.create_tables([Usuario, Anuncio])

#  CRIAR USUARIOS NA TABELA
usuario =  Usuario.create(nome="Yanzin", email= "teste@teste.com", senha ="123456" )
print ("Novo usuario:", usuario.id, usuario.nome, usuario.email)


# LSITAR TODOS OS USUARIOS
Usuario.create(nome="Yanzin", email= "teste@teste.com", senha ="1234556" )
Usuario.create(nome="jorde", email= "teste2@teste.com", senha ="1234546" )
Usuario.create(nome="Yazin", email= "teste3@teste.com", senha ="1234536" )

lista_usuarios = Usuario.select()
print("Listando usuarios: ")

for u in lista_usuarios:
    print("-", u.id, u.nome, u.email)

# USUARIO PELO ID 
usuario1 = Usuario.get(Usuario.id == 1)
print("Usuario pelo id ->", usuario1.id, usuario1.nome)

# USUARIO PELO EMAIL 
yan = Usuario.get(Usuario.email == "teste@teste.com")
print("Usuario pelo email ->", yan.id, yan.nome, yan.email)

# ALTERAÇOES NA TABELA
jorde = Usuario.get(Usuario.email == "teste2@teste.com")
jorde.nome = "jorge"
jorde.save()
print("Jorde atualizado: ", jorde.nome)

# TENTANDO CRIAR UM USUARIO COM EMAIL DUPLICADO
print("Tentando criar um usario duplicado")

try:
    Usuario_dplicado = Usuario.create(nome = "duplicado", email ="teste2@teste.com", senha = "123456")
except:
    print("Email ja existente!")

# DELETAR UM USUARIO

usuario_deletado = Usuario.get(Usuario.email == "teste@teste.com")
usuario_deletado.delete_instance()

try:
    Usuario.get(Usuario.email == "teste@teste.com")
except:
    print("Usuario deletado!")

# CRIANDO UM ANUNCIO

Yanzin = Usuario.get(Usuario.email =="teste@teste.com")

anuncio = Anuncio.create(
     usuario = Yanzin,
   titulo = "videeo de banco de dados",
     descricao = "O projeto seria criar um video sobre banco de dados  e ORM em python",
     valor = 500.0
 )
print("novo anuncio: ", anuncio.id, anuncio.titulo)

# FILTRANDO ANUNCIOS POR USUARIO 

Anuncio.create(usuario = Yanzin, titulo = "Anuncio 1", descricao = "Deixa o like", valor = 1000)
Anuncio.create(usuario = Yanzin, titulo = "Anuncio 2", descricao = "COmente", valor = 2000)
Anuncio.create(usuario = Yanzin, titulo = "Anuncio 3", descricao = "likezada", valor = 5000)

print("anuncios do yan :")
# BUSQUE NA TABELA ANUNCIOS, INCLUINDO A TABELA USUARIO, AONDE O EMAIL USUARIO É IGUAL AO EMAIL
anuncios_yan = Anuncio.select().join(Usuario).where( Usuario.email == "teste@teste.com")
for a in anuncios_yan:
    print("-", a.id, a.titulo, a.valor)


# DELETAR UM ANUNCIO
Anuncio.delete().execute()

print("Quantidade de anuncios:", Anuncio.select().count())