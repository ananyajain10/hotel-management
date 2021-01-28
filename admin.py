import datetime
import os
def format():
    print('\n--------------------------------------\n')
def admin():
    os.system('cls')
    print('**************enter new registration*************')
    namef=input('Enter Firstname --')
    namel=input('Enter Lastname --')
    mobno=input('Enter phone number --')
    emailid=input('Enter user email_id--')
    days=input('Enter no. of days--')
    ch=int(input('1.GENERAL\n2.JOINT\n3.DULEX\n4.MULTI_DULEX\nchoose one catagory='))
    format()
    if ch==1:
        amount=int(days)*2000
    if ch==2:
        amount=int(days)*4000
    if ch==3:
        amount=int(days)*6000
    if ch==4:
        amount=int(days)*10000
        
        
    date=datetime.datetime.now().date()
    hs=datetime.datetime.now().hour
    mn=datetime.datetime.now().minute
    ss=datetime.datetime.now().second
    time=str(hs)+ ':'+str(mn)+ ':'+str(ss)
    final= namef + ' ' + namel + ' ' + mobno + ' ' + emailid + ' ' + str(days) + ' ' + str(ch) + ' ' + str(date) + ' ' + str(time)+ ' '+str(amount)+ '\n'
    f=open('Costumer.txt','a')
    f.write(final)
    f.close()