import fpdf

pdf = fpdf.FPDF(orientation='p', unit='mm', format= 'A4')
pdf.add_page()
pdf.set_font(family='Times', style='B', size= 12)
pdf.cell(w=0, h=12,txt='Hi there', ln=1, border=1,align='L')

pdf.output('MyPDF.pdf')