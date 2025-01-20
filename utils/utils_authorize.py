from docx import Document
from abc import ABC
from auto_classes.auto_class import AbstractInfo


def fill_template(template_document: Document, data: AbstractInfo, make_bold: bool = False):
    """
    Fill placeholders in a DOCX template.

    Args:
        template_document (Document): The template DOCX object.
        data (DataClassType): Object with a `to_placeholder_mapping` method that returns a dictionary.
        make_bold (bool): If True, make placeholders bold. Defaults to False.
    """
    data_mapping_dict = data.to_placeholder_mapping()

    # Replace placeholders
    for paragraph in template_document.paragraphs:
        for key, value in data_mapping_dict.items():
            if key in paragraph.text:
                if not isinstance(value, str):
                    value = str(value)

                # paragraph.text = paragraph.text.replace(key, value)

                # Find the run containing the placeholder
                for run in paragraph.runs:
                    if key in run.text:
                        # Replace the placeholder
                        run.text = run.text.replace(key, value)
                        # Apply bold if needed
                        if make_bold:
                            run.bold = True
                        break  # Exit after replacing the key
    return template_document
