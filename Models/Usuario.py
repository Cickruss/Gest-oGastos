from Models.Familia import Familia
class Usuario(Familia):
    def __init__(self, nome, dataNascimento, parentesco):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.parentesco = parentesco
        #self.fotoPerfil = fotoPerfil #fotoPerfil
