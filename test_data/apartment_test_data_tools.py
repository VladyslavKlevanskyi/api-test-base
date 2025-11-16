import io
import random
import string

from PIL import Image
from faker import Faker
from reportlab.pdfgen import canvas

fake = Faker()

def get_apartment_data() -> dict[str, int | str | bool | list[int]]:
    """
    Generate a randomized dictionary representing apartment data
    for testing purposes.

    Returns:
        dict: A dictionary containing various fields typically associated
              with an apartment listing, such as unit ID, number of bedrooms,
              availability, image URLs, etc.
    """
    return {
        "unit_id": random.randint(50, 999),
        "unit_type": random.choice(
            string.ascii_uppercase
        ) + str(random.randint(0, 20)),
        "bedrooms": random.randint(0, 7),
        "bathrooms": random.randint(1, 7),
        "floor": random.randint(-10, 999),
        "area": round(random.uniform(0, 99999.9), 1),
        "price": random.randint(10000, 1500000),
        "description": fake.text(max_nb_chars=50),
        "available": fake.boolean(),
        "plan_image": fake.file_path(depth=3, category="image"),
        "angle_ids": [
            random.randint(1, 999) for _ in range(random.randint(1, 5))
        ],
        "images": [
            fake.url() for _ in range(random.randint(1, 10))
        ],
        "tour": fake.url()
    }


def get_few_apartments_data(
        times: int
) -> list[dict[str, int | str | bool | list[int]]]:
    """
    Generate a list of unique apartment data dictionaries.

    Args:
        times: The number of unique apartment objects to generate.

    Returns:
        list: A list of apartment data dictionaries with unique unit IDs.
    """
    uniq_unit_id = set()
    while len(uniq_unit_id) < times:
        uniq_unit_id.add(random.randint(50, 300))
    apartments_list = []

    for unit_id in uniq_unit_id:
        apartment = get_apartment_data()
        apartment["unit_id"] = unit_id  # Ensure uniqueness
        apartments_list.append(apartment)
    return apartments_list

def remove_apartment_data(
        key: str
) -> dict[str, int | str | bool | float | list[int]]:
    """
    Generate apartment data and remove a specific key from the dictionary.

    Args:
        key: The field name to remove from the generated apartment data.

    Returns:
        dict: Apartment data with the specified key removed.
    """
    apartment_data = get_apartment_data()
    apartment_data.pop(key, None)  # Silently ignore missing key
    return apartment_data


def replace_apartment_data(
        key: str,
        value: int | str | bool | float | list[int] | list[str] | None
) -> dict[str, int | str | bool | float | list[int] | list[str] | None]:
    """
    Generate apartment data and replace the value of a specific field.

    Args:
        key: The field name to modify.
        value: The new value to assign to the field. Can be None.

    Returns:
        dict: Apartment data with the updated field value.
    """
    apartment_data = get_apartment_data()
    apartment_data[key] = value
    return apartment_data

def prepare_file_upload(
        content: bytes,
        extension: str
) -> dict[str, tuple[str, io.BytesIO, str]]:
    """
    Prepare a file for multipart/form-data upload compatible with HTTP
    clients like httpx.

    Args:
        content: Binary content of the file.
        extension: File extension (e.g., 'jpg', 'pdf', 'txt').

    Returns:
        dict: A dictionary formatted as {"file": (filename, file_object,
              content_type)} suitable for use with httpx or requests.

    Raises:
        ValueError: If the file extension is not supported.
    """
    test_file_name = f"test_plan.{extension.lower()}"
    ext = extension.lower()

    # Determine MIME type based on file extension
    if ext in {"jpg", "jpeg"}:
        content_type = "image/jpeg"
    elif ext == "png":
        content_type = "image/png"
    elif ext == "bmp":
        content_type = "image/bmp"
    elif ext == "tiff":
        content_type = "image/tiff"
    elif ext == "pdf":
        content_type = "application/pdf"
    elif ext == "txt":
        content_type = "text/plain"
    else:
        raise ValueError(f"Unsupported extension: .{ext}")

    file_obj = io.BytesIO(content)
    file_obj.name = test_file_name

    return {"file": (test_file_name, file_obj, content_type)}

def generate_content(file_format: str) -> bytes:
    """
    Generate file content in various formats (image, PDF, text) for testing
    uploads.

    Args:
        file_format: The format of the content to generate.
                     Supported formats: "JPEG", "PNG", "BMP", "TIFF", "PDF",
                                        "TXT"

    Returns:
        bytes: The generated file content in binary form.

    Raises:
        ValueError: If an unsupported format is provided.
    """
    if file_format in {"JPEG", "PNG", "BMP", "TIFF"}:
        color = (255, 0, 0)
        img = Image.new("RGB", (10, 10), color)
        buf = io.BytesIO()
        img.save(buf, format=file_format)
        return buf.getvalue()
    elif file_format == "PDF":
        buf = io.BytesIO()
        canvas_obj = canvas.Canvas(buf)
        canvas_obj.drawString(100, 750, "Hello PDF!")
        canvas_obj.save()
        return buf.getvalue()
    elif file_format == "TXT":
        return b"Hello, this is a test .txt file.\nLine 2."
    else:
        raise ValueError(f"Unsupported format: .{file_format}")

def all_fields_test_params(all_lists: list) -> list:
    result_list = []
    for sublist in all_lists:
        result_list.extend(sublist)
    return result_list
