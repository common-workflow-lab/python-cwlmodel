import json
import os

import logging

import sys
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

    return json.dumps(schema_doc, indent=4)


if __name__ == '__main__':
    print(normalize_spec(sys.argv[1]))