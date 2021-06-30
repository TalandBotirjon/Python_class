
"""
* Pythonda Mashina classini tuzish.
"""
"""
* Creating a Machine Class in Python.
"""
"""
Создание машинного класса в Python.
"""


class Machine():
    """
    Class Machine. 
    Values: Machine name,
    Machine maker name,
    Machine make year,
    Machine machine cost.
    """
    def __init__ (self, name, makername, myear, cost ):
        self.name = name
        self.makername = makername
        self.myear = myear
        self.cost = cost
        
    def getname(self):
        """Return Machine name. """
        return self.name
        
    def getmaker(self):
        """Return Machine maker name. """
        return self.makername
        
    def getyears(self):
        """ Return Machine make years. """
        return self.myear
        
    def getcost(self):
        """Return Machine costs. """
        return self.cost
        
    def getinfo (self):
        """Machine info print. """
        print(f"{self.name}, maker {self.makername}.")
        print(f"Make year: {self.myear}. Cost {self.cost}")


mashina = Machine('BMW M5', "BMW", 2010, 15000)

#print(mashina.getname())
#print(mashina.getmaker())
#print(mashina.getyears())
#print(mashina.getcost())

print(mashina.getinfo())


# I love Uzbekistan :)
