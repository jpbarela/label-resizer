from pypdf import PdfReader, PdfWriter, Transformation, PageObject

INCH_UNITS = 72
LEGAL_WIDTH = 8.5 * INCH_UNITS
LEGAL_HEIGHT = 14 * INCH_UNITS


def transform_pdf(input_file: str, output_file: str) -> None:
    """
    Reads the file identified by input_file transforms the file and outputs it to the output_file
    """
    reader = PdfReader(input_file)
    writer = PdfWriter()

    dest_page = writer.add_blank_page(width=LEGAL_WIDTH, height=LEGAL_HEIGHT)
    position = 0
    for page in reader.pages:
        rotated_page = _rotate_page(page)
        dest_page.merge_transformed_page(
            rotated_page, _calculate_translation(position))
        position += 1
        if position % 4 == 0:
            dest_page = writer.add_blank_page(width=LEGAL_WIDTH, height=LEGAL_HEIGHT)

    writer.write(output_file)


def _rotate_page(input_page: PageObject) -> PageObject:
    """
    Rotates input_page 90 degrees without updating input_page
    """
    temp_writer = PdfWriter()
    temp_writer.add_page(input_page)
    temp_writer.pages[0].rotate(90).transfer_rotation_to_content()
    return temp_writer.pages[0]


def _calculate_translation(position: int) -> Transformation:
    """
    Calculates the translation based on the position
    """
    left = False
    top = False
    if position % 2 == 0:
        left = True
    if position % 4 in [0, 1]:
        top = True

    x = 0.25 * INCH_UNITS + (0 if left else 4 * INCH_UNITS)
    y = 1 * INCH_UNITS + (6 * INCH_UNITS if top else 0)
    return Transformation().translate(tx=x, ty=y)
