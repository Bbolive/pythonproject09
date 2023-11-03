# คุณสมบัติเด่น oop : Interitance สืบทอด
# คือ Class หนึ้งสือบทอดอีก Class หนึ่ง ( มีแม่ Super/ มีลูก Sub)
# พอเป็นแม่ลูกกัน แม่มีแะไรลูกมีด้วย 
class TestA :
    data1 = 10
    data2 = 20

    def showSAU( ) :
        print('Hi.....SAU')

class TestB(TestA) :
    data3 = 30

    def showWow( ) :
        print('Wow wow wow')

class TestC(TestA) :
    dataA = 40

class TestD(TestB) :
    data5 = 50

ob1 = TestA( )
ob2 = TestB( )
ob3 = TestD( )

# คุณสมบัติเด่น  oop : Polymorphism พ้องรูป
# คือ พฤติกรรมเดียวกัน แต่วิธีการต่างกัน ( ต้องเป็นแม่ ลูกกัน)
# คือ การที่ลูกเอา Method ของแม่มาเขียนใหม่
class TestZ(TestA) :
    data6 = 60
    
    # Polymorphism : Overiding Method
    def showSAU( ) :
        print('Hi.....SAU')

ob4 = TestZ( )