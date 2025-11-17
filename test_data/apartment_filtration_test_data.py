APARTMENT_DATA_FOR_FILTRATION_TEST = [
    {
        "unit_id": 1,
        "unit_type": "A1",
        "bedrooms": 9,
        "bathrooms": 3,
        "floor": 20,
        "area": 10,
        "price": 500000,
        "available": True,
        "angle_ids": [1, 3]
    },
    {
        "unit_id": 2,
        "unit_type": "A1",
        "bedrooms": 8,
        "bathrooms": 4,
        "floor": 10,
        "area": 10,
        "price": 700000,
        "available": False,
        "angle_ids": [2, 3, 4]
    },
    {
        "unit_id": 3,
        "unit_type": "A1",
        "bedrooms": 7,
        "bathrooms": 5,
        "floor": 8,
        "area": 10,
        "price": 400000,
        "available": True,
        "angle_ids": [3, 5]
    },
    {
        "unit_id": 4,
        "unit_type": "B2",
        "bedrooms": 6,
        "bathrooms": 6,
        "floor": 7,
        "area": 10,
        "price": 100000,
        "available": False,
        "angle_ids": [1, 2, 3]
    },
    {
        "unit_id": 5,
        "unit_type": "C3",
        "bedrooms": 5,
        "bathrooms": 7,
        "floor": 6,
        "area": 10,
        "price": 300000,
        "available": True,
        "angle_ids": [2]
    },
    {
        "unit_id": 6,
        "unit_type": "A1",
        "bedrooms": 4,
        "bathrooms": 8,
        "floor": 1,
        "area": 10,
        "price": 510000,
        "available": True,
        "angle_ids": [1, 3, 7]
    },
]

unit_type_field_filtration_params = [
    (
        "'unit_type' field filtration 1",
        "unit_type",
        "A1",
        4
    ),
    (
        "'unit_type' field filtration 2",
        "unit_type",
        "B2",
        1
    ),
]
min_bedrooms_field_filtration_params = [
    (
        "'min_bedrooms' field filtration 1",
        "min_bedrooms",
        6,
        4
    ),
    (
        "'min_bedrooms' field filtration 2",
        "min_bedrooms",
        7,
        3
    ),
]
max_bedrooms_field_filtration_params = [
    (
        "'max_bedrooms' field filtration 1",
        "max_bedrooms",
        6,
        3
    ),
    (
        "'max_bedrooms' field filtration 2",
        "max_bedrooms",
        7,
        4
    ),
]
min_bathrooms_field_filtration_params = [
    # min_bathrooms
    (
        "'min_bathrooms' field filtration 1",
        "min_bathrooms",
        6,
        3
    ),
    (
        "'min_bathrooms' field filtration 2",
        "min_bathrooms",
        7,
        2
    ),
]
max_bathrooms_field_filtration_params = [
    (
        "'max_bathrooms' field filtration 1",
        "max_bathrooms",
        6,
        4
    ),
    (
        "'max_bathrooms' field filtration 2",
        "max_bathrooms",
        7,
        5
    ),
]
min_floor_field_filtration_params = [
    (
        "'min_floor' field filtration 1",
        "min_floor",
        8,
        3
    ),
    (
        "'min_floor' field filtration 2",
        "min_floor",
        7,
        4
    ),
]
max_floor_field_filtration_params = [
    (
        "'max_floor' field filtration 1",
        "max_floor",
        10,
        5
    ),
    (
        "'max_floor' field filtration 2",
        "max_floor",
        7,
        3
    ),
]
min_price_field_filtration_params = [
    (
        "'min_price' field filtration 1",
        "min_price",
        400000,
        4
    ),
    (
        "'min_price' field filtration 2",
        "min_price",
        500000,
        3
    ),
]
max_price_field_filtration_params = [
    (
        "'max_price' field filtration 1",
        "max_price",
        300000,
        2
    ),
    (
        "'max_price' field filtration 2",
        "max_price",
        500000,
        4
    ),
]
available_field_filtration_params = [
    (
        "'available' field filtration 1",
        "available",
        True,
        4
    ),
    (
        "'available' field filtration 2",
        "available",
        False,
        2
    ),
]
angle_id_field_filtration_params = [
    (
        "'angle_id' field filtration 1",
        "angle_id",
        1,
        3
    ),
    (
        "'angle_id' field filtration 2",
        "angle_id",
        3,
        5
    ),
]

FILTRATION_BY_FEW_FIELDS_TEST_PARAMS = [
    # 'min_bedrooms'&'max_bedrooms'
    (
        "'min_bedrooms'&'max_bedrooms' fields filtration",
        {"min_bedrooms": 5, "max_bedrooms": 8},
        4
    ),
    # 'min_bathrooms'&'max_bathrooms'
    (
        "'min_bathrooms'&'max_bathrooms' fields filtration",
        {"min_bathrooms": 4, "max_bathrooms": 7},
        4
    ),
    # 'min_floor'&'max_floor'
    (
        "'min_floor'&'max_floor' fields filtration",
        {"min_floor": 2, "max_floor": 15},
        4
    ),
    # 'min_price'&'max_price'
    (
        "'min_price'&'max_price' fields filtration",
        {"min_price": 300000, "max_price": 500000},
        3
    ),
    # other fields
    (
        "'unit_type'&'available' fields filtration",
        {"unit_type": "A1", "available": True},
        3
    ),
    (
        "'unit_type'&'available'&'angle_id' fields filtration",
        {"unit_type": "A1", "available": True, "angle_id": 1},
        2
    ),
]

FILTRATION_BY_ONE_FIELD_TEST_PARAMS = [
    unit_type_field_filtration_params,
    min_bedrooms_field_filtration_params,
    max_bedrooms_field_filtration_params,
    min_bathrooms_field_filtration_params,
    max_bathrooms_field_filtration_params,
    min_floor_field_filtration_params,
    max_floor_field_filtration_params,
    min_price_field_filtration_params,
    max_price_field_filtration_params,
    available_field_filtration_params,
    angle_id_field_filtration_params
]
