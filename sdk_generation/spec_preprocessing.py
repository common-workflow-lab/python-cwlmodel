import json
import os
import logging
import sys
import keyword

from schema_salad import schema as sc
from schema_salad import validate
from schema_salad.ref_resolver import file_uri


_logger = logging.getLogger("salad")


def normalize_spec(schema):

    # Get the metaschema to validate the schema
    metaschema_names, metaschema_doc, metaschema_loader = sc.get_metaschema()

    # Load schema document and resolve refs

    # if not (urllib.parse.urlparse(schema_uri)[0] and urllib.parse.urlparse(schema_uri)[0] in [u'http', u'https', u'file']):
    schema_uri = file_uri(os.path.abspath(schema))
    schema_raw_doc = metaschema_loader.fetch(schema_uri)

    try:
        schema_doc, schema_metadata = metaschema_loader.resolve_all(
            schema_raw_doc, schema_uri)
    except validate.ValidationException as e:
        _logger.error("Schema `%s` failed link checking:\n%s",
                      schema, e)
        _logger.debug("Index is %s", list(metaschema_loader.idx.keys()))
        _logger.debug("Vocabulary is %s", list(metaschema_loader.vocab.keys()))
        return 1
    except RuntimeError as e:
        _logger.error("Schema `%s` read error:\n%s",
                      schema, e)
        return 1

    return schema_doc


def rename_classes(schema):
    """
    rename future class names to get rid of https://w3id.org/cwl/salad
    """
    for item in schema:
        item['name'] = item['name'].split('#')[-1]
    return schema


def preprocess_spec(schema):
    normalized_schema = normalize_spec(schema)
    for entry in normalized_schema:
        if entry['type'] == 'record':
            namespace, name = entry['name'].split('#',1)
            fields = []
            for entry_field in entry.get('fields',[]):
                field_namespace, field_class_name = entry_field['name'].split('#',1)
                field_name = field_class_name.split('/',1)[1]
                if keyword.iskeyword(field_name):
                    field_name += '_'
                fields.append({'name': field_name, 
                               'doc': entry_field.get('doc','NODOC')})
            extends_uris = entry.get('extends',[])
            extends_uris = [extends_uris] if isinstance(extends_uris, str) else extends_uris
            extends = [extend_uri.split('#',1)[1] for extend_uri in extends_uris]
            yield {'name': name,
                   'extends': extends,
                   'doc': entry.get('doc','NODOC'),
                   'fields': fields}


if __name__ == '__main__':
    print(json.dumps(normalize_spec(sys.argv[1]), indent=4))
