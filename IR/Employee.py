# Import class
from datetime import datetime
from IEmployee import IEmployee
from abc import ABCMeta, abstractmethod

class Employee(IEmployee, metaclass = ABCMeta):
    
    _counter = 0
    def __init__(self, mtle, nom, dateNaissance, dateEmbauche, salaireBase):
        Employee._counter += 1
        self.__mtle = Employee._counter
        self.__nom = nom
        self.__dateNaissance = dateNaissance
        self.__dateEmbauche = dateEmbauche
        self.__salaireBase = salaireBase
    
    @property
    def getmtle(self): 
        return self.__mtle
    
    @property
    def getnom(self):
        return self.__nom
    
    @property
    def getdateNaissance(self):
        return self.__dateNaissance
    
    @property
    def getdateEmbauche(self):
        return self.__dateEmbauche
    
    @property
    def getsalaireBase(self):
        return self.__salaireBase
    
    def setmtle(self, mtle):
        self.__mtle = mtle
    
    def setnom(self, nom):
        self.__nom = nom
    
    def setdateNaissance(self, dateNaissance):
        self.__dateNaissance = dateNaissance
    
    def setsalaireBase(self, salaireBase):
        self.__salaireBase = salaireBase
    
    def setdateEmbauche(self, dateEmbauche):
        if (self.Age(dateEmbauche) < 20):
            return False
        else:
            self.__dateEmbauche = dateEmbauche
    
    @abstractmethod
    def SalaryToPay(self):
        pass

    def Age(self, dateEmbauche):
        dateNaissance = datetime.strptime(self.getdateNaissance, '%d/%m/%Y')
        dateEmbauche = datetime.strptime(dateEmbauche, '%d/%m/%Y')
        age = dateEmbauche.year - dateNaissance.year
        return age
    
    def Seniority(self):
        nowyear = datetime.now().year
        dateEmbauche = datetime.strptime(self.getdateEmbauche, '%d/%m/%Y')
        return nowyear - dateEmbauche.year
    
    def RetirementDate(self, retirement_age):
        dateNaissance = datetime.strptime(self.getdateNaissance, '%d/%m/%Y')  
        return dateNaissance.year + retirement_age
    
    def __str__(self):
        return f"Employee ID : "+self.getmtle+ "- Name:"  +self.getnom + - "Date of Birth:"  +str(self.getdateNaissance) + "- Employment Date:"  + str(self.getdateEmbauche) + "- Base Salary:"  +str(self.getsalaireBase  )
    
    def __eq__(self, other):
        return self.getmtle == other.getmtle