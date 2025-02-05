import os.path

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5, A7
from reportlab.lib import colors  # Import the colors module
from reportlab.lib.colors import Color
from reportlab.pdfbase.acroform import AcroForm


def create_editable_pdf(output_file: str, background_image: str, same_information_for_all_pages: bool = False, debug: bool = False):
    list_car_type_options = ["------", "Elektryczny", "Hybrydowy", "Hybryda plug-in", "Benzyna", "Diesel"]

    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))

    # Create a canvas object with A5 page size
    c = canvas.Canvas(output_file, pagesize=A7)
    # width, height = (298.08, 206.64)
    width, height = A7

    # Create an AcroForm object
    form = c.acroForm

    # Set fillColor to 100% transparent using RGBA (R, G, B, A)
    transparent_color = Color(0, 0, 0, 0)  # Black color with 100% transparency (Alpha = 0)
    font_size = 8.5

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

    for index, car_type in enumerate(list_car_type_options):
        if background_image:
            # Add a background image
            c.drawImage(background_image, 0, 0, width=width, height=height)

        # Add editable text D1_car_info field
        D_info_height_spacing = 16
        D_info_height_substraction_base = 55
        form.textfield(
            name="D1_car_info" if same_information_for_all_pages else f"D1_car_info_page{index}",
            tooltip="Enter car information",
            x=45,
            y=height - D_info_height_substraction_base,
            width=125,
            height=16,
            value="D1. BBA",  # Default selected value
            textColor=colors.black,  # Use colors.black instead of "black"
            borderColor=border_color,
            fillColor=transparent_color,
            borderWidth=border_width,
            fontName="Helvetica",
            fontSize=font_size,
        )
        form.textfield(
            name="D2_car_info" if same_information_for_all_pages else f"D2_car_info_page{index}",
            tooltip="Enter car information",
            x=45,
            y=height - D_info_height_substraction_base - D_info_height_spacing,
            width=125,
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
            name="D3_car_info" if same_information_for_all_pages else f"D3_car_info_page{index}",
            tooltip="Enter car information",
            x=45,
            y=height - D_info_height_substraction_base - D_info_height_spacing * 2,
            width=125,
            height=16,
            value="D3. SEAL U",  # Default selected value
            textColor=colors.black,  # Use colors.black instead of "black"
            borderColor=border_color,
            fillColor=transparent_color,
            borderWidth=border_width,
            fontName="Helvetica",
            fontSize=font_size,
        )

        # Add an editable text field E_vin with a maximum length of 17 characters
        E_vin_height_substraction_base = 130
        form.textfield(
            name="E_vin" if same_information_for_all_pages else f"E_vin_page{index}",
            tooltip="Enter VIN (max 17 characters)",
            x=65,
            y=height - E_vin_height_substraction_base,
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
        F1_height_substraction_base = 152
        form.textfield(
            name="F1_weight_field" if same_information_for_all_pages else f"F1_weight_field_page{index}",
            tooltip="Enter weight KG",
            x=35,
            y=height - F1_height_substraction_base,
            width=30,
            height=16,
            value="1800",  # Default empty value
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
            name="F2_gross_weight_field" if same_information_for_all_pages else f"F2_gross_weight_field_page{index}",
            tooltip="Enter Gross Weight KG",
            x=100,
            y=height - F1_height_substraction_base,
            width=30,
            height=16,
            value="2000",  # Default empty value
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
            name="F3_field" if same_information_for_all_pages else f"F3_field_page{index}",
            tooltip="Enter F3",
            x=165,
            y=height - F1_height_substraction_base,
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
        GL_field_height_substraction_base = 175
        form.textfield(
            name="G_field" if same_information_for_all_pages else f"G_field_page{index}",
            tooltip="Enter G",
            x=60,
            y=height - GL_field_height_substraction_base,
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
            name="L_field" if same_information_for_all_pages else f"L_field_page{index}",
            tooltip="Enter L",
            x=150,
            y=height - GL_field_height_substraction_base,
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
        P1_P2_height_substraction_base = 194
        form.textfield(
            name="P1_field" if same_information_for_all_pages else f"P1_field_page{index}",
            tooltip="Enter P1",
            x=60,
            y=height - P1_P2_height_substraction_base,
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
            name="P2_field" if same_information_for_all_pages else f"P2_field_page{index}",
            tooltip="Enter P2",
            x=145,
            y=height - P1_P2_height_substraction_base,
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
        P3_S1_S2_field_height_substraction_base = 214
        form.textfield(
            name="P3_select_car_type" if same_information_for_all_pages else f"P3_select_car_type_page{index}",
            tooltip="Choose an option",
            x=27,
            y=height - P3_S1_S2_field_height_substraction_base,
            width=65,
            height=16,
            value=car_type,  # Default car_type value
            textColor=colors.black,
            borderColor=border_color,
            fillColor=transparent_color,
            borderWidth=border_width,
            fontSize=font_size,
        )
        # Add editable text S1_select_number_of_seats field
        form.textfield(
            name="S1_select_number_of_seats" if same_information_for_all_pages else f"S1_select_number_of_seats_page{index}",
            tooltip="Choose an number_of_seats",
            x=115,
            y=height - P3_S1_S2_field_height_substraction_base,
            width=25,
            height=16,
            # options=["---", "2", "3", "5", "6", "7", "8", "9", "10"],  # The options for the drop-down
            value="5",  # Default selected value
            textColor=colors.black,
            borderColor=border_color,
            fillColor=transparent_color,
            borderWidth=border_width,
            fontSize=font_size,
        )
        # Add editable text S2_field field
        form.textfield(
            name="S2_field" if same_information_for_all_pages else f"S2_field_page{index}",
            tooltip="Enter S2_field",
            x=170,
            y=height - P3_S1_S2_field_height_substraction_base,
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

        # Add editable text H_start_date_field
        H_field_height_substraction_base = 240
        form.textfield(
            name=f"H_start_date_field_page{index}",
            tooltip="Enter Start Date (YYYY-MM-DD)",
            x=27,
            y=height - H_field_height_substraction_base,
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
        # Add editable text I_end_date_field
        I_field_height_substraction_base = 265
        form.textfield(
            name=f"I_end_date_field_page{index}",
            tooltip="Enter End Date (YYYY-MM-DD)",
            x=27,
            y=height - I_field_height_substraction_base,
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

        # Finish the current page and move to the next one
        c.showPage()
        print(f"Page [{index + 1}|{len(list_car_type_options)}] with car type [{car_type}] finished...")

    # Finalize the PDF
    c.save()
    print("### Creation finished ###")


if __name__ == "__main__":
    # Specify output file and background image

    DEBUG = False
    SAME_INFO_ALL_PAGES = True # except date

    output_file = "results_editable/Dowod_editable_with_bg.pdf"
    bg_file = "assets_dowod/Template_dowod_sample_back_printed_red.png"  # Replace with your background image file
    # Create the editable PDF with BG
    create_editable_pdf(
        output_file=output_file,
        background_image=bg_file,
        same_information_for_all_pages=SAME_INFO_ALL_PAGES,
        debug=DEBUG
    )

    output_file = "results_editable/Dowod_editable_NoBG_SAME.pdf"
    bg_file = None
    # Create the editable PDF no BG
    create_editable_pdf(
        output_file=output_file,
        background_image=bg_file,
        same_information_for_all_pages=SAME_INFO_ALL_PAGES,
        debug=DEBUG
    )

    SAME_INFO_ALL_PAGES = False
    output_file = "results_editable/Dowod_editable_NoBG_allDIFF.pdf"
    bg_file = None
    # Create the editable PDF no BG
    create_editable_pdf(
        output_file=output_file,
        background_image=bg_file,
        same_information_for_all_pages=SAME_INFO_ALL_PAGES,
        debug=DEBUG
    )