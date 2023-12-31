from fpdf import FPDF

class PDFDoc:
    def __init__(self):
        self.pdf = FPDF(orientation="P", format="A4")

    def create_pdf(self):
        self.pdf.add_page()

    def add_image(self):
        width = self.pdf.w
        height = self.pdf.h
        self.pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png",width/2 - 90, height/2 - 75, 180)
    
    def add_header(self):
        self.pdf.set_font("Arial", "", 40)
        self.pdf.cell(185, 60, "CS50 Shirtificate", align="C")
        

    def add_shirt_text(self):
        self.pdf.ln(10)
        self.pdf.set_text_color(250, 250, 250)
        self.pdf.set_font("Arial", "", 20)
        self.pdf.cell(0, 250, "Tushar Bhat took CS50", align="C")
        self.pdf.output("shirtificate.pdf")
    

def main():
    pdf = PDFDoc()
    pdf.create_pdf()
    pdf.add_image()
    pdf.add_header()
    pdf.add_shirt_text()

if __name__ == "__main__":
    main()