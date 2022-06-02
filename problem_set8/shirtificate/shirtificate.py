from fpdf import FPDF
from PIL import Image

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# CS50 Shirtificate
pdf.set_font("Times", "B", size=64)
pdf.cell(0, 20, txt="CS50 Shirtificate", align="C")

# image
pdf.image("shirtificate.png", 0, 40, 210, 260)

# user name
pdf.ln()
pdf.set_font("Times", "B", size=32)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 170, txt=f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
