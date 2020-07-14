"""https://alwayscodin.blogspot.com/2020/06/tcs-opa-12th-june-solution.html"""

#Please refer this above link for quesion

"""
Input :

4
1
Yes
2.5
Yes
87
2
No
3.5
No
123
3
Yes
1.5
No
56
4
Yes
2
Yes
104
87


Output:

87 Cleared
135.0
"""


class ParkedVehicle:
    """vehicleSeq,fourWheeler,parkedFor,valetParking,parkedStatus"""
    def __init__(self,vehicleSeq,fourWheeler,parkedFor,valetParking):
        self.vehicleSeq=vehicleSeq
        self.fourWheeler=fourWheeler
        self.parkedFor=parkedFor
        self.valetParking=valetParking
        self.parkedStatus="Parked"

    


class ParkingLot:
    def __init__(self,vehicleobj):
        self.vehicleobj=vehicleobj

    def updateParkedStatus(self,lot_number):
        res=None
        for i in self.vehicleobj:
            if i == lot_number:
                self.vehicleobj[i].parkedStatus="Cleared"
                res=self.vehicleobj[i].parkedStatus
                break
        return res
        

    def getParkingCharges(self,lot_number):
        """if fourwheeler is yes then hour*50 else hour*30
        if valetparking is yes then add 10
        """
        res=None
        for i in self.vehicleobj:
            if i== lot_number:
                if self.vehicleobj[i].fourWheeler=="Yes":
                    res=self.vehicleobj[i].parkedFor*50
                else:
                    res=self.vehicleobj[i].parkedFor*30

                if self.vehicleobj[i].valetParking=="Yes":
                    res+=10
        return res
        

t=int(input())
d=dict()
for i in range(t):
    seqn=int(input())
    fourw=input()
    hour=float(input())
    valet=input()
    lot=int(input())
    temp=ParkedVehicle(seqn,fourw,hour,valet)
    d[lot]=temp

n=int(input())
p=ParkingLot(d)
res1=p.updateParkedStatus(n)
res2=p.getParkingCharges(n)
if(res1==None):
    print("Lot number not found")
else:
    print(str(n)+res1)

if(res2==None):
    print("Lot number not found")
else:
    print(res2)