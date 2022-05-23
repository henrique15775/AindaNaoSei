from .. import requisicoes
class Address:
    def __init__(self, logradouro, bairro, localidadeUF, CEP):
        self.__logradouro = logradouro
        self.__bairro = bairro 
        self.__localidadeUF = localidadeUF
        self.__CEP = CEP
        
    @property
    def logradouro(self):
        return self.__logradouro    
        
    @logradouro.setter
    def logradouro(self,newLogradouro):
        self.__logradoutro = newLogradouro   
        
    @property
    def bairro(self):
        return self.__bairro    
        
    @bairro.setter
    def bairro(self,newBairro):
        self.__bairro = newBairro
        
    @property
    def localidadeUF(self):
        return self.__localidadeUF    
        
    @localidadeUF.setter
    def localidadeUF(self,newLocalidadeUF):
        self.__localidadeUF = newLocalidadeUF        
        
        
    @property
    def CEP(self):
        return self.__CEP
    
    @CEP.setter
    def CEP(self, newCEP):
        self.__CEP = newCEP    
        
        
    def PesquisarCEP(self):
        req = requisicoes.RequisicaoCep(self.__CEP)
        self.__logradouro = req.logradouro
        self.__bairro = req.bairro
        self.__localidadeUF = req.localidade
    