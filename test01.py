def sumnumber ( ) :
    pass

# สร้าง  Claass  ใน Python
class IoTSAU : 
    # data/attribute/filed/property member เหมือนกับตัวแปร
    info1 = 20
    info2 = ''

    # Mathod member เหมือนกับ fuction
    def showHi(self): 
        print( 'Hi.....')

    def showInfo( self ) :
        print(self.info1, self.info1)
        self.showHi( )

# สร้าง Oobject
obA = IoTSAU( )
obB = IoTSAU( )
obC = IoTSAU( )

obA.info1 = 100
print( obA.info1 + obB.info1) # 120
obC.showInfo()
obA.showInfo()
