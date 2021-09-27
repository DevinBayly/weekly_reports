import yaml
import os
import shutil
#import python_quick

with open('updates.yaml','r') as phile:
    contents = yaml.full_load(phile)

def fill_gaps():
    ## this is intended to add other elements to the detailed_collection section
    dc  = contents['detailed_collection']
    attrs = contents['attributes']
    for name in contents['names']:
        dc_ele = dc.get(name.title(),-1)
        ## check whether we have a project by this name yet
        if dc_ele != -1:
        ## this would be where we make sure all the attributes are present
            for attr in attrs:
                if dc_ele.get(attr,-1) == -1:
                    dc_ele[attr] = None
        ## if not 

        if dc_ele == -1:
            dc[name.title()]={attr:None for attr in contents["attributes"]}


    
def save_contents() :
    backups = [f for f in os.listdir() if "backup" in f]
    with open("first_doc.yaml","w") as phile:
        yaml.dump(contents,phile)
    ## this gives us actual empty strings for ease
    with open("first_doc.yaml","r") as phile:
        text_with_nones = phile.read()
    correct_text = text_with_nones.replace("null","")
    shutil.copy("first_doc.yaml",f"first_doc_backup_{len(backups) +1}.yaml")
    with open("first_doc.yaml","w") as phile:
        phile.write(correct_text)

def build_requests_from_yaml():
    # pen the yaml
    with open("first_doc.yaml","r") as phile:
        structured_doc = yaml.full_load(phile)
    # create a string
    result_string = ""
    # parse the yaml
    dc =  structured_doc["detailed_collection"]
    for project_entry in dc:
        result_string += f"*{project_entry}*\n\n"
        pe = dc[project_entry]
        ## go over all the individual attributes of project and add that to the result string
        for attr in pe:
    # add things with the correct headers to the string
            result_string += f"---{attr}---\n\n{pe[attr]}\n\n"


    # then return
    return form_request(result_string)

def form_request(text):
    requests = [
         {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text':text 
            }
        }
    ]
    return requests



def send_to_gdocs(doc_id,requests):
    service = python_quick.build_service()
    service.documents().batchUpdate(documentId=doc_id,body={'requests':requests}).execute()


def full_run():
    fill_gaps()
    save_contents()
    #document_id ="1HLsxu3P6C43GiS3qCAOgv3ZWZcN7Tept4oSdOdR2lIU" 
    #req = build_requests_from_yaml()
    #send_to_gdocs(document_id,req)


