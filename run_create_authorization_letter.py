import os
from utils.utils_io import load_config
from auto_classes.authorization_info_class import CompanyInfo, DriverInfo
from auto_classes.dowod_info_instances import CarInfo
from docx import Document
from utils.utils_authorize import fill_template


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

    for idx, company in enumerate(company_instances):
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
        if not os.path.exists(save_dir):
            os.makedirs(save_dir, exist_ok=True)
        # Save the modified document
        res_doc.save(f"{save_dir}/output_{company.company_name}.docx")


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
