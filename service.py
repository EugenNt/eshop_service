

lass Service:
    def __init__(self,_id,_name,_price):
        self.setId(_id)
        self.setName(_name)
        self.setPrice(_price)
    

    def setId(self,id):
        self._id=id
    def getId(self):
        return self._id

    def setName(self,name):
        self._name=name
    def getName(self):
        return self._name

    def setPrice(self,price):
        self._price=price
    def getPrice(self):
        return self._price




    def __str__(self):
        return f"{self._id}-{self._name} {self._price}"

    def __repr__(self):
        return str(self)

class ServiceRepositoryFactory:
    
    def __init__(self):
        self.lastCreatedId=0
        self.service=[]
    def getService(self,name,price):
        obj=Service(id,name,price)
        self.lastCreatedId+=1
        obj.id=self.lastCreatedId
        self.save(obj)
        return obj

    def save(self,service):
        self.service.append(service)
    def saveAll(self,service):
        self.sevice=service
    
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

      
class Currency:
    def __init__(self,id,code,nominal,rate):
        self.id=id
        self.code=code
        self.nominal=nominal
        self.rate=rate
    
    def __repr__(self):
        return f"\nid={self.id}\n code={self.code}\n nominal={self.nominal}\n rate={self.rate}"
