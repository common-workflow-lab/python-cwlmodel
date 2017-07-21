"""
Here we aim to parse the content of the schema salad for CWL tool.
"""

import ruamel.yaml as ryaml

# - CONSTANTS
NO_KEY_MSG = " ----- NOT FOUND ----- "
SCHEMA_DIR = "schemas_v1.0/"

process_schema = SCHEMA_DIR + "Process.yml"
tool_schema = SCHEMA_DIR + "CommandLineTool.yml"

# Load and merge both graph of the schemas
clt_model = []
for schema in [process_schema, tool_schema]:
    with open(schema) as yaml_file:
        schema_dict = ryaml.load(yaml_file, Loader=ryaml.Loader)
        clt_model += schema_dict['$graph'] 
 
for ele in clt_model:
    """
    print(ele.get('name', NO_KEY_MSG),
          ele.get('type', NO_KEY_MSG),
          ele.keys(),
          sep=' - ')
    """
    if ele.get('name', None) == 'CommandLineTool':
        clt_ele = ele

# Let's take the example of CommandLineTool
print("Future name of the class", clt_ele['name'], sep=" -> ")
print("Docstring should contains", clt_ele['doc'], sep=" -> ")
print("Object can have these attributes")
for field in clt_ele['fields']:
    print(" --->", field['name'], " ----> type(s):", field['type'])
