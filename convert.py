#!/usr/bin/env python
# coding: utf-8

# In[1]:


import importlib


# In[2]:


import yaml_parse


# In[3]:


# yaml_parse.fill_gaps()
# yaml_parse.save_contents()


# In[4]:


import yaml


# In[5]:




# In[6]:


import datetime

now = datetime.datetime.now()
delt = datetime.timedelta(days=2)
delt
now - delt


# In[7]:


import os 


# In[11]:


import datetime
import yaml
from io import StringIO
import time

def run():
    now = datetime.datetime.now() - datetime.timedelta(days=3)
    
    with open("updates.yaml","r") as phile:
        # projects
        p = yaml.full_load(phile)
    ophile = StringIO()
    dc = p["detailed_collection"]
    ## dc now is a list
    ophile.write(f"# Data & Visualization Weekly Projects Report {now:%Y}_{now:%m}_{now:%d}\n")
    ophile.write(f"\n## Active Projects \n\n")
    ophile.write(f"\n### Active Development  \n\n")
    for el in dc:
        p_name_key = el[0]
        if p_name_key == "Template":
            continue
        ##print(dc,p_name_key)
        deets = el[1]
        #print(deets["status"])
        if deets["status"] == "active" and deets["type"] != "consult":
            ##print("details",p_name_key,deets,"\n\n")
            ophile.write(f"* {p_name_key} \n")
            ## go through the under points
            ## this will be a nested list
            #print(deets)
            if deets["updates"] != None and len(deets["updates"]) > 0:
                latest = deets["updates"][0]
                if not deets["newUpdates"]:
                    print("no updates for ",p_name_key)
                    continue
                for update in latest:
                    ophile.write(f"\t * {update}\n")
    ophile.write(f"\n\n### Consultations \n\n")
    for el in dc:
        p_name_key = el[0]
        ##print(dc,p_name_key)
        deets = el[1]        
        if deets["type"] == "consult" and deets["status"]== "active" and deets["newUpdates"]:
            ##print("details",p_name_key,deets,"\n\n")
            ophile.write(f"* {p_name_key} \n")
            ## go through the under points
            ## this will be a nested list
            #print(deets)
            if deets["updates"] != None and len(deets["updates"]) > 0:
                latest = deets["updates"][0]
                if not deets["newUpdates"]:
                    print("no updates for ",p_name_key)
                    continue
                for update in latest:
                    ophile.write(f"\t * {update}\n")
    ophile.write(f"\n## Upcoming \n\n")
    for el in dc:
        p_name_key = el[0]
        ##print(dc,p_name_key)
        deets = el[1]     
        if deets["status"] == "upcoming":
            ophile.write(f"* {p_name_key} \n")
    ophile.write(f"\n\n## Completed For Fiscal Year \n\n")
    ## sections for this
    # workshop section
    
    ophile.write(f"\n\n### Recently Completed \n\n")
    just_finished(dc,ophile)
    
    ophile.write(f"\n\n### Workshops/Trainings \n\n")
    section_fill(dc,ophile,"complete","workshop")
    # collabs
    ophile.write(f"\n\n### Completed Projects/Collaborations \n\n")
    section_fill(dc,ophile,"complete","collaboration")
     # consults
    ophile.write(f"\n\n### Completed Consultations \n\n")
    section_fill(dc,ophile,"complete","consult")
    #infra
    ophile.write(f"\n\n### Infrastructure Developed \n\n")
    section_fill(dc,ophile,"complete","infrastructure")
    #protocols and analysis
    ophile.write(f"\n\n### Protocols and Analysis Developed \n\n")
    return ophile



def just_finished(dc,ophile):
    for el in dc:
        p_name_key = el[0]
        ##print(dc,p_name_key)
        deets = el[1]
        if deets["status"] == "complete" and deets["newUpdates"] == True:
            ophile.write(f"* {p_name_key} \n")
            #print(deets)
            print(p_name_key)
            links = deets['links']
            for link in links:
                ophile.write(f"\t * {link} \n")


def section_fill(dc,ophile,status,typ):
    for el in dc:
        p_name_key = el[0]
        ##print(dc,p_name_key)
        deets = el[1]
        if deets["status"] == status and deets["type"] == typ:
            ophile.write(f"* {p_name_key} \n")
            #print(deets)
            if status == "complete":
                print(p_name_key)
                links = deets['links']
                if links:
                    for link in links:
                        ophile.write(f"\t * {link} \n")

result = run()
result.seek(0)


result.seek(0)
now = datetime.datetime.now() - datetime.timedelta(days=3)
with open(f"{now:%Y}-{now:%m}-{now:%d}-Data-Vis-Weekly.md","w") as phile:
    phile.write(result.read())
result.seek(0)
with open("convert_temp.md","w") as phile:
    phile.write(result.read())

    
