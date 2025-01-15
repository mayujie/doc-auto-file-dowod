#
# References:
# https://realpython.com/python-data-classes/
#
from typing import Optional, Dict, Tuple
from dataclasses import dataclass


@dataclass
class CompanyInfo:
    company_name: str
    company_address: str
    company_address_code_city: str
    company_nip_number: str
    company_regon_number: Optional[str] = None

    def to_placeholder_mapping(self) -> dict:
        return {
            "{{COMPANY_NAME}}": self.company_name,
            "{{COMPANY_ADDRESS}}": self.company_address,
            "{{COMPANY_ADDRESS_CODE_CITY}}": self.company_address_code_city,
            "{{COMPANY_NIP_NUMBER}}": self.company_nip_number,
            "{{COMPANY_REGON_NUMBER}}": self.company_regon_number,
        }


@dataclass
class DriverInfo:
    driver_name: str
    driver_license_number: str
    title: str
    gender: str

    def to_placeholder_mapping(self) -> dict:
        return {
            "{{DRIVER_NAME}}": self.driver_name,
            "{{DRIVER_LICENSE_NUMBER}}": self.driver_license_number,
            "{{TITLE}}": self.title,
            "{{GENDER}}": self.gender,
        }
