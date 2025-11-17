from test_data.apartment_test_data_messages import MESSAGES
from test_data.apartment_test_data_tools import (
    remove_apartment_data,
    get_apartment_data
)

UPLOAD_PLAN_FIELD_VALID_PARAMS = [
    (
        "Send file with 'jpg' extension",
        remove_apartment_data(key="plan_image"),
        "JPEG",
        "jpg"
    ),
    (
        "Send file with 'jpeg' extension",
        remove_apartment_data(key="plan_image"),
        "JPEG",
        "jpeg"
    ),
    (
        "Send file with 'png' extension",
        remove_apartment_data(key="plan_image"),
        "PNG",
        "png"
    ),
    (
        "Replace existing link",
        get_apartment_data(),
        "JPEG",
        "jpg"
    ),
]

UPLOAD_PLAN_FIELD_INVALID_PARAMS = [
    (
        "Send file with 'BMP' format",
        remove_apartment_data(key="plan_image"),
        "BMP",
        "bmp",
        MESSAGES["unsupported_file"]
    ),
    (
        "Send file with 'TIFF' format",
        remove_apartment_data(key="plan_image"),
        "TIFF",
        "tiff",
        MESSAGES["unsupported_file"]
    ),
    (
        "Send file with 'PDF' format",
        remove_apartment_data(key="plan_image"),
        "PDF",
        "pdf",
        MESSAGES["unsupported_file"]
    ),
    (
        "Send file with 'TXT' format",
        remove_apartment_data(key="plan_image"),
        "TXT",
        "txt",
        MESSAGES["unsupported_file"]
    ),
]
