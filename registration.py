import os
def register():
    os.system('cls')
    print('**********************admin page************************')
    
    namef=input('Enter Firstname --')
    namel=input('Enter Lastname --')
    mobno=int(input('Enter phone number --'))
    username=input('Enter Username --')
    emailid=input('Enter user email_id--')
    paso=input('Enter unique passward --')
    f=open('adminn.txt','r')
    b=f.read()
    c=b.split('\n')
    c.pop()
    flag=1

    for i in c:
        z=i.split(' ')
        if username==z[3]:
            flag=0
            print('Username already exists')
            register()

    if flag==1:

        if (not os.path.exists('adminn.txt')):
            open('adminn.txt','w')
        f=open('adminn.txt','a')     
        f.write(namef+' ')
        f.write(namel+' ')
        f.write(str(mobno)+' ')
        f.write(username+' ')
        f.write(emailid+' ')
        f.write(paso+'\n')
        f.close()





