

class Service:
    def __init__(self,id,name,money):
        self.id=id
        self.name=name
        self.money=money
    
    def __str__(self):
        return f"{self.id}-{self.name} {self.money}"

    def __repr__(self):
        return str(self)

class ServiceRepositoryFactory:
    
    def __init__(self):
        self.lastCreatedId=0
        self.service=[]
    def getService(self,name,money):
        obj=Service(id,name,money)
        self.lastCreatedId+=1
        obj.id=self.lastCreatedId
        self.save(obj)
        return obj

    def save(self,service):
        self.service.append(service)
    
    def all(self):
        return  tuple(self.service)
    
    def findById(self,id):
        for s in self.service:
            if s.id == id:
                return s
    def findByName(self,name):
        for s in self.service:
            if s.name==name:
                return s

    def deliteById(self,id):
        if self.id == id:
            self.service.pop(self.id -1 )

      


srf=ServiceRepositoryFactory()
s1=srf.getService("NameFirst",100)
print(s1)