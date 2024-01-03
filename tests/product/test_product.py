from inventory_report.product import Product


def test_create_product() -> None:
    id = "1"
    company_name = "X"
    product_name = "ABC"
    manufacturing_date = "2023-09-28"
    expiration_date = "2023-10-28"
    serial_number = "12345"
    storage_instructions = "Dry place"

    product = Product(
        id=id,
        company_name=company_name,
        product_name=product_name,
        manufacturing_date=manufacturing_date,
        expiration_date=expiration_date,
        serial_number=serial_number,
        storage_instructions=storage_instructions
    )

    assert product.id == id
    assert product.company_name == company_name
    assert product.product_name == product_name
    assert product.manufacturing_date == manufacturing_date
    assert product.expiration_date == expiration_date
    assert product.serial_number == serial_number
    assert product.storage_instructions == storage_instructions
