import os

from jinja2 import Environment
from jinja2 import FileSystemLoader

from schema_parsing import parse_schemas


def write_code_to_file(filepath, code):
    with open(filepath, 'w') as f:
        f.write(code)

def generate_classes(spec_dir, dest):
    """
    :param spec_dir: directory with schema-salad CWL specification
    :param dest: directory to write generated Python classes
    """
    dest = os.path.abspath(dest)
    classes = parse_schemas(spec_dir)

    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "templates")
    env = Environment(loader=FileSystemLoader(path),
                      trim_blocks=True,
                      lstrip_blocks=True)
    template = env.get_template('class-template.j2')
    result = template.render(classes=classes)
    filepath = os.path.join(dest, "cwl-sdk.py")
    write_code_to_file(filepath, result)

    # TODO: append serializer/deserializer functions to generated files
