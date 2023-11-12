from Models.Familia import Familia
class Integrante(Familia) :
    def __int__(self, nome, parentesco, dataNascimento):
        self.nome = nome
        self.parentesco = parentesco
        self.dataNascimento = dataNascimento
        #self.fotoPerfil = fotoPerfil #fotoPerfil
