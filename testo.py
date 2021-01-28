def testo():
    username=input('enter username-')
    passward=input('enter passward-')
    f=open('adminn.txt','r')
    a=f.read()
    a=a.split('\n')
    a.pop()
    for i in a:
        b=i.split(' ')
        
        if username==b[3] and passward==b[5]:
            print('access granted')
            break
    else:
        print('access denied')    
testo()             