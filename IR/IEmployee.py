from abc import ABCMeta, abstractmethod

# Abstract Class for representing an employee
class IEmployee(metaclass = ABCMeta):
   
    @abstractmethod
    def Age(self):
        pass

    @abstractmethod
    def Seniority(self):
        pass

    @abstractmethod
    def Retirementdate(self, retirement_age):
        pass