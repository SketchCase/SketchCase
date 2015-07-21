def prep_doc_for_json(doc, unicodify = []):
    doc = doc.to_mongo().to_dict()
    doc['id'] = unicode(doc['_id'])

    for field in unicodify:
        doc[field] = unicode(doc[field])

    del doc['_id']
    return doc
