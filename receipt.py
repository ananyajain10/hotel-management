

def receipt():
    import yagmail
    first_name=input('Enter first_name-')
    last_name=input('Enter last_name-')

    f=open('costumer.txt','r')
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

    if first_name==b[0] or last_name==b[1]:
        namef=first_name 
        namel=last_name
        mob=b[2]
        date=b[6]
        time=b[-2]
        days=b[4]
        amount=b[-1]
        type=b[5]

        if type==1:
            type='GENERAL'

        if type==2:
            type='JOINT'

        if type==3:
            type='DULEX'

        if type==4:
            type='MULTI_DULEX'                                    

        svp= ''
        svp+='NAME=\t'+ namef + namel+'\n'
        
        svp+='CONTACT_NO=\t'+ str(mob)+'\n'
        svp+='CHECK_IN_DATE=\t'+ str(date)+'\n'
        svp+='CHECK_IN_TIME=\t'+ str(time)+'\n'
        svp+='NO_OF_DAYS=\t'+ str(days)+'\n'

        svp+='\n---------------------------------------\n'
        svp+='\n---------------------------------------\n'
        svp+='AMOUNT_TO_PAY=\t\t' + str(amount)

        print(svp)
        f=open('receipt.txt','w')
        f.write(svp)
        f.close()
        from fpdf import FPDF
        pdf=FPDF()
        pdf.add_page()
        pdf.set_font('arial','B',size=15)

        f=open('receipt.txt','r')

        for i in f: 
            pdf.cell(10,20,txt=i,ln=1,align='L')

        pdf.output('costumer_receipt.pdf')

        yag=yagmail.SMTP('jainananya355@gmail.com','@#jainananya')
        print(svp)
        yag.send(to=b[3], subject='KINDELY CHECK YOUR RECEIPT', contents=svp)

        
    else:
        print('NO SUCH NAMED COSTUMER.....')
