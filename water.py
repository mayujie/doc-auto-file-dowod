from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter, PdfReader


def create_watermark(watermark_file, watermark_text, rotation_angle=135):
    """
    Creates a watermark PDF with the specified text and rotation angle.
    """
    c = canvas.Canvas(watermark_file, pagesize=(595.27, 841.89))  # A4 size (points)
    c.setFont("Helvetica", 60)

    # c.setFillGray(0.9, 0.9)  # Set transparency (gray scale)
    # Set transparency using a blend of colors
    c.setFillAlpha(0.2)  # Set transparency level (0 = fully transparent, 1 = fully opaque)


    # Positions for the watermarks (Y-coordinates for upper, center, and bottom)
    positions = [480, 300, 150]  # Adjust values as needed for your layout

    for y in positions:
        c.saveState()  # Save the canvas state before transformations
        c.translate(180, y)  # Set the position for the current watermark
        c.rotate(rotation_angle)  # Rotate text counterclockwise
        c.drawString(-150, 0, watermark_text)  # Draw the watermark text
        c.restoreState()  # Restore the canvas state to avoid affecting other elements

    c.save()


def add_watermark_to_pdf(input_pdf, output_pdf, watermark_file):
    """
    Adds the watermark to each page of the input PDF and saves the output PDF.
    """
    # Read the input PDF and the watermark PDF
    pdf_reader = PdfReader(input_pdf)
    watermark_reader = PdfReader(watermark_file)
    watermark_page = watermark_reader.pages[0]

    pdf_writer = PdfWriter()

    # Add the watermark to each page
    for page in pdf_reader.pages:
        page.merge_page(watermark_page)  # Merge the watermark onto the page
        pdf_writer.add_page(page)

    # Save the output PDF
    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)


# Usage
input_pdf = "assets_doc/W2200P31 Baigale Authorization Letter.pdf"
output_pdf = "assets_doc/output_with_watermark.pdf"
watermark_file = "assets_doc/watermark.pdf"
# watermark_text = "AMUATU Sp. z o.o."
# watermark_text = "Toyar Sp. z o.o."
# watermark_text = "FRANO Sp. z o.o."
# watermark_text = "LSY Sp. z o.o."
watermark_text = "COMMERCIA Sp. z o.o."
# watermark_text = "PEONY.EUR Sp. z o.o."


# Create the watermark and add it to the input PDF
create_watermark(watermark_file, watermark_text, rotation_angle=45)
add_watermark_to_pdf(input_pdf, output_pdf, watermark_file)
