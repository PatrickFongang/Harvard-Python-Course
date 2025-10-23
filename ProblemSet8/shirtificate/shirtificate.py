from fpdf import FPDF
def main():
    name = input("Name: ")
    pdf=FPDF()
    create_title(pdf)
    create_shirt(pdf,name)
    pdf.output("shirtificate.pdf")

def create_title(pdf):
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=45)
    pdf.cell(80)
    pdf.cell(30, 30, "CS50 Shirtificate", align="C")
    pdf.ln(50)

def create_shirt(pdf,name):
    img="https://cs50.harvard.edu/python/psets/8/shirtificate/shirtificate.png"
    width=180
    hight=160
    X=(210-width)/2
    pdf.image(img, x=X, w=width,h=hight)

    pdf.set_font("Helvetica", size=20)
    pdf.set_text_color(255,255,255)
    text=name.strip().title()+" took CS50"
    text_length=pdf.get_string_width(text)
    pdf.set_xy((210-text_length)/2,110)
    pdf.cell(20,30,text)

if __name__ == "__main__":
    main()
