import fpdf

document = fpdf.FPDF()

document.set_font('Times', 'B', 14)
document.set_text_color(19, 83, 173)
document.add_page()

document.cell(0,5,'Testowy dokument')
document.ln()
document.set_font('Times', '', 12)
document.set_text_color(0)
document.multi_cell(0,5, 'Lorem ipsum dolor sit amet, '
                         'consectetur adipiscing elit.'* 20)
document.output('raport.pdf')



