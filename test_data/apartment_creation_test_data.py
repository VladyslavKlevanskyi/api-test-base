from test_data.apartment_test_data_messages import MESSAGES
from test_data.apartment_test_data_tools import (
    remove_apartment_data,
    replace_apartment_data
)

# =================VALID TEST DATA=======================

unit_type_field_valid_test_data = [
    (
        "No 'unit_type' field in payload",
        "unit_type",
        remove_apartment_data(key="unit_type"),
        None
    ),
    (
        "Send None into 'unit_type' field",
        "unit_type",
        replace_apartment_data(key="unit_type", value=None),
        None
    ),
    (
        "Send one char into 'unit_type' field",
        "unit_type",
        replace_apartment_data(key="unit_type", value="T"),
        "T"
    ),
    (
        "Send 25 char into 'unit_type' field",
        "unit_type",
        replace_apartment_data(key="unit_type", value="T" * 25),
        "T" * 25
    ),
    (
        "Send float into 'unit_type' field",
        "unit_type",
        replace_apartment_data(key="unit_type", value=10.1),
        "10.1"
    ),
    (
        "Send integer into 'unit_type' field",
        "unit_type",
        replace_apartment_data(key="unit_type", value=11),
        "11"
    ),
    (
        "Check strip spaces 'unit_type' field",
        "unit_type",
        replace_apartment_data(key="unit_type", value="  23.F "),
        "23.F"
    )
]

bedrooms_field_valid_test_data = [
    (
        "Send 0 to 'bedrooms' field in payload",
        "bedrooms",
        replace_apartment_data(key="bedrooms", value=0),
        0
    ),
    (
        "Send 9 to 'bedrooms' field in payload",
        "bedrooms",
        replace_apartment_data(key="bedrooms", value=9),
        9
    )
]

bathrooms_field_valid_test_data = [
    (
        "Send 1 to 'bathrooms' field in payload",
        "bathrooms",
        replace_apartment_data(key="bathrooms", value=1),
        1
    ),
    (
        "Send 9 to 'bathrooms' field in payload",
        "bathrooms",
        replace_apartment_data(key="bathrooms", value=9),
        9
    )
]

floor_field_valid_test_data = [
    (
        "Send -10 to 'floor' field in payload",
        "floor",
        replace_apartment_data(key="floor", value=-10),
        -10
    ),
    (
        "Send 999 to 'floor' field in payload",
        "floor",
        replace_apartment_data(key="floor", value=999),
        999
    )
]

area_field_valid_test_data = [
    (
        "Send 0 to 'area' field in payload",
        "area",
        replace_apartment_data(key="area", value=0),
        0
    ),
    (
        "Send 1.1 to 'area' field in payload",
        "area",
        replace_apartment_data(key="area", value=1.1),
        1.1
    )
]

price_field_valid_test_data = [
    (
        "No 'price' field in payload",
        "price",
        remove_apartment_data(key="price"),
        None
    ),
    (
        "Send None into 'price' field",
        "price",
        replace_apartment_data(key="price", value=None),
        None
    ),
    (
        "Send 1 to 'price' field in payload",
        "price",
        replace_apartment_data(key="price", value=1),
        1
    )
]

description_field_valid_test_data = [
    (
        "No 'description' field in payload",
        "description",
        remove_apartment_data(key="description"),
        None
    ),
    (
        "Send None into 'description' field",
        "description",
        replace_apartment_data(key="description", value=None),
        None
    ),
    (
        "Send one char into 'description' field",
        "description",
        replace_apartment_data(key="description", value="T"),
        "T"
    ),
    (
        "Send 255 char into 'description' field",
        "description",
        replace_apartment_data(key="description", value="T" * 255),
        "T" * 255
    ),
    (
        "Send float into 'description' field",
        "description",
        replace_apartment_data(key="description", value=10.1),
        "10.1"
    ),
    (
        "Send integer into 'description' field",
        "description",
        replace_apartment_data(key="description", value=11),
        "11"
    ),
    (
        "Send bool into 'description' field",
        "description",
        replace_apartment_data(key="description", value=False),
        "False"
    ),
    (
        "Check strip spaces 'description' field",
        "description",
        replace_apartment_data(key="description", value="  23.F "),
        "23.F"
    ),
    (
        "Check special symbols '.,\"( )-!?&%' into 'description' field",
        "description",
        replace_apartment_data(key="description", value=".,\"( )-!?&%"),  # noqa:  Q003
        ".,\"( )-!?&%"  # noqa:  Q003
    )
]

available_field_valid_test_data = [
    (
        "Send True into 'available' field",
        "available",
        replace_apartment_data(key="available", value=True),
        True
    ),
    (
        "Send False into 'available' field",
        "available",
        replace_apartment_data(key="available", value=False),
        False
    )
]

plan_image_field_valid_test_data = [
    (
        "No 'plan_image' field in payload",
        "plan_image",
        remove_apartment_data(key="plan_image"),
        None
    ),
    (
        "Send None into 'plan_image' field",
        "plan_image",
        replace_apartment_data(key="plan_image", value=None),
        None
    ),
    (
        "Send one char into 'plan_image' field",
        "plan_image",
        replace_apartment_data(key="plan_image", value="T"),
        "T"
    ),
    (
        "Send 255 char into 'plan_image' field",
        "plan_image",
        replace_apartment_data(key="plan_image", value="T" * 255),
        "T" * 255
    ),
    (
        "Send string '_.\\/-Qa0' into 'plan_image' field",
        "plan_image",
        replace_apartment_data(key="plan_image", value="_.\\/-Qa0"),
        "_.\\/-Qa0"
    )
]

angle_ids_field_valid_test_data = [
    (
        "No 'angle_ids' field in payload",
        "angle_ids",
        remove_apartment_data(key="angle_ids"),
        None
    ),
    (
        "Send None into 'angle_ids' field",
        "angle_ids",
        replace_apartment_data(key="angle_ids", value=None),
        None
    ),
]

images_field_valid_test_data = [
    (
        "No 'images' field in payload",
        "images",
        remove_apartment_data(key="images"),
        None
    ),
    (
        "Send None into 'images' field",
        "images",
        replace_apartment_data(key="images", value=None),
        None
    ),
    (
        "Send 1024 char into 'images' field",
        "images",
        replace_apartment_data(key="images", value="https://goog.ca/" * 64),
        ["https://goog.ca/" * 64]
    ),
    (
        "Send list of 20 URLs into 'images' field",
        "images",
        replace_apartment_data(key="images", value=[
            "https://google.ca/" for _ in range(20)
        ]
                               ),
        ["https://google.ca/" for _ in range(20)]
    ),
    (
        "Send list of 1 URL into 'images' field",
        "images",
        replace_apartment_data(key="images", value=["https://google.ca/"]),
        ["https://google.ca/"]
    ),
]

tour_field_valid_test_data = [
    (
        "No 'tour' field in payload",
        "tour",
        remove_apartment_data(key="tour"),
        None
    ),
    (
        "Send None into 'tour' field",
        "tour",
        replace_apartment_data(key="tour", value=None),
        None
    ),
    (
        "Send 1024 char URL into 'tour' field",
        "tour",
        replace_apartment_data(key="tour", value="https://goog.ca/" * 64),
        "https://goog.ca/" * 64
    ),
]

# =================INVALID TEST DATA=======================


unit_id_field_invalid_test_data = [
    (
        "No required 'unit_id' field",
        remove_apartment_data("unit_id"),
        ("unit_id", MESSAGES["field_required"])
    ),
    (
        "Send None to the 'unit_id' field",
        replace_apartment_data(key="unit_id", value=None),
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
    (
        "Send bool to the 'unit_id' field",
        replace_apartment_data(key="unit_id", value=True),
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
    (
        "Send string to the 'unit_id' field",
        replace_apartment_data(key="unit_id", value="string"),
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
    (
        "Send float to the 'unit_id' field",
        replace_apartment_data(key="unit_id", value=1.1),
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
    (
        "Negative value to 'unit_id' field",
        replace_apartment_data(key="unit_id", value=-1),
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
    (
        "Send 0 to 'unit_id' field",
        replace_apartment_data(key="unit_id", value=0),
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
    (
        "Send 1000 to 'unit_id' field",
        replace_apartment_data(key="unit_id", value=1000),
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
]

unit_type_field_invalid_test_data = [
    (
        "Send bool to the 'unit_type' field",
        replace_apartment_data(key="unit_type", value=True),
        ("unit_type", MESSAGES["unit_type_not_bool"])
    ),
    (
        "Send empty string to the 'unit_type' field",
        replace_apartment_data(key="unit_type", value=""),
        ("unit_type", MESSAGES["unit_type_not_empty"])
    ),
    (
        "Send spaces only to the 'unit_type' field",
        replace_apartment_data(key="unit_type", value="    "),
        ("unit_type", MESSAGES["unit_type_not_empty"])
    ),
    (
        "Send 26 chars to the 'unit_type' field",
        replace_apartment_data(key="unit_type", value="q" * 26),
        ("unit_type", MESSAGES["unit_type_all"])
    ),
    (
        "Send non latin chars to the 'unit_type' field",
        replace_apartment_data(key="unit_type", value="яЖбЮфΩδتشکगघ"),
        ("unit_type", MESSAGES["unit_type_all"])
    ),
    (
        "Send special chars to the 'unit_type' field",
        replace_apartment_data(
            key="unit_type",
            value="@#$!&?*%~`^\"\':;?,./|(){}[]<>"
        ),
        ("unit_type", MESSAGES["unit_type_all"])
    ),
]

bedrooms_field_invalid_test_data = [
    (
        "No required 'bedrooms' field",
        remove_apartment_data("bedrooms"),
        ("bedrooms", MESSAGES["field_required"])
    ),
    (
        "Send None to the 'bedrooms' field",
        replace_apartment_data(key="bedrooms", value=None),
        ("bedrooms", MESSAGES["bedrooms_val_err"])
    ),
    (
        "Send string to the 'bedrooms' field",
        replace_apartment_data(key="bedrooms", value="string"),
        ("bedrooms", MESSAGES["bedrooms_val_err"])
    ),
    (
        "Send bool to the 'bedrooms' field",
        replace_apartment_data(key="bedrooms", value=False),
        ("bedrooms", MESSAGES["bedrooms_val_err"])
    ),
    (
        "Send float to the 'bedrooms' field",
        replace_apartment_data(key="bedrooms", value=1.1),
        ("bedrooms", MESSAGES["bedrooms_val_err"])
    ),
    (
        "Negative value to 'bedrooms' field",
        replace_apartment_data(key="bedrooms", value=-1),
        ("bedrooms", MESSAGES["bedrooms_val_err"])
    ),
    (
        "Send 10 to 'bedrooms' field",
        replace_apartment_data(key="bedrooms", value=10),
        ("bedrooms", MESSAGES["bedrooms_val_err"])
    ),
]

bathrooms_field_invalid_test_data = [
    (
        "No required 'bathrooms' field",
        remove_apartment_data("bathrooms"),
        ("bathrooms", MESSAGES["field_required"])
    ),
    (
        "Send None to the 'bathrooms' field",
        replace_apartment_data(key="bathrooms", value=None),
        ("bathrooms", MESSAGES["bathrooms_val_err"])
    ),
    (
        "Send string to the 'bathrooms' field",
        replace_apartment_data(key="bathrooms", value="string"),
        ("bathrooms", MESSAGES["bathrooms_val_err"])
    ),
    (
        "Send bool to the 'bathrooms' field",
        replace_apartment_data(key="bathrooms", value=False),
        ("bathrooms", MESSAGES["bathrooms_val_err"])
    ),
    (
        "Send float to the 'bathrooms' field",
        replace_apartment_data(key="bathrooms", value=1.1),
        ("bathrooms", MESSAGES["bathrooms_val_err"])
    ),
    (
        "Send 0 to 'bathrooms' field",
        replace_apartment_data(key="bathrooms", value=0),
        ("bathrooms", MESSAGES["bathrooms_val_err"])
    ),
    (
        "Send 10 to 'bathrooms' field",
        replace_apartment_data(key="bathrooms", value=10),
        ("bathrooms", MESSAGES["bathrooms_val_err"])
    ),
]

floor_field_invalid_test_data = [
    (
        "No required 'floor' field",
        remove_apartment_data("floor"),
        ("floor", MESSAGES["field_required"])
    ),
    (
        "Send None to the 'floor' field",
        replace_apartment_data(key="floor", value=None),
        ("floor", MESSAGES["floor_val_err"])
    ),
    (
        "Send string to the 'floor' field",
        replace_apartment_data(key="floor", value="string"),
        ("floor", MESSAGES["floor_val_err"])
    ),
    (
        "Send bool to the 'floor' field",
        replace_apartment_data(key="floor", value=False),
        ("floor", MESSAGES["floor_val_err"])
    ),
    (
        "Send float to the 'floor' field",
        replace_apartment_data(key="floor", value=1.1),
        ("floor", MESSAGES["floor_val_err"])
    ),
    (
        "Send -11 to 'floor' field",
        replace_apartment_data(key="floor", value=-11),
        ("floor", MESSAGES["floor_val_err"])
    ),
    (
        "Send 1000 to 'floor' field",
        replace_apartment_data(key="floor", value=1000),
        ("floor", MESSAGES["floor_val_err"])
    ),
]

area_field_invalid_test_data = [
    (
        "No required 'area' field",
        remove_apartment_data("area"),
        ("area", MESSAGES["field_required"])
    ),
    (
        "Send None to the 'area' field",
        replace_apartment_data(key="area", value=None),
        ("area", MESSAGES["area_val_err"])
    ),
    (
        "Send string to the 'area' field",
        replace_apartment_data(key="area", value="string"),
        ("area", MESSAGES["area_val_err"])
    ),
    (
        "Send bool to the 'area' field",
        replace_apartment_data(key="area", value=False),
        ("area", MESSAGES["area_val_err"])
    ),
    (
        "Send -0.1 to 'area' field",
        replace_apartment_data(key="area", value=-0.1),
        ("area", MESSAGES["area_val_err"])
    ),
]

price_field_invalid_test_data = [
    (
        "Send string to the 'price' field",
        replace_apartment_data(key="price", value="string"),
        ("price", MESSAGES["price_val_err"])
    ),
    (
        "Send bool to the 'price' field",
        replace_apartment_data(key="price", value=False),
        ("price", MESSAGES["price_val_err"])
    ),
    (
        "Send float to the 'price' field",
        replace_apartment_data(key="price", value=1.1),
        ("price", MESSAGES["price_val_err"])
    ),
    (
        "Send 0 to 'price' field",
        replace_apartment_data(key="price", value=0),
        ("price", MESSAGES["price_val_err"])
    ),
]

description_field_invalid_test_data = [
    (
        "Send empty string to the 'description' field",
        replace_apartment_data(key="description", value=""),
        ("description", MESSAGES["description_val_err"])
    ),
    (
        "Send spaces only to the 'description' field",
        replace_apartment_data(key="description", value="    "),
        ("description", MESSAGES["description_val_err"])
    ),
    (
        "Send 256 chars to the 'description' field",
        replace_apartment_data(key="description", value="q" * 256),
        ("description", MESSAGES["description_val_err"])
    ),
    (
        "Send non latin chars to the 'description' field",
        replace_apartment_data(key="description", value="яЖбЮфΩδتشکगघ"),
        ("description", MESSAGES["description_val_err"])
    ),
    (
        "Send special chars to the 'description' field",
        replace_apartment_data(
            key="description",
            value="@#$*~`^\':;./|{}[]<>"
        ),
        ("description", MESSAGES["description_val_err"])
    ),
]

available_field_invalid_test_data = [
    (
        "No required 'available' field",
        remove_apartment_data("available"),
        ("available", MESSAGES["field_required"])
    ),
    (
        "Send None to the 'available' field",
        replace_apartment_data(key="available", value=None),
        ("available", MESSAGES["available_val_err"])
    ),
    (
        "Send string to the 'available' field",
        replace_apartment_data(key="available", value="String"),
        ("available", MESSAGES["available_val_err"])
    ),
    (
        "Send 1 to the 'available' field",
        replace_apartment_data(key="available", value=1),
        ("available", MESSAGES["available_val_err"])
    ),
    (
        "Send -0.1 to 'available' field",
        replace_apartment_data(key="available", value=-0.1),
        ("available", MESSAGES["available_val_err"])
    ),
]

plan_image_field_invalid_test_data = [
    (
        "Send bool to the 'plan_image' field",
        replace_apartment_data(key="plan_image", value=True),
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send 1 to the 'plan_image' field",
        replace_apartment_data(key="plan_image", value=1),
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send -0.1 to 'plan_image' field",
        replace_apartment_data(key="plan_image", value=-0.1),
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send non latin chars to the 'plan_image' field",
        replace_apartment_data(key="plan_image", value="яЖбЮфΩδتشکगघ"),
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send empty string to the 'plan_image' field",
        replace_apartment_data(key="plan_image", value=""),
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send spaces only to the 'plan_image' field",
        replace_apartment_data(key="plan_image", value="    "),
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send 256 chars to the 'plan_image' field",
        replace_apartment_data(key="plan_image", value="q" * 256),
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send string with spaces to the 'plan_image' field",
        replace_apartment_data(key="plan_image", value="String with spaces"),
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send special chars to the 'plan_image' field",
        replace_apartment_data(
            key="plan_image",
            value="@#$!&?*%~`^\"\':;?,|(){}[]<>"
        ),
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
]

angle_ids_field_invalid_test_data = [
    (
        "Send bool to the 'angle_ids' field",
        replace_apartment_data(key="angle_ids", value=True),
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send string to the 'angle_ids' field",
        replace_apartment_data(key="angle_ids", value="String"),
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send 1 to the 'angle_ids' field",
        replace_apartment_data(key="angle_ids", value=1),
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send -0.1 to 'angle_ids' field",
        replace_apartment_data(key="angle_ids", value=-0.1),
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send empty list to 'angle_ids' field",
        replace_apartment_data(key="angle_ids", value=[]),
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send list with negative int to 'angle_ids' field",
        replace_apartment_data(key="angle_ids", value=[-1, 2]),
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send list with bool to 'angle_ids' field",
        replace_apartment_data(key="angle_ids", value=[True, False]),
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send list with float to 'angle_ids' field",
        replace_apartment_data(key="angle_ids", value=[1.1, 2]),
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send list with string to 'angle_ids' field",
        replace_apartment_data(key="angle_ids", value=["String", 2]),
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
]

images_field_invalid_test_data = [
    (
        "Send bool to the 'images' field",
        replace_apartment_data(key="images", value=True),
        ("images", MESSAGES["images_val_err"])
    ),
    (
        "Send bool to one of the array values to the 'images' field",
        replace_apartment_data(
            key="images",
            value=["https://google.ca/", True, "https://chrome.ca/"]
        ),
        ("images", MESSAGES["images_val_err_URL"])
    ),

    (
        "Send 1 to the 'images' field",
        replace_apartment_data(key="images", value=1),
        ("images", MESSAGES["images_val_err"])
    ),
    (
        "Send 1 to one of the array values to the 'images' field",
        replace_apartment_data(
            key="images",
            value=["https://google.ca/", 1, "https://chrome.ca/"]
        ),
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send -0.1 to 'images' field",
        replace_apartment_data(key="images", value=-0.1),
        ("images", MESSAGES["images_val_err"])
    ),
    (
        "Send -0.1 to one of the array values to the 'images' field",
        replace_apartment_data(
            key="images",
            value=["https://google.ca/", -0.1, "https://chrome.ca/"]
        ),
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send empty string to the 'images' field",
        replace_apartment_data(key="images", value=""),
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send empty string to one of the array values to the 'images' field",
        replace_apartment_data(
            key="images",
            value=["https://google.ca/", "", "https://chrome.ca/"]
        ),
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send spaces only to the 'images' field",
        replace_apartment_data(key="images", value="    "),
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send spaces only to one of the array values to the 'images' field",
        replace_apartment_data(
            key="images",
            value=["https://google.ca/", "    ", "https://chrome.ca/"]
        ),
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send string with space to the 'images' field",
        replace_apartment_data(key="images", value="String space"),
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send string with space to one of the array values to the "
        "'images' field",
        replace_apartment_data(
            key="images",
            value=["https://google.ca/", "https://chro me.ca/", "https://chrome.ca/"]
        ),
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send string with 1025 symbols to the 'images' field",
        replace_apartment_data(
            key="images",
            value="https://goog.ca/" * 64 + "5"
        ),
        ("images", MESSAGES["images_val_err_max_char"])
    ),
    (
        "Send string with 1025 symbols to one of the array values to the "
        "'images' field",
        replace_apartment_data(
            key="images",
            value=[
                "https://google.ca/",
                "https://goog.ca/" * 64 + "5",
                "https://chrome.ca/"
            ]
        ),
        ("images", MESSAGES["images_val_err_max_char"])
    ),
    (
        "Send list of 20 URLs into 'images' field",
        replace_apartment_data(
            key="images",
            value=["https://google.ca/" for _ in range(21)]
        ),
        ("images", MESSAGES["images_val_err_max_URLs"])
    ),
    (
        "Send empty array to the 'images' field",
        replace_apartment_data(key="images", value=[]),
        ("images", MESSAGES["images_val_err"])
    ),
]

tour_field_invalid_test_data = [
    (
        "Send bool to the 'tour' field",
        replace_apartment_data(key="tour", value=True),
        ("tour", MESSAGES["tour_val_err"])
    ),
    (
        "Send 1 to the 'tour' field",
        replace_apartment_data(key="tour", value=1),
        ("tour", MESSAGES["tour_val_err"])
    ),
    (
        "Send -0.1 to the 'tour' field",
        replace_apartment_data(key="tour", value=-0.1),
        ("tour", MESSAGES["tour_val_err"])
    ),
    (
        "Send empty string to the 'tour' field",
        replace_apartment_data(key="tour", value=""),
        ("tour", MESSAGES["tour_val_err"])
    ),
    (
        "Send spaces only to the 'tour' field",
        replace_apartment_data(key="tour", value="    "),
        ("tour", MESSAGES["tour_val_err"])
    ),
    (
        "Send string with space to the 'tour' field",
        replace_apartment_data(key="tour", value="https://goog le.ca/"),
        ("tour", MESSAGES["tour_val_err"])
    ),
    (
        "Send 1025 char into 'tour' field",
        replace_apartment_data(key="tour", value="https://goog.ca/" * 64 + "5"),
        ("tour", MESSAGES["tour_val_err"])
    ),
]

ALL_FIELDS_VALID_TEST_PARAMS = [
    unit_type_field_valid_test_data,
    bedrooms_field_valid_test_data,
    bathrooms_field_valid_test_data,
    floor_field_valid_test_data,
    area_field_valid_test_data,
    price_field_valid_test_data,
    description_field_valid_test_data,
    available_field_valid_test_data,
    plan_image_field_valid_test_data,
    angle_ids_field_valid_test_data,
    images_field_valid_test_data,
    tour_field_valid_test_data
]

ALL_FIELDS_INVALID_TEST_PARAMS = [
    unit_id_field_invalid_test_data,
    unit_type_field_invalid_test_data,
    bedrooms_field_invalid_test_data,
    bathrooms_field_invalid_test_data,
    floor_field_invalid_test_data,
    area_field_invalid_test_data,
    price_field_invalid_test_data,
    description_field_invalid_test_data,
    available_field_invalid_test_data,
    plan_image_field_invalid_test_data,
    angle_ids_field_invalid_test_data,
    images_field_invalid_test_data,
    tour_field_invalid_test_data
]