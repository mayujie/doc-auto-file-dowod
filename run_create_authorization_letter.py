from utils.utils_io import load_config
from auto_classes.authorization_info_class import CompanyInfo, DriverInfo
from auto_classes.dowod_info_instances import CarInfo


def main(company_list: list, config_comapny_file: str, config_car_driver_file: str):
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
    print()


if __name__ == '__main__':
    companies = [
        "amuatu",
        "toyar",
        # "frano",
        # "lsy",
        # "commercia",
        # "peony",
    ]
    main(
        company_list=companies,
        config_comapny_file="auto_info_config/config_company.yml",
        config_car_driver_file="auto_info_config/config_car_driver.yml",
    )
