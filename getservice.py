import xml.etree.ElementTree as ET
import requests
from service import Currency
class CurrencyService:
    
    def getCurrencies(self):
        res=requests.get("https://www.bnm.md/ro/official_exchange_rates?get_xml=1&date=18.07.2021")
        currensies=[]
        data=ET.fromstring(res.text)
      
        for item in data:
            id=item.find("NumCode")
            code=item.find("CharCode")
            nominal=item.find("Nominal")
            rate=item.find("Value")
            currency=Currency(id.text,code.text,nominal.text,rate.text)
            currensies.append(currency)
    

           
            
                
    
        return currensies

cs=CurrencyService()
currs=cs.getCurrencies()
print(currs)