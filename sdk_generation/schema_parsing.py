import os

from sdk_generation.spec_normalization import normalize_spec


def parse_schemas(source_dir):
    normalized_scheme = normalize_spec(os.path.join(source_dir, "CommonWorkflowLanguage.yml"))
    return normalized_scheme