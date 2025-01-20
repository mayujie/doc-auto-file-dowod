import cv2
import os
import subprocess
from typing import Union, Tuple


def show_image_with_scale(
        org_img,
        winname: str,
        scale_factor: Union[float, int] = 1
):
    if scale_factor != 1:
        # Define the scaling factor (e.g., resize to half of the original size)
        scale_factor = 0.5  # Change this value to adjust the resize scale

        # Calculate the new dimensions based on the scaling factor
        new_width = int(org_img.shape[1] * scale_factor)
        new_height = int(org_img.shape[0] * scale_factor)

        # Resize the image using cv2.resize()
        image = cv2.resize(org_img, (new_width, new_height))
    else:
        image = org_img

    cv2.imshow(mat=image, winname=winname)
    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def convert_docx_to_pdf_and_cleanup(docx_file, output_dir):
    """
    Converts a .docx file to a .pdf using LibreOffice, then removes the .docx file.

    Parameters:
    - docx_file: Path to the .docx file.
    - output_dir: Directory to save the output PDF.
    """
    if not docx_file.endswith(".docx"):
        raise ValueError(f"Invalid file format. {docx_file} Use '.docx'.")

    # Run LibreOffice conversion to convert .docx to .pdf
    subprocess.run(
        [
            "libreoffice",
            "--headless",  # Run in headless mode (no GUI)
            "--convert-to", "pdf",  # Specify output format
            docx_file,
            "--outdir", output_dir,  # Output directory
        ],
        check=True
    )
    print(f"PDF saved in {output_dir}")

    # Remove the .docx file
    try:
        os.remove(docx_file)
        print(f"Removed: {docx_file}")
    except OSError as e:
        print(f"Error deleting file {docx_file}: {e}")
