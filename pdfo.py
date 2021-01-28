from fpdf import FPDF
pdf=FPDF()
pdf.add_page()
pdf.set_font('arial','B',size=15)

f=open('receipt.txt','r')

for i in f:
    pdf.cell(10,20,txt=i,ln=1,align='L')

pdf.output('costumer_receipt.pdf')