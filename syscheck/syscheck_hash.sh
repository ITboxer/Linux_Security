#!/bin/bash

ds="`date`"

dt="`date "+%Y%m%d%H%M"`"
acc=$1
com=$(hostname -s)
com_syschk=$com\_syschk_hash\_$dt
rm -rf $com_syschk

mkdir $com_syschk

clear

# Hash
h01=$com_syschk"/h01.filehash.log"

######################
# File Hash
######################
echo -e "\033[1;36m============================================"
echo -e "* File Hash "
echo -e "bypass hanging system file or set timeout"
echo -e "find / -type f -exec timeout 1s md5sum ""{}"" +"
echo -e "find / -not -path "/proc/*" -not -path "/sys/*" -type f -exec md5sum "{}" +"
echo -e "============================================\033[0;0m"

find / -type f -exec timeout 1s md5sum "{}" +                             2>/dev/null  >> $h01
#find / -not -path "/proc/*" -not -path "/sys/*" -type f -exec md5sum "{}" + 2>/dev/null >> $h01

echo -e "\033[1;36m============================================"
echo -e "* FINISH - Result File Packing"
echo -e "============================================\033[0;0m"
echo "# tar -czf $com_syschk.tar.gz $com_syschk"
if [ `which tar | wc -l` -eq 1 ]
  then
    tar -czf $com_syschk.tar.gz $com_syschk
	echo "# rm -rf $com_syschk"
	rm -rf $com_syschk
  else
    echo "  => tar Command Not Found "
fi

echo
echo


