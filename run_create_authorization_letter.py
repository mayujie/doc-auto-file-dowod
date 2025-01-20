import os
from tqdm import tqdm

from utils.utils_io import load_config, check_create_save_directory, save_docx
from utils.utils_authorize import fill_template
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

        save_dir = "results_author"
        save_docx_file = f"{save_dir}/output_{company.company_name}.docx"
        save_pdf_file_final = f"{save_dir}/doc_{company.company_name}.pdf"

        check_create_save_directory(save_directory=save_dir)
        # Save the modified document
        save_docx(
            docx_obj=res_doc,
            docx_save_file=save_docx_file,
        )
        # convert docx file to pdf file
        convert_docx_to_pdf_and_cleanup(
            docx_file=f"{save_dir}/output_{company.company_name}.docx",
            output_dir=save_dir,
        )


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
