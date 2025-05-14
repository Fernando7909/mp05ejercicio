from fpdf import FPDF

# Crear una instància de FPDF
pdf = FPDF()

# Afegir una pàgina
pdf.add_page()

# Configurar el tipus de lletra
pdf.set_font("Arial", size=12)

# Afegir un text
pdf.cell(200, 10, txt="Hola, aquest és un document PDF generat amb FPDF!", ln=True, align='C')

# Guardar el PDF
#pdf.output("document_bàsic.pdf")


class PDF(FPDF):
    # Afegir un encapçalament a cada pàgina
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Aquest és l\'encapçalament', 0, 1, 'C')

    # Afegir un peu de pàgina a cada pàgina
    def footer(self):
        self.set_y(-15)  # Posició 15mm des del final de la pàgina
        self.set_font('Arial', 'I', 8)
        # Número de pàgina
        self.cell(0, 10, f'Pàgina {self.page_no()}', 0, 0, 'C')


# Crear una instància del PDF personalitzat
pdf = PDF()

pdf.add_page()
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'Cos del document', 0, 1)

#pdf.output("document_encapcalament_peu.pdf")

data = [
    ["Producte", "Quantitat", "Preu"],
    ["Ordinador", "10", "500"],
    ["Teclat", "20", "20"],
    ["Ratoli", "50", "10"],
]

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 12)

# Capçaleres
for header in data[0]:
    pdf.cell(40, 10, header, 1)
pdf.ln()

# Files de la taula
pdf.set_font('Arial', '', 12)
for row in data[1:]:
    for item in row:
        pdf.cell(40, 10, item, 1)
    pdf.ln()

pdf.output("document_taula.pdf")

