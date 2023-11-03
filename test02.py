class IoTThailand :
    # data
    wow = 100

    # Contruture ไม่ใช่ Member แต่จะทำงานทุกครังที่สร้าง object
    # contruture
    def __init__( self , woo, wee, wea) : # parameter 3 = woo wee wea
        self.woo = woo
        self.wee = wee
        self.wea = wea
    
    
    #Method 
    def showdata(self) :
        print(self.wow * 20)

    #Destructure
    def __del__(self) :
        print('Good Morning Teacher.....')


ob1 = IoTThailand( 10, 20, 10 )
ob2 = IoTThailand( 10, 20, 30 )
ob3 = IoTThailand( 5, 20, 20 )
ob4 = IoTThailand( 10, 20, 10 )

print(ob1.wea + ob2.wea)
print(ob3.showdata( ))
