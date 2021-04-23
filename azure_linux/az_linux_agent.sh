#!/bin/sh

yum install wget -y

ZCM_IP=150.136.194.83
USER=admin@zconverter.com

wget -P /tmp/ --tries=200 http://${ZCM_IP}/Download/ZConverter_CloudTargetClient_Setup_V3.4_Build_3073.tar.gz &> /tmp/wget.log --no-check-certificate
sleep 10
tar zxvf /tmp/ZConverter_CloudTargetClient_Setup_V3.4_Build_3073.tar.gz -C /tmp
/tmp/zconverter_install_target/install.sh default2 ${ZCM_IP} ${USER} &

