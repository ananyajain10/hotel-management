from login import login
from admin import admin
from registration import register
from receipt import receipt
def format():
    print('\n----------------------------------------\n')
import os
os.system('cls')
def indexo():
    os.system('cls')
    print('1.ADMIN\n2.REGISTRATION PAGE\n3.RECIEPT')
    x=int(input('enter no='))
    if x==1:
        
        z=login()
        if z==1:
            #entry for new admin
            register()
        if z==0:
            format()
            print(input('press enter to continue...'))
            indexo()    
    if x==2:
        
        z=login()
        if z==1:
            #costumer entry
            admin()
        if z==0:
            print(input('press enter to continue...'))
            indexo()
    if x==3:
        receipt()
        
indexo()      



    
