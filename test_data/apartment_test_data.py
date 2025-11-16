from test_data.apartment_creation_test_data import (
    ALL_FIELDS_VALID_TEST_PARAMS as create_valid_params,
    ALL_FIELDS_INVALID_TEST_PARAMS as create_invalid_params
)
from test_data.apartment_filtration_test_data import (
    FILTRATION_BY_ONE_FIELD_TEST_PARAMS,
    FILTRATION_BY_FEW_FIELDS_TEST_PARAMS
)
from test_data.apartment_update_test_data import (
    ALL_FIELDS_VALID_TEST_PARAMS as update_valid_params,
    ALL_FIELDS_INVALID_TEST_PARAMS as update_invalid_params
)
from test_data.apartment_test_data_tools import (
    get_apartment_data,
    get_few_apartments_data,
    all_fields_test_params,
)

APARTMENTS_NUMBER = 5  # number of generated apartments for tests_apartment

FILTER_NUMBER = 4

APARTMENT_DATA = get_apartment_data()
APARTMENT_DATA2 = get_apartment_data()

APARTMENTS_DATA = get_few_apartments_data(times=APARTMENTS_NUMBER)

FIELD_VALIDATION_VALID_TEST_PARAMS = all_fields_test_params(
    create_valid_params
)

FIELD_VALIDATION_INVALID_TEST_PARAMS = all_fields_test_params(
    create_invalid_params
)

FIELD_UPDATE_VALID_TEST_PARAMS = all_fields_test_params(
    update_valid_params
)

FIELD_UPDATE_INVALID_TEST_PARAMS = all_fields_test_params(
    update_invalid_params
)

ONE_FIELD_FILTRATION_TEST_PARAMS = all_fields_test_params(
    FILTRATION_BY_ONE_FIELD_TEST_PARAMS
)
FEW_FIELD_FILTRATION_TEST_PARAMS = FILTRATION_BY_FEW_FIELDS_TEST_PARAMS
