import yaml
from copy import deepcopy
import uuid
doc = yaml.load(open("updates.yaml").read(),Loader=yaml.Loader)

deets = doc["detailed_collection"]

# want to sort and also add a detail that things are from longer ago

print(deets[-1][1]["status"])

def sort(e):
    if e[1]["status"] =="complete":
        return 5
    else:
        return 0

sd = sorted(deets,key=sort)

for e in sd:
    archive = False
    if e[1]["status"] =="complete":
        archive = True
    e[1]["archive"] = archive



##write out the result
with open(f"test.yml{uuid.uuid1()}","w") as phile:
    phile.write(yaml.dump(sd,default_flow_style= False))

