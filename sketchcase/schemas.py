document_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'}
    },
    'required': ['name'],
    'additionalProperties': False
}

artboard_scehma = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'document_id': {'type': 'string'}
    },
    'required': ['name', 'document_id'],
    'additionalProperties': False
}

revision_schema = {
    'type': 'object',
    'properties': {
        'artboard_id': {'type': 'string'},
        'image_url': {'type': 'string'},
        'image_data': {'type': 'string'}
    },
    'required': ['artboard_id'],
    'additionalProperties': False
}
