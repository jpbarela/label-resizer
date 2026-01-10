import click
from pdf_manipulator import transform_pdf


@click.command()
@click.argument("input_file", type=str, metavar='<input_file>')
@click.argument("output_file", type=str, metavar='<output_file>')
def label_resize(input_file: str, output_file: str) -> None:
    """
    Transforms <input_file> into the <output_file>
    """
    transform_pdf(input_file, output_file)


if __name__ == '__main__':
    label_resize()
