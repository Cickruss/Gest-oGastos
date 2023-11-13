from Models import Integrante, Familia, conn

familia = Familia.Familia(0, 0, 0)
lista_integrantes = []
def cadastrarUsuario(nome, dataNascimento, parentesco):#, fotoPerfil):
    try:
        integrante = Integrante.Integrante(nome, dataNascimento, parentesco, True) #, fotoPerfil
        lista_integrantes.append(integrante)
        print("Cadastro de usuario realizado.")
        print('nome: '+integrante.nome)
        nomeFamilia = nome.split()
        nomeFamilia = str(nomeFamilia[-1])
        familia.nome = nomeFamilia
        familia.usuario = integrante
        print('Familia: '+nomeFamilia)
    except:
        print('Falha ao cadastrar usuário.')

def cadastrarIntegrante(nome, dataNascimento, parentesco): #, fotoPerfil):
    try:
        integrante = Integrante.Integrante(nome, dataNascimento, parentesco, False)#, fotoPerfil)
        lista_integrantes.append(integrante)
        familia.integrantes = lista_integrantes
        print("Cadastro de integrante realizado.")
        print('nome: '+integrante.nome)
    except:
        print('Falha ao cadastrar integrante.')

def mostrarDashboard():
    EnviarFamiliaDB()

def EnviarFamiliaDB():
    cur, connect = conn.DB_Connect()

    contador = 2
    for integrante in lista_integrantes:
        membro_id = contador
        nome_completo = integrante.nome
        data_nascimento = integrante.dataNascimento
        parentesco = integrante.parentesco
        foto_perfil = "cokecosa"
        admin = True if familia.usuario.nome == integrante.nome else False
        print(f'{nome_completo},{admin}')
        insert = f"INSERT INTO membro_familia (membro_id, nome_completo, data_nascimento, parentesco, foto_perfil, admin) VALUES ({membro_id}, '{nome_completo}', '{data_nascimento}', '{parentesco}', '{foto_perfil}', {admin});"
        cur.execute(insert)
        connect.commit()
        contador += 1

    cur.close()
    connect.close()
    print('dados inseridos com sucesso')








