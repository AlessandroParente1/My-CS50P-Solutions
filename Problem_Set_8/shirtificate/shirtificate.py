from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font("Helvetica", style="B", size=24)
        self.cell(0, 20, "CS50 Shirtificate", ln=True, align="C")
        self.ln(10)

    def create_shirtificate(self, name):
        self.add_page()
        self.image("shirtificate.png", x=25, y=60, w=160)
        self.set_font("Helvetica", style="B", size=20)
        self.set_text_color(255, 255, 255)
        self.set_xy(50, 130)
        self.cell(110, 10, f"{name} took CS50", align="C")

    def save_pdf(self, filename):
        self.output(filename)


def main():
    name = input("Name: ")
    pdf = Shirtificate(orientation="P", format="A4")
    pdf.create_shirtificate(name)
    pdf.save_pdf("shirtificate.pdf")


if __name__ == "__main__":
    main()
