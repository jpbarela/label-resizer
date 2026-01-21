import click
from pdf_manipulator import transform_pdf


@click.command()
@click.argument("input_file", type=str, metavar='<input_file>')
@click.argument("output_file", type=str, metavar='<output_file>')
@click.option('--position', help='the starting position of the labels', type=int, default=1)
def label_resize(input_file: str, output_file: str, position: int = 1) -> None:
    """
    Transforms <input_file> into the <output_file>
    """
    # internally use zero-based indexing but start at 1 for the cli
    transform_pdf(input_file, output_file, position=position-1)


if __name__ == '__main__':
    label_resize()
