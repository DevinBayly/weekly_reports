import yaml

def parse_yaml():
    with open("first_doc.yaml") as phile:
        contents = yaml.full_load(phile)

    requests = []
    ## write it upsidown so the name part has to be the last thing that goes in the request list
    for key in contents["detailed_collection"]:
        dc_ele = contents["detailed_collection"][key]
        print(dc_ele["updates"])
        requests.append({
            'insertText':{
                'location':{
                    'index':1
                },
                'text':f"{dc_ele['updates']}"
            }
        })
        requests.append({
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 1,
                    'endIndex':  1
                    },
                'paragraphStyle': {
                    'namedStyleType': 'NORMAL_TEXT',
                    },
                'fields': 'namedStyleType'
                }
            })
        requests.append(
            {
                'insertText':{
                    'location':{
                        'index':1
                    },
                    'text':key
                }
            })
        requests.append({
            'updateParagraphStyle': {
                'range': {
                    'startIndex': 1,
                    'endIndex':  1
                    },
                'paragraphStyle': {
                    'namedStyleType': 'HEADING_1',
                    },
                'fields': 'namedStyleType'
                }
            })
    return requests



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
