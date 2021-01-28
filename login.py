import os
from forgetpwd import forgetpwd
def format():
    print('\n-------------------------------\n')
def login():
    os.system('cls')
    print('**************AUTHENTICATION********************')
    
    username=input('enter username--')
    passward=input('enter passward--')


    f=open('adminn.txt','r')
    z=f.read()
    f.close()
    z=z.split('\n')
    z.pop()
    
    cn=[]
    cp=[]    
    for i in z:
        b=i.split(' ')
        cn.append(b[3])
        cp.append(b[5])
    
    
    if username in cn and passward in cp:
        os.system('cls')
        
        if cn.index(username)==cp.index(passward):
            format()
            print('access granted')
            return 1
        else:
            format()
            print('wrong passward') 
            forgetpwd() 
            
                        
    else:
        format()
        print('wrong passward') 
        forgetpwd()
                      

        
        

        