from pathlib import Path

REQUIRED_CONCEPT_FIELDS = ['id', 'title', 'summary', 'plain_jp', 'description']


def validate_concept(data: dict, path: Path) -> None:
    missing = [key for key in REQUIRED_CONCEPT_FIELDS if not data.get(key)]
    if missing:
        raise ValueError(f'{path}: missing required fields {missing}')


def validate_dashboard(data: dict, path: Path) -> None:
    for key in ['id', 'title', 'summary']:
        if not data.get(key):
            raise ValueError(f'{path}: missing required field {key}')
