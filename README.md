# weblogic_jndi_batch_add
quickly to add jndi


# modify config

open linux_start.py or windows_start.py to modify config into ur env setting

```bash
adminUsername="weblogicUserName"
adminPassword="weblogicPassword"
adminURL="t3://localhost:7001"
setDomainEnv='/wls11g/user_projects/domains/base_domain/bin/setDomainEnv.sh'
execWlst='/wls11g/wlserver_10.3/common/bin/wlst.sh'
configFilePath='/home/download/test/testcmd/jdbc_linux/temp/config.py'

```

# jndi datasources

open data.json modify datasource data as json array

```bash
{
  "name":"weblogicDatasourceName",
  "jndiName":"weblogicJndiName(ex:jdbc/myjndi)",
  "dsURL":"datasourceurl",
  "user":"datasourceusername",
  "password":"datasourcepwd",
  "target":"AdminServer"
}
```

# run script

windows
```bash
windows_start.py
```
linux
```bash
python linux_start.py
```

