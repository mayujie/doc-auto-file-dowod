from utils.utils_authorize import create_watermark_pdf, add_watermark_to_pdf

# Usage
input_pdf = "assets_doc/Template_Authorization_Letter.pdf"
# input_pdf = "results_author/doc_AMUATU Sp. z o.o..pdf"

output_pdf = "results_author/output_with_watermark.pdf"

# watermark_text = "AMUATU Sp. z o.o."
# watermark_text = "Toyar Sp. z o.o."
# watermark_text = "FRANO Sp. z o.o."
# watermark_text = "LSY Sp. z o.o."
watermark_text = "COMMERCIA Sp. z o.o."
# watermark_text = "PEONY.EUR Sp. z o.o."

## @TODO pure text watermark
input_pdf = "assets_doc/A2_CNEU.pdf"
output_pdf = "results_author/A2_CNEU.pdf"
watermark_text = "CN.EU SOLUTION"

watermark_file = f"results_author/watermark_{watermark_text}.pdf"

# Create the watermark and add it to the input PDF
create_watermark_pdf(
    watermark_file=watermark_file,
    watermark_text=watermark_text,
    rotation_angle=45,
    num_watermarks=2,
    # num_watermarks=3,
)
add_watermark_to_pdf(
    input_pdf=input_pdf,
    output_pdf=output_pdf,
    watermark_file=watermark_file,
    delete_input_pdf=False,  # Keep the input PDF for further processing if needed
)
