MESSAGES = {
    "field_required": "Field required",
    "unit_id_val_err": "Value error, unit_id must be an integer "
                       "between 1 and 999 (inclusive)",
    "unit_type_not_bool": "Value error, unit_type cannot be a boolean",
    "unit_type_not_empty": "Value error, unit_type cannot be an empty or "
                           "whitespace-only string",
    "unit_type_all": "Value error, unit_type must be 1–25 characters and "
                     "contain only letters, digits, spaces, '.', '-', or '_'",
    "bedrooms_val_err": "Value error, bedrooms must be an integer between 0"
                        " and 9 (inclusive)",
    "bathrooms_val_err": "Value error, bathrooms must be an integer between"
                         " 1 and 9 (inclusive)",
    "floor_val_err": "Value error, floor must be an integer between -10 "
                         "and 999 (inclusive)",
    "area_val_err": "Value error, area must be a non-negative number "
                    "(int or float)",
    "price_val_err": "Value error, price must be a positive integer if "
                     "provided",
    "description_val_err": "Value error, description must be a non-empty string"
                           " (max 255 characters) containing only Latin"
                           " letters, digits, spaces, and the following"
                           " symbols: '.', ',', '\"', \"'\", '(', ')', '!',"
                           " '/', '?', '&', '%', ':', or '-'",
    "available_val_err": "Value error, available must be a boolean "
                         "(true or false)",
    "plan_image_val_err": "Value error, plan_image must be a non-empty string "
                          "(max 255 characters) containing only Latin letters,"
                          " digits, '.', '_', '-', '/' or '\\'",
    "angle_ids_val_err": "Value error, angle_ids must be a list of positive "
                         "integers",
    "images_val_err": "Value error, images must be a non-empty list of URLs",
    "images_val_err_URL": "Value error, Each element in 'images' array must"
                          " be a string with valid URL.",
    "images_val_err_max_char": "Value error, URL exceeds maximum length of"
                               " 1024 characters.",
    "images_val_err_max_URLs": "Value error, 'images' may contain no more"
                               " than 20 URLs",
    "tour_val_err": "Value error, Field 'tour' must be a valid URL "
                    "with maximum length 1024.",
    "apartment_is_exist": "Apartment with this unit_id already exists",
    "unsupported_file": "Unsupported file format.",
}