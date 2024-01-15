# Import class
from Employee import Employee  
from ir import IR

class Trainer(Employee, IR):
    def __init__(self, mtle, nom, dateNaissance, dateEmbauche, salaireBase):
        super().__init__(mtle, nom, dateNaissance, dateEmbauche, salaireBase)
        self.__heureSup = 0
        self.__tarifHsup = 70
    
    @property
    def getheureSup(self):
        return self.__heureSup
    
    @property
    def gettarifHsup(self):
        return self.__tarifHsup
    
    def setheureSup(self, hs1):
        self.__heureSup = hs1
    
    def settarifHsup(self, Ths):
        self.__tarifHsup = Ths
    
    def __str__(self):
        return super().__str__() + f"Number of overtime hours per month:" + str(self.getheureSup)+   +"- Remuneration per overtime hour:" + str(self.gettarifHsup)

    def salaryToPay(self):
        return (self.getsalaireBase + self.getheureSup * self.gettarifHsup) * (1 - self.getIR(self.getsalaireBase))