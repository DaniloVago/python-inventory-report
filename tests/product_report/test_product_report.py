from inventory_report.product import Product
from _pytest.capture import CaptureFixture


def test_product_report(capsys: CaptureFixture[str]) -> None:
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

    print(product)

    captured = capsys.readouterr()

    expected_output = (
            f"The product {id} - {product_name} "
            f"with serial number {serial_number} "
            f"manufactured on {manufacturing_date} "
            f"by the company {company_name} "
            f"valid until {expiration_date} "
            "must be stored according to the following instructions: "
            f"{storage_instructions}.\n"
        )

    assert captured.out == expected_output
