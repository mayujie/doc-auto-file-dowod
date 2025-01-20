from utils.utils_authorize import create_watermark_pdf, add_watermark_to_pdf

# Usage
input_pdf = "assets_doc/W2200P31 Baigale Authorization Letter.pdf"
# input_pdf = "results_author/output_AMUATU Sp. z o.o..pdf"

output_pdf = "results_author/output_with_watermark.pdf"
watermark_file = "results_author/watermark.pdf"

# watermark_text = "AMUATU Sp. z o.o."
# watermark_text = "Toyar Sp. z o.o."
# watermark_text = "FRANO Sp. z o.o."
# watermark_text = "LSY Sp. z o.o."
watermark_text = "COMMERCIA Sp. z o.o."
# watermark_text = "PEONY.EUR Sp. z o.o."


# Create the watermark and add it to the input PDF
create_watermark_pdf(
    watermark_file=watermark_file,
    watermark_text=watermark_text,
    rotation_angle=45,
)
add_watermark_to_pdf(
    input_pdf=input_pdf,
    output_pdf=output_pdf,
    watermark_file=watermark_file,
)
