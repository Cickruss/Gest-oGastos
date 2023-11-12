from Models import Usuario, Integrante, Familia

familia = Familia.Familia(0, 0, 0)
def cadastrarUsuario(nome, dataNascimento, parentesco):#, fotoPerfil):
    try:
        usuario = Usuario.Usuario(nome, dataNascimento, parentesco) #, fotoPerfil)
        print("Cadastro de usuario realizado.")
        print('nome: '+usuario.nome)
        nomeFamilia = nome.split()
        nomeFamilia = str(nomeFamilia[-1])
        familia.nome = nomeFamilia
        familia.usuario = usuario
        print('Familia: '+nomeFamilia)
    except:
        print('Falha ao cadastrar usuário.')

lista_integrantes = []
def cadastrarIntegrante(nome, dataNascimento, parentesco): #, fotoPerfil):
    try:
        integrante = Integrante.Integrante(nome, dataNascimento, parentesco)#, fotoPerfil)
        lista_integrantes.append(integrante)
        familia.integrantes = lista_integrantes
        print("Cadastro de integrante realizado.")
        print('nome: '+integrante.nome)
    except:
        print('Falha ao cadastrar integrante.')

def mostrarDashboard():
    lista_nomes_integrantes = []
    for integrante in familia.integrantes:
        lista_nomes_integrantes.append(integrante.nome)
    print(f'Familia: {familia.nome}\nUsuário: {familia.usuario.nome}\nIntegrantes: {", ".join(lista_nomes_integrantes)}')

