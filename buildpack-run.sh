#!/bin/sh

# this pack is valid for apps with a hello.txt in the root
if [ -f $1/hello.txt ]; then
  echo "HelloFramework"
  exit 0
else
  exit 1
fi


#Create symlinks for tools
sudo ln -sfn /opt/mssql-tools/bin/sqlcmd-13.0.1.0 /usr/bin/sqlcmd 
sudo ln -sfn /opt/mssql-tools/bin/bcp-13.0.1.0 /usr/bin/bcp