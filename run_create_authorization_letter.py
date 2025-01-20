import os
from tqdm import tqdm

from utils.utils_io import load_config, check_create_save_directory, save_docx, remove_files_from_dir
from utils.utils_authorize import fill_template, create_watermark_pdf, add_watermark_to_pdf
from utils.utils import convert_docx_to_pdf_and_cleanup
from auto_classes.authorization_info_class import CompanyInfo, DriverInfo
from auto_classes.dowod_info_instances import CarInfo
from docx import Document


def main(
        company_list: list,
        config_comapny_file: str,
        config_car_driver_file: str,
        doc_template_file: str,
):
    all_company_info = load_config(config_file=config_comapny_file)
    car_driver_info = load_config(config_file=config_car_driver_file)
    selected_company_info = {
        key: value for key, value in all_company_info.items() if key in company_list
    }
    driver_instance = DriverInfo(*car_driver_info['driver'].values())
    car_instance = CarInfo(*car_driver_info['car_info'].values())
    company_instances = [
        CompanyInfo(*selected_company_info[comp_name].values()) for comp_name in selected_company_info.keys()
    ]

    save_dir = "results_author"
    for idx, company in enumerate(tqdm(company_instances)):
        # Load the document
        res_doc = Document(doc_template_file)
        res_doc = fill_template(
            template_document=res_doc,
            data=driver_instance
        )
        res_doc = fill_template(
            template_document=res_doc, data=company,
            make_bold=True,
        )
        res_doc = fill_template(
            template_document=res_doc,
            data=car_instance
        )

        temp_save_docx_file = f"{save_dir}/output_{company.company_name}.docx"
        temp_save_pdf_file = temp_save_docx_file.replace('.docx', '.pdf')

        save_pdf_file_final = f"{save_dir}/doc_{company.company_name}.pdf"
        watermark_pdf = f"{save_dir}/watermark_{company.company_name}.pdf"

        check_create_save_directory(save_directory=save_dir)
        # Save the modified document
        save_docx(
            docx_obj=res_doc,
            docx_save_file=temp_save_docx_file,
        )
        # convert docx file to pdf file
        convert_docx_to_pdf_and_cleanup(
            docx_file=temp_save_docx_file,
            output_dir=save_dir,
        )
        # create watermark pdf
        create_watermark_pdf(watermark_file=watermark_pdf, watermark_text=company.company_name, rotation_angle=45)
        # Add watermark to doc pdf
        add_watermark_to_pdf(
            input_pdf=temp_save_pdf_file,
            output_pdf=save_pdf_file_final,
            watermark_file=watermark_pdf,
        )

    remove_files_from_dir(directory=save_dir, extension='.pdf', keywords='watermark_')


if __name__ == '__main__':
    companies = [
        "amuatu",
        "toyar",
        "frano",
        "lsy",
        "commercia",
        "peony",
    ]
    doc_template_file = "assets_doc/Template_Authorization_Letter.docx"
    main(
        company_list=companies,
        config_comapny_file="auto_info_config/config_company.yml",
        config_car_driver_file="auto_info_config/config_car_driver.yml",
        doc_template_file=doc_template_file,
    )
