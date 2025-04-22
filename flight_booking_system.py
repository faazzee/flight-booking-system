class passanger:
    def __init__(self):
        self.passanger_details=[]
    def passangerbookings(self,name:str,phone_number:int,passport_no:int,):
            tix={"name":name,"phone_number":phone_number,"passport_no":passport_no}
            self.passanger_details.append(tix)
            print(self.passanger_details)
    def deletebooking(self,name:str):
         for i in self.passanger_details:
          if i['name']==name:
              self.passanger_details.remove(i)
              print("the booking is deleted")
    def viewbooking(self):
         for i in self.passanger_details:
              print(i)
class flight:
     def __init__(self):
          self.flight_detils=[]
     def flight(self,flight_type:str,flight_numberplate:str,flight_quantity:int):
          details={"flight_type":flight_type,"flight_numberplate":flight_numberplate,"flight_quantity":flight_quantity}
          self.flight_detils.append(details)
          print(self.flight_detils)


class booking:
     def __init__(self):
          pass
Flight=flight()
Passanger=passanger()
while True:
     
     userinput=int(input("what do u want to do??\n 1. give yr pass details? \n 2.chk flight\n 3.delete booking\n 4.view booking \n 5. "))
     if userinput==1:
        name=str(input("what is your name"))
        phone_number=int(input("what is yr phno"))
        passport_no=int(input("what is yr pass no"))
        Passanger.passangerbookings(name,phone_number,passport_no)
     
     elif userinput==2:
          flight_type=str(input("what flight type?"))
          flight_numberplate=int(input("what is the numberplate"))
          flight_quantity=int(input("how many passengers can it hold"))
          Flight.flight(flight_type,flight_quantity,flight_numberplate)
     
     elif userinput==3:
          delete=str(input("who do u want to dele booking for?"))
          Passanger.deletebooking(delete)
     
     elif userinput==4:
          Passanger.viewbooking()
