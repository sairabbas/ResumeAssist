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

    for x in contact:
       pdf.multi_cell(200,5, txt = x, align = 'C')
    contact.close()

    education = open('./education.txt','r')
    pdf.cell(200,5, txt = "Education", align = 'L')
    pdf.set_font('Times','',10)
    for y in education:
        pdf.multi_cell(200,5, txt = y, align = 'L')
    education.close()

    pdf.set_font('Times','BI',11)
    pdf.cell(200,5, txt = "Selected Independent Projects", align = 'L')
    projects = open('./project.txt', 'r')
    pdf.set_font('Times','',10)
    for z in projects:
       pdf.multi_cell(200,5,txt = z, align = 'L')
    projects.close()

    pdf.set_font('Times','BI',11)
    pdf.cell(200,5, txt = "Experience", align = 'L')
    experience = open('./work.txt', 'r')
    pdf.set_font('Times','',10)
    for a in experience:
        pdf.multi_cell(200,5,txt = a, align = 'L')
    experience.close()

    pdf.set_font('Times','BI',11)
    pdf.cell(200,5, txt = "Skills", align = 'L')
    skills = open('./skill.txt', "r")
    pdf.set_font('Times','',10)
    for b in skills:
        pdf.multi_cell(200,5,txt = b, align = 'L')
    skills.close()

    pdf.output("resume.pdf", "F")


createPDF()
