import cv2
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
