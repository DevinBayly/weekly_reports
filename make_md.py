import datetime
import yaml

def run():
    now = datetime.datetime.now()
    with open("first_doc.yaml","r") as phile:
        # projects
        p = yaml.full_load(phile)

    with open("my_doc.md","w") as phile:
        dc = p["detailed_collection"]
        phile.write(f"# Data & Visualization Weekly Projects Report {now:%Y}_{now:%m}_{now:%d}\n")
        phile.write(f"\n## Active Projects \n\n")
        phile.write(f"\n### Active Development \n\n")
        for p_name_key in dc:
            deets = dc[p_name_key]
            print(deets["status"])
            if deets["status"] == "active":
                phile.write(f"* {p_name_key} \n")
                ## go through the under points
                ## this will be a nested list
                print(deets)
                if deets["updates"] != None and len(deets["updates"]) > 0:
                    latest = deets["updates"][0]
                    for update in latest:
                        phile.write(f"\t * {update}\n")
        phile.write(f"\n\n### Consultations \n\n")
        for p_name_key in dc:
            deets = dc[p_name_key]
            if deets["type"] == "consult":
                phile.write(f"* {p_name_key} \n")
        phile.write(f"\n## Upcoming \n\n")
        for p_name_key in dc:
            deets = dc[p_name_key]
            if deets["status"] == "upcoming":
                phile.write(f"* {p_name_key} \n")
        phile.write(f"\n\n## Completed For Fiscal Year \n\n")
        ## sections for this
        # workshop section
        phile.write(f"\n\n### Workshops/Trainings \n\n")
        section_fill(dc,phile,"complete","workshop")
        # collabs
        phile.write(f"\n\n### Completed Projects/Collaborations \n\n")
        section_fill(dc,phile,"complete","collaboration")
        #infra
        phile.write(f"\n\n### Infrastructure Developed \n\n")
        section_fill(dc,phile,"complete","infrastructure")
        #protocols and analysis
        phile.write(f"\n\n### Protocols and Analysis Developed \n\n")




def section_fill(dc,phile,status,type):
    for p_name_key in dc:
        deets = dc[p_name_key]
        if deets["status"] == status and deets["type"] == type:
            phile.write(f"* {p_name_key} \n")

