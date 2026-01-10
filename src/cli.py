import click
from pypdf import PdfReader, PdfWriter, Transformation

INCH_UNITS = 72
LEGAL_WIDTH = 8.5 * INCH_UNITS
LEGAL_HEIGHT = 14 * INCH_UNITS


@click.command()
@click.argument("input_file", type=str, metavar='<input_file>')
@click.argument("output_file", type=str, metavar='<output_file>')
def label_resize(input_file: str, output_file: str) -> None:
    """
    Transforms <input_file> into the <output_file>
    """
    reader = PdfReader(input_file)
    writer = PdfWriter()

    dest_page = writer.add_blank_page(width=LEGAL_WIDTH, height=LEGAL_HEIGHT)
    for page in reader.pages:
        temp_writer = PdfWriter()
        temp_writer.add_page(page)
        temp_writer.pages[0].rotate(90).transfer_rotation_to_content()
        dest_page.merge_transformed_page(
            temp_writer.pages[0], Transformation().translate(tx=0.25*INCH_UNITS, ty=1*INCH_UNITS))

    writer.write(output_file)


if __name__ == '__main__':
    label_resize()
