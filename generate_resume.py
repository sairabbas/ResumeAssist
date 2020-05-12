#you need to install the fpdf library
# run: pip install fpdf

from fpdf import FPDF

#def write_file():


def createPDF():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times','BI',11)
#   write file...
    contact = open("./user.txt","r")

    for a in contact:
       pdf.multi_cell(200,5, txt = a, align = 'C')
    contact.close()

    education = open('./education.txt','r')
    pdf.cell(200,5, txt = "Education", align = 'L')
    y = pdf.get_y()
    pdf.line(200,y+5,5,y+5)
    pdf.set_font('Times','',10)
    for b in education:
        pdf.multi_cell(200,5, txt = b, align = 'L')
    education.close()

    pdf.set_font('Times','BI',11)
    pdf.cell(200,5, txt = "Selected Independent Projects", align = 'L')
    y = pdf.get_y()
    pdf.line(200,y+5,5,y+5)
    projects = open('./project.txt', 'r')
    pdf.set_font('Times','',10)
    for c in projects:
       pdf.multi_cell(200,5,txt = c, align = 'L')
    projects.close()

    pdf.set_font('Times','BI',11)
    pdf.cell(200,5, txt = "Experience", align = 'L')
    y = pdf.get_y()
    pdf.line(200,y+5,5,y+5)
    experience = open('./work.txt', 'r')
    pdf.set_font('Times','',10)
    for d in experience:
        pdf.multi_cell(200,5,txt = d, align = 'L')
    experience.close()

    pdf.set_font('Times','BI',11)
    pdf.cell(200,5, txt = "Skills", align = 'L')
    y = pdf.get_y()
    pdf.line(200,y+5,5,y+5)
    skills = open('./skill.txt', "r")
    pdf.set_font('Times','',10)
    for e in skills:
        pdf.multi_cell(200,5,txt = e, align = 'L')
    skills.close()

    try:
        pdf.output("resume.pdf", "F")
        return "Success"
    except:
        return "Error"




createPDF()
