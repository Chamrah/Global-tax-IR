# Importing the Employe and IR classes
from Employee import Employee
from ir import IR

# Class Agent that herite from Employee and IR
class Agent(Employee, IR):
    def __init__(self, mtle, nom, dateNaissance, dateEmbauche, salaireBase, PrimeResponsabilite):
        super().__init__(mtle, nom, dateNaissance, dateEmbauche, salaireBase)
        self.__PrimeResponsabilite = PrimeResponsabilite

    def GetResponsabilite(self):
        return  self.__PrimeResponsabilite
    
    def SetResponsabilite(self, NewResponsabilite):
        self.__PrimeResponsabilite = NewResponsabilite

    
    def salaireAPayer(self):
        return (self.getsalaireBase + self.__PrimeResponsabilite) * (1 - self.getIR(self.getsalaireBase))