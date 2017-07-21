import ruamel.yaml as ryaml

def load_schema(schema_path):
    """
    """
    with open(schema_path) as yaml_file:
        """
        Get the path of the CommonwWorkflowLanguage schema and return a list of DICT
        """
        schema_list = ryaml.load(yaml_file, Loader=ryaml.Loader)
    return schema_list
