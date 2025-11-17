from test_data.apartment_test_data_messages import MESSAGES


# =================VALID TEST DATA=======================

unit_id_field_valid_test_data = [
    #  unit_id field
    (
        "Send integer into 'unit_id' field",
        "unit_id",
        11,
        11
    ),
]

unit_type_field_valid_test_data = [
    (
        "Send None into 'unit_type' field",
        "unit_type",
        None,
        None,
    ),
    (
        "Send one char into 'unit_type' field",
        "unit_type",
        "T",
        "T",
    ),
    (
        "Send 25 char into 'unit_type' field",
        "unit_type",
        "T" * 25,
        "T" * 25,
    ),
    (
        "Send float into 'unit_type' field",
        "unit_type",
        "10.1",
        "10.1"
    ),
    (
        "Send integer into 'unit_type' field",
        "unit_type",
        11,
        "11"
    ),
    (
        "Check strip spaces 'unit_type' field",
        "unit_type",
        "  23.F ",
        "23.F"
    ),
]

bedrooms_field_valid_test_data = [
    (
        "Send 0 to 'bedrooms' field in payload",
        "bedrooms",
        0,
        0
    ),
    (
        "Send 9 to 'bedrooms' field in payload",
        "bedrooms",
        9,
        9
    ),
]

bathrooms_field_valid_test_data = [
    (
        "Send 1 to 'bathrooms' field in payload",
        "bathrooms",
        1,
        1
    ),
    (
        "Send 9 to 'bathrooms' field in payload",
        "bathrooms",
        9,
        9
    ),
]

floor_field_valid_test_data = [
    (
        "Send -10 to 'floor' field in payload",
        "floor",
        -10,
        -10
    ),
    (
        "Send 999 to 'floor' field in payload",
        "floor",
        999,
        999
    ),
]

area_field_valid_test_data = [
    (
        "Send 0 to 'area' field in payload",
        "area",
        0,
        0
    ),
    (
        "Send 1.1 to 'area' field in payload",
        "area",
        1.1,
        1.1
    ),
]
price_field_valid_test_data = [
    (
        "Send None into 'price' field",
        "price",
        None,
        None
    ),
    (
        "Send 1 to 'price' field in payload",
        "price",
        1,
        1
    ),
]
description_field_valid_test_data = [
    (
        "Send None into 'description' field",
        "description",
        None,
        None
    ),
    (
        "Send one char into 'description' field",
        "description",
        "T",
        "T"
    ),
    (
        "Send 255 char into 'description' field",
        "description",
        "T" * 255,
        "T" * 255
    ),
    (
        "Send float into 'description' field",
        "description",
        10.1,
        "10.1"
    ),
    (
        "Send integer into 'description' field",
        "description",
        11,
        "11"
    ),
    (
        "Send bool into 'description' field",
        "description",
        False,
        "False"
    ),
    (
        "Check strip spaces 'description' field",
        "description",
        "  23.F ",
        "23.F"
    ),
    (
        "Check special symbols '.,\"( )-!?&%' into 'description' field",
        "description",
        ".,\"( )-!?&%",  # noqa:  Q003
        ".,\"( )-!?&%"  # noqa:  Q003
    ),
]

available_field_valid_test_data = [
    (
        "Send True into 'available' field",
        "available",
        True,
        True
    ),
    (
        "Send False into 'available' field",
        "available",
        False,
        False
    ),
]

plan_image_field_valid_test_data = [
    (
        "Send None into 'plan_image' field",
        "plan_image",
        None,
        None
    ),
    (
        "Send one char into 'plan_image' field",
        "plan_image",
        "T",
        "T"
    ),
    (
        "Send 255 char into 'plan_image' field",
        "plan_image",
        "T" * 255,
        "T" * 255
    ),
    (
        "Send string '_.\\/-Qa0' into 'plan_image' field",
        "plan_image",
        "_.\\/-Qa0",
        "_.\\/-Qa0"
    ),
]

angle_ids_field_valid_test_data = [
    (
        "Send None into 'angle_ids' field",
        "angle_ids",
        None,
        None
    ),
]

images_field_valid_test_data = [
    (
        "Send None into 'images' field",
        "images",
        None,
        None
    ),
    (
        "Send 1024 char into 'images' field",
        "images",
        "https://goog.ca/" * 64,
        ["https://goog.ca/" * 64]
    ),
    (
        "Send list of 20 URLs into 'images' field",
        "images",
        ["https://google.ca/" for _ in range(20)],
        ["https://google.ca/" for _ in range(20)]
    ),
    (
        "Send list of 1 URLs into 'images' field",
        "images",
        ["https://google.ca/"],
        ["https://google.ca/"]
    ),
]

tour_field_valid_test_data = [
    (
        "Send None into 'tour' field",
        "tour",
        None,
        None
    ),
    (
        "Send 1024 char URL into 'tour' field",
        "tour",
        "https://goog.ca/" * 64,
        "https://goog.ca/" * 64
    ),
]

# =================INVALID TEST DATA=======================

unit_id_field_invalid_test_data = [
    (
        "Send None to the 'unit_id' field",
        {"unit_id": None},
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
    (
        "Send bool to the 'unit_id' field",
        {"unit_id": True},
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
    (
        "Send string to the 'unit_id' field",
        {"unit_id": "string"},
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
    (
        "Send float to the 'unit_id' field",
        {"unit_id": 1.1},
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
    (
        "Negative value to 'unit_id' field",
        {"unit_id": -1},
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
    (
        "Send 0 to 'unit_id' field",
        {"unit_id": 0},
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
    (
        "Send 1000 to 'unit_id' field",
        {"unit_id": 1000},
        ("unit_id", MESSAGES["unit_id_val_err"])
    ),
]
unit_type_field_invalid_test_data = [
    (
        "Send bool to the 'unit_type' field",
        {"unit_type": True},
        ("unit_type", MESSAGES["unit_type_not_bool"])
    ),
    (
        "Send empty string to the 'unit_type' field",
        {"unit_type": ""},
        ("unit_type", MESSAGES["unit_type_not_empty"])
    ),
    (
        "Send spaces only to the 'unit_type' field",
        {"unit_type": "    "},
        ("unit_type", MESSAGES["unit_type_not_empty"])
    ),
    (
        "Send 26 chars to the 'unit_type' field",
        {"unit_type": "q" * 26},
        ("unit_type", MESSAGES["unit_type_all"])
    ),
    (
        "Send non latin chars to the 'unit_type' field",
        {"unit_type": "яЖбЮфΩδتشکगघ"},
        ("unit_type", MESSAGES["unit_type_all"])
    ),
    (
        "Send special chars to the 'unit_type' field",
        {"unit_type": "@#$!&?*%~`^\"\':;?,./|(){}[]<>"},
        ("unit_type", MESSAGES["unit_type_all"])
    ),
]

bedrooms_field_invalid_test_data = [
    (
        "Send None to the 'bedrooms' field",
        {"bedrooms": None},
        ("bedrooms", MESSAGES["bedrooms_val_err"])
    ),
    (
        "Send string to the 'bedrooms' field",
        {"bedrooms": "string"},
        ("bedrooms", MESSAGES["bedrooms_val_err"])
    ),
    (
        "Send bool to the 'bedrooms' field",
        {"bedrooms": False},
        ("bedrooms", MESSAGES["bedrooms_val_err"])
    ),
    (
        "Send float to the 'bedrooms' field",
        {"bedrooms": 1.1},
        ("bedrooms", MESSAGES["bedrooms_val_err"])
    ),
    (
        "Negative value to 'bedrooms' field",
        {"bedrooms": -1},
        ("bedrooms", MESSAGES["bedrooms_val_err"])
    ),
    (
        "Send 10 to 'bedrooms' field",
        {"bedrooms": 10},
        ("bedrooms", MESSAGES["bedrooms_val_err"])
    ),
]
bathrooms_field_invalid_test_data = [
    (
        "Send None to the 'bathrooms' field",
        {"bathrooms": None},
        ("bathrooms", MESSAGES["bathrooms_val_err"])
    ),
    (
        "Send string to the 'bathrooms' field",
        {"bathrooms": "string"},
        ("bathrooms", MESSAGES["bathrooms_val_err"])
    ),
    (
        "Send bool to the 'bathrooms' field",
        {"bathrooms": False},
        ("bathrooms", MESSAGES["bathrooms_val_err"])
    ),
    (
        "Send float to the 'bathrooms' field",
        {"bathrooms": 1.1},
        ("bathrooms", MESSAGES["bathrooms_val_err"])
    ),
    (
        "Send 0 to 'bathrooms' field",
        {"bathrooms": 0},
        ("bathrooms", MESSAGES["bathrooms_val_err"])
    ),
    (
        "Send 10 to 'bathrooms' field",
        {"bathrooms": 10},
        ("bathrooms", MESSAGES["bathrooms_val_err"])
    ),
]

floor_field_invalid_test_data = [
    (
        "Send None to the 'floor' field",
        {"floor": None},
        ("floor", MESSAGES["floor_val_err"])
    ),
    (
        "Send string to the 'floor' field",
        {"floor": "string"},
        ("floor", MESSAGES["floor_val_err"])
    ),
    (
        "Send bool to the 'floor' field",
        {"floor": False},
        ("floor", MESSAGES["floor_val_err"])
    ),
    (
        "Send float to the 'floor' field",
        {"floor": 1.1},
        ("floor", MESSAGES["floor_val_err"])
    ),
    (
        "Send -11 to 'floor' field",
        {"floor": -11},
        ("floor", MESSAGES["floor_val_err"])
    ),
    (
        "Send 1000 to 'floor' field",
        {"floor": 1000},
        ("floor", MESSAGES["floor_val_err"])
    ),
]

area_field_invalid_test_data = [
    (
        "Send None to the 'area' field",
        {"area": None},
        ("area", MESSAGES["area_val_err"])
    ),
    (
        "Send string to the 'area' field",
        {"area": "string"},
        ("area", MESSAGES["area_val_err"])
    ),
    (
        "Send bool to the 'area' field",
        {"area": False},
        ("area", MESSAGES["area_val_err"])
    ),
    (
        "Send -0.1 to 'area' field",
        {"area": -0.1},
        ("area", MESSAGES["area_val_err"])
    ),
]

price_field_invalid_test_data = [
    (
        "Send string to the 'price' field",
        {"price": "string"},
        ("price", MESSAGES["price_val_err"])
    ),
    (
        "Send bool to the 'price' field",
        {"price": False},
        ("price", MESSAGES["price_val_err"])
    ),
    (
        "Send float to the 'price' field",
        {"price": 1.1},
        ("price", MESSAGES["price_val_err"])
    ),
    (
        "Send 0 to 'price' field",
        {"price": 0},
        ("price", MESSAGES["price_val_err"])
    ),
]

description_field_invalid_test_data = [
    (
        "Send empty string to the 'description' field",
        {"description": ""},
        ("description", MESSAGES["description_val_err"])
    ),
    (
        "Send spaces only to the 'description' field",
        {"description": "    "},
        ("description", MESSAGES["description_val_err"])
    ),
    (
        "Send 256 chars to the 'description' field",
        {"description": "q" * 256},
        ("description", MESSAGES["description_val_err"])
    ),
    (
        "Send non latin chars to the 'description' field",
        {"description": "яЖбЮфΩδتشکगघ"},
        ("description", MESSAGES["description_val_err"])
    ),
    (
        "Send special chars to the 'description' field",
        {"description": "@#$*~`^\':;./|{}[]<>"},
        ("description", MESSAGES["description_val_err"])
    ),
]

available_field_invalid_test_data = [
    (
        "Send None to the 'available' field",
        {"available": None},
        ("available", MESSAGES["available_val_err"])
    ),
    (
        "Send string to the 'available' field",
        {"available": "String"},
        ("available", MESSAGES["available_val_err"])
    ),
    (
        "Send 1 to the 'available' field",
        {"available": 1},
        ("available", MESSAGES["available_val_err"])
    ),
    (
        "Send -0.1 to 'available' field",
        {"available": -0.1},
        ("available", MESSAGES["available_val_err"])
    ),
]

plan_image_field_invalid_test_data = [
    (
        "Send bool to the 'plan_image' field",
        {"plan_image": True},
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send 1 to the 'plan_image' field",
        {"plan_image": 1},
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send -0.1 to 'plan_image' field",
        {"plan_image": -0.1},
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send non latin chars to the 'plan_image' field",
        {"plan_image": "яЖбЮфΩδتشکगघ"},
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send empty string to the 'plan_image' field",
        {"plan_image": ""},
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send spaces only to the 'plan_image' field",
        {"plan_image": "    "},
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send 256 chars to the 'plan_image' field",
        {"plan_image": "q" * 256},
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send string with spaces to the 'plan_image' field",
        {"plan_image": "String with spaces"},
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
    (
        "Send special chars to the 'plan_image' field",
        {"plan_image": "@#$!&?*%~`^\"\':;?,|(){}[]<>"},
        ("plan_image", MESSAGES["plan_image_val_err"])
    ),
]

angle_ids_field_invalid_test_data = [
    (
        "Send bool to the 'angle_ids' field",
        {"angle_ids": True},
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send string to the 'angle_ids' field",
        {"angle_ids": "String"},
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send 1 to the 'angle_ids' field",
        {"angle_ids": 1},
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send -0.1 to 'angle_ids' field",
        {"angle_ids": -0.1},
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send empty list to 'angle_ids' field",
        {"angle_ids": []},
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send list with negative int to 'angle_ids' field",
        {"angle_ids": [-1, 2]},
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send list with bool to 'angle_ids' field",
        {"angle_ids": [True, False]},
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send list with float to 'angle_ids' field",
        {"angle_ids": [1.1, 2]},
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
    (
        "Send list with string to 'angle_ids' field",
        {"angle_ids": ["String", 2]},
        ("angle_ids", MESSAGES["angle_ids_val_err"])
    ),
]

images_field_invalid_test_data = [
    (
        "Send bool to the 'images' field",
        {"images": True},
        ("images", MESSAGES["images_val_err"])
    ),
    (
        "Send bool to one of the array values to the 'images' field",
        {"images": ["https://google.ca/", True, "https://chrome.ca/"]},
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send 1 to the 'images' field",
        {"images": 1},
        ("images", MESSAGES["images_val_err"])
    ),
    (
        "Send 1 to one of the array values to the  'images' field",
        {"images": ["https://google.ca/", 1, "https://chrome.ca/"]},
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send -0.1 to 'images' field",
        {"images": -0.1},
        ("images", MESSAGES["images_val_err"])
    ),
    (
        "Send -0.1 to one of the array values to 'images' field",
        {"images": ["https://google.ca/", -0.1, "https://chrome.ca/"]},
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send empty string to the 'images' field",
        {"images": ""},
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send empty string to one of the array values to the 'images' field",
        {"images": ["https://google.ca/", "", "https://chrome.ca/"]},
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send spaces only to the 'images' field",
        {"images": "    "},
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send spaces only to one of the array values to the 'images' field",
        {"images": ["https://google.ca/", "    ", "https://chrome.ca/"]},
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send string with space to the 'images' field",
        {"images": "String space"},
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send string with space to one of the array values to the "
        "'images' field",
        {"images": [
            "https://google.ca/", "String space", "https://chrome.ca/"
        ]},
        ("images", MESSAGES["images_val_err_URL"])
    ),
    (
        "Send string with 1025 symbols to the 'images' field",
        {"images": "https://goog.ca/" * 64 + "5"},
        ("images", MESSAGES["images_val_err_max_char"])
    ),
    (
        "Send string with 1025 symbols to one of the array values to the "
        "'images' field",
        {"images": [
            "https://google.ca/",
            "https://goog.ca/" * 64 + "5",
            "https://chrome.ca/"
        ]},
        ("images", MESSAGES["images_val_err_max_char"])
    ),
    (
        "Send list of 20 URLs into 'images' field",
        {"images": ["https://google.ca/" for _ in range(21)]},
        ("images", MESSAGES["images_val_err_max_URLs"])
    ),
    (
        "Send empty array to the 'images' field",
        {"images": []},
        ("images", MESSAGES["images_val_err"])
    ),
]

tour_field_invalid_test_data = [
    (
        "Send bool to the 'tour' field",
        {"tour": True},
        ("tour", MESSAGES["tour_val_err"])
    ),
    (
        "Send 1 to the 'tour' field",
        {"tour": 1},
        ("tour", MESSAGES["tour_val_err"])
    ),
    (
        "Send -0.1 to the 'tour' field",
        {"tour": -0.1},
        ("tour", MESSAGES["tour_val_err"])
    ),
    (
        "Send empty string to the 'tour' field",
        {"tour": ""},
        ("tour", MESSAGES["tour_val_err"])
    ),
    (
        "Send spaces only to the 'tour' field",
        {"tour": "    "},
        ("tour", MESSAGES["tour_val_err"])
    ),
    (
        "Send string with space to the 'tour' field",
        {"tour": "https://goog le.ca/"},
        ("tour", MESSAGES["tour_val_err"])
    ),
    (
        "Send 1025 char into 'tour' field",
        {"tour": "https://goog.ca/" * 64 + "5"},  # noqa:  Q003
        ("tour", MESSAGES["tour_val_err"])
    ),
]


ALL_FIELDS_VALID_TEST_PARAMS = [
    unit_id_field_valid_test_data,
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
