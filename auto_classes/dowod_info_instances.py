#
# References:
# https://realpython.com/python-data-classes/
#
from typing import Optional, Dict, Tuple
from dataclasses import dataclass


class CONST_DOWOD_TYPE(object):
    FRONT_FILE_SUFFIX = "front"
    BACK_FILE_SUFFIX = "back"


@dataclass
class CarInfo:
    brand: str
    model: str
    vin_number: str
    start_date: str
    end_date: str
    plate_number: Optional[str] = None

    def get_section_d(self):
        section_d = f"D1. {self.brand}\nD2. ...\nD3. {self.model}"
        return section_d

    def to_placeholder_mapping(self) -> dict:
        return {
            "{{CAR_BRAND}}": self.brand,
            "{{CAR_MODEL}}": self.model,
            "{{CAR_VIN}}": self.vin_number,
            "{{CAR_PLATE_NUMBER}}": self.plate_number,
            "{{DATE_START}}": self.start_date,
            "{{DATE_END}}": self.end_date,
        }


@dataclass
class SectionInfo:
    value: str
    position: Tuple[int, int]


@dataclass
class RegistrationProofInfo:
    section_D: SectionInfo
    section_E: SectionInfo
    section_H: SectionInfo
    section_I: SectionInfo
