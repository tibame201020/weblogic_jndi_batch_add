import json
import subprocess

#############################################################################
#                                                                           #
#                               config                                      #
#                                                                           #
#############################################################################

adminUsername="weblogicUserName"
adminPassword="weblogicPassword"
adminURL="t3://localhost:7001"
setDomainEnv="D:/Dev/Oracle/wls10/Middleware/user_projects/domains/base_domain/bin/setDomainEnv.cmd"
execWlst="D:/Dev/Oracle/wls10/Middleware/wlserver_10.3/common/bin/wlst.cmd"

#############################################################################
#                                                                           #
#                               script                                      #
#                                                                           #
#############################################################################

with open('data.json') as f:
    data = json.load(f)

for i in data:
    name=i['name']
    jndiName=i['jndiName']
    dsURL=i['dsURL']
    user=i['user']
    password=i['password']
    target=i['target']
    
    copyCmd="xcopy config.py temp /Y"
    subprocess.call(copyCmd, shell=True)
    
    f = open("temp\config.py", "r")
    strs = f.readline().replace('weblogicAdminUsername',adminUsername)
    strs = strs + f.readline().replace('weblogicAdminPassword',adminPassword)
    strs = strs + f.readline().replace('t3://localhost:7001',adminURL)
    strs = strs + f.readline().replace('weblogicDatasourceName',name)
    strs = strs + f.readline().replace('weblogicJndiName',jndiName)
    strs = strs + f.readline().replace('dataSourceUrl',dsURL)
    strs = strs + f.readline().replace('dataSourceUserName',user)
    strs = strs + f.readline().replace('dataSourcePassword',password)
    strs = strs + f.readline().replace('targetServerName',target)
    print(strs)
    line = f.readline()
 
    while line:
        line = f.readline()
        strs = strs + line
    f.close()
    
    w = open("temp\config.py", "w")
    w.writelines(strs)
    w.close()
    
    subprocess.call([setDomainEnv])
    subprocess.call([execWlst, "temp\config.py"])