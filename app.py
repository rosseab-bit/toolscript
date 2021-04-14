# -*- coding: utf-8 -*- 
import os 
import sys
import json
import time
db_scripts = 'conf.d/scripts.json'
script_path = './packages'

banner = """
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
"""
print ('='*22)
print ('@sbitsar')
print (banner)
print ('    scriptools')
print ('='*22)
print ('Bienvenido a scriptool!')

list_scripts = os.listdir(script_path)
load_dbScripts = json.loads(open(db_scripts).read())
load_dbScripts["scripts"] = list_scripts
dump_list = open(db_scripts, 'w')
dump_list.write(json.dumps(load_dbScripts, indent=4))
dump_list.close()
print (load_dbScripts)
list_scripts_loads = json.loads(open(db_scripts).read())["scripts"]
n = 0
for script in json.loads(open(db_scripts).read())["scripts"]:
    print (str(n)+': '+script)
    n = n+1
option = input('Desea ejecutar todos los scripts? yes/no ')
if option == "yes":
    print ('Se ejecutaran los siguiente scripts')
    n = 0
    for script in json.loads(open(db_scripts).read())["scripts"]:
        print (str(n)+' : '+f"{script}")
        n = n+1
    option = input('Desea continuar: yes/no \n')
    if option == "yes":
        for script in json.loads(open(db_scripts).read())["scripts"]:
            execute = f'python3 packages/{script} 2>>tmp/{script}.err 1>>tmp/{script}.out' 
            print (execute)
    elif option == "no":
        print ('Se cancela la ejecucion de los siguientes scripts:\n')
        n = 0
        for script in json.loads(open(db_scripts).read())["scripts"]:
            print (str(n)+' : '+f"{script}")
            n = n+1
    else:
        print ('La opcion ingresada no se encuentra disponible.')
elif option == "no":
    number_script = input('ingrese el numbero de los scrips a ejecutar separado por una coma ej: 0,1,4 \n')
    scripts_execute = number_script.split(',')
    print ('se ejecutaran los siguientes scripts:')
    print ('-'*20)
    for script in scripts_execute:
        print (list_scripts_loads[int(script)])
    print ('-'*20)
    option = input('Confirma la ejecucion de los scipts? yes/no: \n')
    if option == 'yes':
        print ('Ejecutando scripts')
        time.sleep(1)
        print ('Finaliza la ejecucion')
    elif option == 'no':
        print ('Se cancela la ejecucion de los scripts')
        print ('-'*20) 
        for script in scripts_execute:
            print(list_scripts_loads[int(script)])
        print ('-'*20)
else:
    print ('La opcion ingresada no esta disponible.')
