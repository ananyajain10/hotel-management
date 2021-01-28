import os
def forgetpwd():
    os.system('cls')
    import yagmail 
    import random
    print('*************regain passward***************')
    username=input('enter username-')
    email=input('enter email_id-')
    f=open('adminn.txt','r')
    r=f.read()
    s=r.split('\n')
    s.pop()
    for i in s:
        c=i.split(' ')
        if username==c[3] and email ==c[4]:
            print('yaaaaa')
            final1=''
            final2=''
            for i in range(6):
                print('yaaa2')
                x=random.randint(0,9)
                final1=final1+str(x)
                final2=final2+ ' '+ str(x)
            #print(final1,'\n',final2) 
            yag=yagmail.SMTP('jainananya355@gmail.com','@#jainananya')
            yag.send(to=email,subject='otp for forget passward',contents=final2)
            check=int(input('enter otp--'))
            print('yaaa3')
            #print(check)
            #print(final1)
            if str(check)==final1:
                print('your passward-',c[5])
            else:
                print('incorrect otp...') 
                return 0   
        else:
            return 0   

            

