"""
the goal of this script is to make sure that the names list at the bottom has all the elements that are represented in the individual elements area
"""

import yaml
from copy import deepcopy
import uuid

doc = yaml.load(open("updates.yaml").read(),Loader=yaml.Loader)

deets = doc["detailed_collection"]
template = doc["detailed_collection"][0]

names = doc["names"]
mod = deepcopy(names)
## add to names whats not in deets
for element in deets[1:]:
    [name,info] = element
    found = False
    for name in names:
        if name.lower() == element[0].lower():
            found = True
            break
    if not found:
        mod.insert(0,element[0])
        

set(names).symmetric_difference(set(mod))
doc["names"] = mod

## make sure there is a section in the doc for each named project
for name in names:
    found = False
    for element in deets[1:]:
        if name.lower() == element[0].lower():
            found = True
            break

    if not found:
        print("adding ",name)
        new_proj_obj = deepcopy(template)
        new_proj_obj[0] = name
        print("type?")
        new_proj_obj[1]["type"] = input("collaboration/consult/infrastructure? ").strip()
        print("status?")
        new_proj_obj[1]["status"] = input("active/upcoming? ").strip()
        deets.insert(1,new_proj_obj)



print(doc["names"])
##write out the result
with open(f"test.yml{uuid.uuid1()}","w") as phile:
    phile.write(yaml.dump(doc,default_flow_style= False))


