import os.path
from typing import Optional
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfReader, PdfWriter, PdfReader
from auto_classes.auto_class import AbstractInfo


def fill_template(template_document: Document, data: AbstractInfo, make_bold: bool = False):
    """
    Fill placeholders in a DOCX template.

    Args:
        template_document (Document): The template DOCX object.
        data (DataClassType): Object with a `to_placeholder_mapping` method that returns a dictionary.
        make_bold (bool): If True, make placeholders bold. Defaults to False.
    """
    data_mapping_dict = data.to_placeholder_mapping()

    # Replace placeholders
    for paragraph in template_document.paragraphs:
        for key, value in data_mapping_dict.items():
            if key in paragraph.text:
                if not isinstance(value, str):
                    value = str(value)

                # paragraph.text = paragraph.text.replace(key, value)

                # Find the run containing the placeholder
                for run in paragraph.runs:
                    if key in run.text:
                        # Replace the placeholder
                        run.text = run.text.replace(key, value)
                        # Apply bold if needed
                        if make_bold:
                            run.bold = True
                        break  # Exit after replacing the key
    return template_document


def create_watermark_pdf(watermark_file: str, watermark_text: str, rotation_angle=135, font_size=60):
    """
    Creates a watermark PDF with the specified text and rotation angle.
    """
    if os.path.exists(watermark_file):
        print(f"{watermark_file} already exists, skipping.")
        return None

    a4_width, a4_height = A4  # A4 size in points
    target_width = 4 / 5 * a4_width  # Two-thirds of the A4 width

    c = canvas.Canvas(watermark_file, pagesize=A4)  # A4 size (points)
    c.setFont("Helvetica", font_size)

    # Adjust font size to meet width requirement
    watermark_width = c.stringWidth(watermark_text, "Helvetica", font_size)
    while watermark_width < target_width:
        font_size += 5  # Increment font size
        c.setFont("Helvetica", font_size)
        watermark_width = c.stringWidth(watermark_text, "Helvetica", font_size)

    print(f"Final font size: {font_size}")
    print(f"Watermark dimensions: Width = {watermark_width}, Height = {font_size}")

    # c.setFillGray(0.9, 0.9)  # Set transparency (gray scale)
    # Set transparency using a blend of colors
    c.setFillAlpha(0.15)  # Set transparency level (0 = fully transparent, 1 = fully opaque)

    # Positions for the watermarks (Y-coordinates for upper, center, and bottom)
    positions = [480, 300, 150]  # Adjust values as needed for your layout
    # positions = [350, 150]  # Adjust values as needed for your layout

    for y in positions:
        c.saveState()  # Save the canvas state before transformations
        c.translate(180, y)  # Set the position for the current watermark
        c.rotate(rotation_angle)  # Rotate text counterclockwise
        c.drawString(-150, 0, watermark_text)  # Draw the watermark text
        c.restoreState()  # Restore the canvas state to avoid affecting other elements

    c.save()


def add_watermark_to_pdf(input_pdf: str, output_pdf: str, watermark_file: str, delete_input_pdf: Optional[bool]=True):
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

    if delete_input_pdf:
        try:
            os.remove(input_pdf)
            print(f"Removed: {input_pdf}")
        except OSError as e:
            print(f"Error deleting file {input_pdf}: {e}")
