import yaml
from copy import deepcopy

doc = yaml.load(open("updates.yaml").read(),Loader=yaml.Loader)

deets = doc["detailed_collection"]
template = doc["detailed_collection"][0]

def addUpdates(deet):
    print()
    [name,info] = deet
    line = input(f"updates for {name}, enter 'no' if not: ").strip()
    new_updates = []
    if line == "no" or line == "":
        info["newUpdates"] = False
    else:
        info["newUpdates"] = True
        while not line == "done" and not line == "":
            new_updates.append(line)
            line = input(f"updates for {name} write 'done' or '' to stop: ").strip()
        print("adding",new_updates," to info")
        info["updates"].insert(0,new_updates)

for element in deets[1:]:
    [name,info] = element
    if info["status"] == "active" :
        print(name)
        print("active project")
        addUpdates(element)

## adding new projects section
new_proj = input("add new project by name? ").strip()
while not new_proj == "no" and not new_proj == '':
    new_proj_obj = deepcopy(template)
    print(new_proj_obj)
    new_proj_obj[0] = new_proj
    print(new_proj_obj)
    new_proj_obj[1]["type"] = input("collaboration/consult/infrastructure? ").strip()
    ## get rid of None update
    addUpdates(new_proj_obj)
    ## insert it into the doc
    deets.insert(1,new_proj_obj)
    new_proj = input("add new project by name? ").strip()



##write out the result
with open("test.yml","w") as phile:
    phile.write(yaml.dump(doc,default_flow_style= False))



