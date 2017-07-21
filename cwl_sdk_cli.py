import argparse as ap
import os

from sdk_generation import generate_classes


def generate_sdk():
    help_text = """
           python-cwlmodel generates CWL SDK in Python for different versions of schema-salad CWL specification.
           Example: $ cwl-sdk SOURCE DEST
           """
    parser = ap.ArgumentParser(description=help_text, formatter_class=ap.RawDescriptionHelpFormatter)
    parser.add_argument('source', help='A directory or URL with CWL specification')
    parser.add_argument('destination', help='A path for generated files ')
    args = parser.parse_args()

    source = args.source
    dest = args.destination
    generate_classes(source, dest)
    print('Generated SDK files to {0}'.format(os.path.abspath(dest)))

if __name__ == '__main__':
    generate_sdk()