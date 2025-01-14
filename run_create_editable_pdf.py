import os.path

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5, A7
from reportlab.lib import colors  # Import the colors module
from reportlab.lib.colors import Color
from reportlab.pdfbase.acroform import AcroForm


def create_editable_pdf(output_file: str, background_image: str, debug: bool = False):
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))

    # Create a canvas object with A5 page size
    c = canvas.Canvas(output_file, pagesize=A7)
    width, height = A7
    # width, height = (298.08, 206.64)

    if background_image:
        # Add a background image
        c.drawImage(background_image, 0, 0, width=width, height=height)

    # Create an AcroForm object
    form = c.acroForm

    D_info_spacing = 16
    # Set fillColor to 100% transparent using RGBA (R, G, B, A)
    transparent_color = Color(0, 0, 0, 0)  # Black color with 100% transparency (Alpha = 0)
    font_size = 7

    if debug:
        border_color = colors.blue
        border_width = 0.5
    else:
        border_color = transparent_color
        border_width = 0

    # Draw the text on the canvas
    # c.setFont("Helvetica", 8)
    # c.setFillColor(colors.black)  # Set the text color
    # c.drawString(45, height - 32, "D1.")  # Coordinates
    # c.drawString(45, height - 32 - D_info_spacing, "D2.")  # Coordinates
    # c.drawString(45, height - 32 - D_info_spacing * 2, "D3.")  # Coordinates

    # Add editable text D1_car_info field
    form.textfield(
        name="D1_car_info",
        tooltip="Enter car information",
        x=45,
        y=height - 40,
        width=120,
        height=16,
        value="D1. BBB",  # Default selected value
        textColor=colors.black,  # Use colors.black instead of "black"
        borderColor=border_color,
        fillColor=transparent_color,
        borderWidth=border_width,
        fontName="Helvetica",
        fontSize=font_size,
    )
    form.textfield(
        name="D2_car_info",
        tooltip="Enter car information",
        x=45,
        y=height - 40 - D_info_spacing,
        width=120,
        height=16,
        value="D2. SAMOCHÓD OSOBOWY",  # Default selected value
        textColor=colors.black,  # Use colors.black instead of "black"
        borderColor=border_color,
        fillColor=transparent_color,
        borderWidth=border_width,
        fontName="Helvetica",
        fontSize=font_size,
    )
    form.textfield(
        name="D3_car_info",
        tooltip="Enter car information",
        x=45,
        y=height - 40 - D_info_spacing * 2,
        width=120,
        height=16,
        value="D3. SSS SS",  # Default selected value
        textColor=colors.black,  # Use colors.black instead of "black"
        borderColor=border_color,
        fillColor=transparent_color,
        borderWidth=border_width,
        fontName="Helvetica",
        fontSize=font_size,
    )

    # Add an editable text field E_vin with a maximum length of 17 characters
    form.textfield(
        name="E_vin",
        tooltip="Enter VIN (max 17 characters)",
        x=65,
        y=height - 118,
        width=90,
        height=16,
        value="12345678912345678",  # Default selected value
        textColor=colors.black,  # Use colors.black instead of "black"
        borderColor=border_color,
        fillColor=transparent_color,
        borderWidth=border_width,
        fontName="Helvetica",
        fontSize=font_size,
        maxlen=17  # Set the maximum character length
    )

    # Add editable text F1_weight_field field
    form.textfield(
        name="F1_weight_field",
        tooltip="Enter weight KG",
        x=35,
        y=height - 139,
        width=30,
        height=16,
        value="1807",  # Default empty value
        textColor=colors.black,
        borderColor=border_color,  # No visible border color
        fillColor=transparent_color,
        borderWidth=border_width,  # No visible border width
        # forceBorder=True,  # Forces the border to be drawn, even if it's invisible
        fontName="Helvetica",
        fontSize=font_size,
        maxlen=7  # Limiting to 10 characters (for YYYY-MM-DD format)
    )
    # Add editable text F2_gross_weight_field field
    form.textfield(
        name="F2_gross_weight_field",
        tooltip="Enter Gross Weight KG",
        x=100,
        y=height - 139,
        width=30,
        height=16,
        value="2217",  # Default empty value
        textColor=colors.black,
        borderColor=border_color,  # No visible border color
        fillColor=transparent_color,
        borderWidth=border_width,  # No visible border width
        # forceBorder=True,  # Forces the border to be drawn, even if it's invisible
        fontName="Helvetica",
        fontSize=font_size,
        maxlen=7  # Limiting to 10 characters (for YYYY-MM-DD format)
    )
    # Add editable text F3_field field
    form.textfield(
        name="F3_field",
        tooltip="Enter F3",
        x=165,
        y=height - 139,
        width=30,
        height=16,
        value="---",  # Default empty value
        textColor=colors.black,
        borderColor=border_color,  # No visible border color
        fillColor=transparent_color,
        borderWidth=border_width,  # No visible border width
        # forceBorder=True,  # Forces the border to be drawn, even if it's invisible
        fontName="Helvetica",
        fontSize=font_size,
        maxlen=7  # Limiting to 10 characters (for YYYY-MM-DD format)
    )

    # Add editable text G_field field
    form.textfield(
        name="G_field",
        tooltip="Enter G",
        x=60,
        y=height - 161,
        width=30,
        height=16,
        value="---",  # Default empty value
        textColor=colors.black,
        borderColor=border_color,  # No visible border color
        fillColor=transparent_color,
        borderWidth=border_width,  # No visible border width
        # forceBorder=True,  # Forces the border to be drawn, even if it's invisible
        fontName="Helvetica",
        fontSize=font_size,
        maxlen=7  # Limiting to 10 characters (for YYYY-MM-DD format)
    )
    # Add editable text L_field field
    form.textfield(
        name="L_field",
        tooltip="Enter L",
        x=150,
        y=height - 161,
        width=30,
        height=16,
        value="---",  # Default empty value
        textColor=colors.black,
        borderColor=border_color,  # No visible border color
        fillColor=transparent_color,
        borderWidth=border_width,  # No visible border width
        # forceBorder=True,  # Forces the border to be drawn, even if it's invisible
        fontName="Helvetica",
        fontSize=font_size,
        maxlen=7  # Limiting to 10 characters (for YYYY-MM-DD format)
    )

    # Add editable text P1_field field
    form.textfield(
        name="P1_field",
        tooltip="Enter P1",
        x=60,
        y=height - 181,
        width=30,
        height=16,
        value="---",  # Default empty value
        textColor=colors.black,
        borderColor=border_color,  # No visible border color
        fillColor=transparent_color,
        borderWidth=border_width,  # No visible border width
        # forceBorder=True,  # Forces the border to be drawn, even if it's invisible
        fontName="Helvetica",
        fontSize=font_size,
        maxlen=7  # Limiting to 10 characters (for YYYY-MM-DD format)
    )
    # Add editable text P2_field field
    form.textfield(
        name="P2_field",
        tooltip="Enter P2",
        x=150,
        y=height - 181,
        width=30,
        height=16,
        value="KW",  # Default empty value
        textColor=colors.black,
        borderColor=border_color,  # No visible border color
        fillColor=transparent_color,
        borderWidth=border_width,  # No visible border width
        # forceBorder=True,  # Forces the border to be drawn, even if it's invisible
        fontName="Helvetica",
        fontSize=font_size,
        maxlen=7  # Limiting to 10 characters (for YYYY-MM-DD format)
    )
    # Add choice field P3_select_car_type
    form.choice(
        name="P3_select_car_type",
        tooltip="Choose an option",
        x=27,
        y=height - 201,
        width=65,
        height=16,
        options=["---", "Elektryczny", "Hybrydowy", "Hybryda plug-in"],  # The options for the drop-down
        value="---",  # Default selected value
        textColor=colors.black,
        borderColor=border_color,
        fillColor=transparent_color,
        borderWidth=border_width,
        fontSize=font_size,
    )
    # Add editable text S1_select_number_of_seats field
    form.choice(
        name="S1_select_number_of_seats",
        tooltip="Choose an number_of_seats",
        x=115,
        y=height - 201,
        width=25,
        height=16,
        options=["---", "2", "3", "5", "6", "7", "8", "9", "10"],  # The options for the drop-down
        value="---",  # Default selected value
        textColor=colors.black,
        borderColor=border_color,
        fillColor=transparent_color,
        borderWidth=border_width,
        fontSize=font_size,
    )
    # Add editable text S2_field field
    form.textfield(
        name="S2_field",
        tooltip="Enter S2_field",
        x=170,
        y=height - 201,
        width=25,
        height=16,
        value="---",  # Default empty value
        textColor=colors.black,
        borderColor=border_color,  # No visible border color
        fillColor=transparent_color,
        borderWidth=border_width,  # No visible border width
        # forceBorder=True,  # Forces the border to be drawn, even if it's invisible
        fontName="Helvetica",
        fontSize=font_size,
        maxlen=7  # Limiting to 10 characters (for YYYY-MM-DD format)
    )

    form.textfield(
        name="H_start_date_field",
        tooltip="Enter Start Date (YYYY-MM-DD)",
        x=27,
        y=height - 227,
        width=57,
        height=16,
        value="2025-00-00",  # Default empty value
        textColor=colors.black,
        borderColor=border_color,  # No visible border color
        fillColor=transparent_color,
        borderWidth=border_width,  # No visible border width
        # forceBorder=True,  # Forces the border to be drawn, even if it's invisible
        fontName="Helvetica",
        fontSize=font_size,
        maxlen=10  # Limiting to 10 characters (for YYYY-MM-DD format)
    )
    form.textfield(
        name="I_end_date_field",
        tooltip="Enter End Date (YYYY-MM-DD)",
        x=27,
        y=height - 252,
        width=57,
        height=16,
        value="2025-00-00",  # Default empty value
        textColor=colors.black,
        borderColor=border_color,  # No visible border color
        fillColor=transparent_color,
        borderWidth=border_width,  # No visible border width
        # forceBorder=True,  # Forces the border to be drawn, even if it's invisible
        fontName="Helvetica",
        fontSize=font_size,
        maxlen=10  # Limiting to 10 characters (for YYYY-MM-DD format)
    )

    # Finalize the PDF
    c.showPage()
    c.save()

    print("Creation finished")


if __name__ == "__main__":
    # Specify output file and background image

    output_file = "results_editable/dowod_editable_with_bg.pdf"
    bg_file = "assets_dowod/Template_dowod_back.png"  # Replace with your background image file
    # Create the editable PDF with BG
    create_editable_pdf(
        output_file=output_file,
        background_image=bg_file,
        debug=False
    )

    output_file = "results_editable/dowod_editable_NoBG.pdf"
    bg_file = None
    # Create the editable PDF no BG
    create_editable_pdf(
        output_file=output_file,
        background_image=bg_file,
        debug=False
    )
