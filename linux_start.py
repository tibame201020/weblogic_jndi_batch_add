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
setDomainEnv='/wls11g/user_projects/domains/base_domain/bin/setDomainEnv.sh'
execWlst='/wls11g/wlserver_10.3/common/bin/wlst.sh'
configFilePath='/home/download/test/testcmd/jdbc_linux/temp/config.py'


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
    driverClass=i['driverClass']
    
    copyCmd='cp config.py temp/'
    subprocess.call(copyCmd, shell=True)
    
    f = open("temp/config.py", "r")
    strs = f.readline().replace('weblogicAdminUsername',adminUsername)
    strs = strs + f.readline().replace('weblogicAdminPassword',adminPassword)
    strs = strs + f.readline().replace('t3://localhost:7001',adminURL)
    strs = strs + f.readline().replace('weblogicDatasourceName',name)
    strs = strs + f.readline().replace('weblogicJndiName',jndiName)
    strs = strs + f.readline().replace('dataSourceUrl',dsURL)
    strs = strs + f.readline().replace('dataSourceUserName',user)
    strs = strs + f.readline().replace('dataSourcePassword',password)
    strs = strs + f.readline().replace('targetServerName',target)
    strs = strs + f.readline().replace('driverClassName',driverClass)
    print(strs)
    line = f.readline()
 
    while line:
        line = f.readline()
        strs = strs + line
    f.close()
    
    w = open("temp/config.py", "w")
    w.writelines(strs)
    w.close()

     
    subprocess.call(['sh', setDomainEnv])
    subprocess.call(['sh', execWlst, configFilePath])
    