# -*- coding: utf-8 -*- 
import os 
import sys
import json

db_scripts = 'conf.d/scripts.json'
script_path = './packages'

list_scripts = os.listdir(script_path)
load_dbScripts = json.loads(open(db_scripts).read())
load_dbScripts["scripts"] = list_scripts
dump_list = open(db_scripts, 'w')
dump_list.write(json.dumps(load_dbScripts, indent=4))
dump_list.close()
print (load_dbScripts)
for script in json.loads(open(db_scripts).read())["scripts"]:
    execute = 'python3 packages/%s' %script
    os.system(execute)

