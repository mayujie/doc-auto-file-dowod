import os
import cv2
from tqdm import tqdm
from typing import Union, Tuple
from auto_classes.dowod_info_instances import CarInfo, RegistrationProofInfo, SectionInfo, CONST_DOWOD_TYPE


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


def make_dowod(
        image_template_path: str,
        unique_scale_factor: tuple,
        car_info: CarInfo,
        file_suffix: str,
        debug: bool,
):
    img = cv2.imread(image_template_path)
    img_size = img.shape[:2]

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.2
    font_thickness = 2
    # font_color = (0, 0, 0)
    font_color = (30, 30, 30)

    if file_suffix == CONST_DOWOD_TYPE.BACK_FILE_SUFFIX:
        registration_proof_info = RegistrationProofInfo(
            section_D=SectionInfo(
                value=car_info.get_section_d(),
                position=(img_size[1] // 4, img_size[0] // 6)
            ),
            section_E=SectionInfo(
                value=car_info.vin_number,
                position=(img_size[1] // unique_scale_factor[0], int(img_size[0] // unique_scale_factor[1]))
            ),
            section_H=SectionInfo(
                value=car_info.start_date,
                position=(img_size[1] // 6, 920)
            ),
            section_I=SectionInfo(
                value=car_info.end_date,
                position=(img_size[1] // 6, 1020)
            ),
        )
        for section_name, section_info in registration_proof_info.__dict__.items():
            if section_name == 'section_D':
                line_height = 40  # Height between lines
                # Split the text into lines
                lines = section_info.value.split('\n')
                # Write each line of text onto the image
                y_offset = section_info.position[1]  # Starting y-offset
                for line in lines:
                    cv2.putText(
                        img, line, (section_info.position[0], y_offset),
                        font, font_scale, font_color, font_thickness, cv2.LINE_AA
                    )
                    y_offset += line_height  # Move to the next line
            else:
                cv2.putText(
                    img, section_info.value, section_info.position,
                    font, font_scale, font_color, font_thickness, cv2.LINE_AA
                )
    elif file_suffix == CONST_DOWOD_TYPE.FRONT_FILE_SUFFIX:
        cv2.putText(
            img, car_info.plate_number, (img_size[1] // unique_scale_factor[0], int(img_size[0] // unique_scale_factor[1])),
            font, font_scale, font_color, font_thickness, cv2.LINE_AA
        )
    else:
        raise ValueError(f"Invalid file suffix: {file_suffix}")

    if debug:
        show_image_with_scale(org_img=img, winname=os.path.basename(image_template_path))
    else:
        save_dir = os.path.join(os.path.dirname(__file__), 'results_dowod')
        os.makedirs(save_dir, exist_ok=True)
        output_image_path = os.path.join(
            save_dir,
            f'{car_info.brand}_{car_info.model}_{car_info.vin_number}_{car_info.plate_number}_{file_suffix}.png'
        )
        cv2.imwrite(output_image_path, img)


if __name__ == '__main__':
    ROOT_DIR = os.path.dirname(__file__)
    IMG_FRONT_PATH = os.path.join(ROOT_DIR, "assets_dowod/Template_dowod_front.png")
    IMG_BACK_PATH = os.path.join(ROOT_DIR, "assets_dowod/Template_dowod_back_stamp.png")
    # IMG_BACK_PATH = os.path.join(ROOT_DIR, "assets_dowod/Template_dowod_back_stamp.png")
    DEBUG = False

    LIST_CARS = [
        # Tuple: (brand_name, model_name, VIN, plate_number, start_time, end_time)
        ('LYNK CO', 'CX 11', 'LS6C3E0M6RF830201', 'W3700P96', '2024-06-10', '2024-07-10'),
        ('Deepal', 'S07', 'LS6C3E0M8RF830202', 'W3700P97', '2024-05-13', '2024-07-12'),
        ('BYD', 'VDE', 'LS6C3E0MXRF830203', 'W3700P98', '2024-12-15', '2025-01-14'),
    ]

    car_instances = [
        CarInfo(
            brand=car_info[0],
            model=car_info[1],
            vin_number=car_info[2],
            plate_number=car_info[3],
            start_date=car_info[4],
            end_date=car_info[5],
        )
        for car_info in LIST_CARS
    ]
    for car in tqdm(car_instances):
        make_dowod(
            image_template_path=IMG_FRONT_PATH,
            car_info=car,
            unique_scale_factor=(6, 2.8),
            file_suffix=CONST_DOWOD_TYPE.FRONT_FILE_SUFFIX,
            debug=DEBUG
        )
        make_dowod(
            image_template_path=IMG_BACK_PATH,
            car_info=car,
            unique_scale_factor=(4, 2.7),
            file_suffix=CONST_DOWOD_TYPE.BACK_FILE_SUFFIX,
            debug=DEBUG
        )
