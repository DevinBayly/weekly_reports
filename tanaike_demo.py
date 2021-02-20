def test_update(docs,text,doc_id):

    requests =[
            {
                'insertText': {
                    'location': {
                        'index': 1,
                        },
                    'text': text
                    }
                },

            {
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': 1,
                        'endIndex':  1
                        },
                    'paragraphStyle': {
                        'namedStyleType': 'HEADING_1',
                        },
                    'fields': 'namedStyleType,spaceAbove,spaceBelow'
                    }
                }
            ]
    docs.documents().batchUpdate(documentId = doc_id,body={'requests':requests}).execute()
