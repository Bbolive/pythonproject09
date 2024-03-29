# คุณสมบัติเด่น oop : Encapsulation แปลว่า ห่อหุ่มหรือซ่อนไว้
# ห่อหุ่ม/ซ่อน dara โดยใส่ __ ไว้หน้าชื่อ data
class MytestA :
    __data1 = 10
    data2 = 20

# เมื่อ data ถูก Encap. การกำหนดค่าหรือเอาค่ามาใช้
# ให้ผ่าน Mathod get เอาค่ามาใช้/set กำหนดค่า

    def getData1(self) :
        return self.__data1
    
    def setData1(self, data1):
        self.__data1 = data1

    def getData3(self) :
        return self.__data3
    
    def setData3(self, data3):
        self.__data3 = data3

    def __init__(self,data3) :
        self.__data3 = data3

    def showData ( self ) :
        print(f'__data1 มีค่า {self.__data1}')
        print(f'data2 มีค่า {self.data2}') 
        print(f'__data3 มีค่า {self.__data3}') 
        print('-------------------------------------')

ob1 = MytestA( 30 )
ob1.showData( )
ob1.data2 = 200
# ob1.__data1 = 100
ob1.setData1(100)
# ob1.__data3 = 999
ob1.setData3(999)
ob1.showData( )
print(ob1.getData3())
