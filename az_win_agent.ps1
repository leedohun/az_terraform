$ZCM_IP="www.z-cloud.net"
$USER="admin@zconverter.com"
$ZCM_IPaddress="150.136.194.83"

$dir=echo $env:temp

ipconfig > $dir/result.txt
ipconfig > c:\reuslt.txt

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls, [Net.SecurityProtocolType]::Tls11, [Net.SecurityProtocolType]::Tls12, [Net.SecurityProtocolType]::Ssl3
[Net.ServicePointManager]::SecurityProtocol = "Tls, Tls11, Tls12, Ssl3"

Invoke-WebRequest -Uri http://$ZCM_IP/Download/ZConverter_CloudTargetClient_Setup_last_1.exe -Outfile $dir/agent.exe
powershell.exe -command "$dir/agent.exe /zcm $ZCM_IPaddress /user $USER"
Invoke-WebRequest -Uri http://$ZCM_IP/Download/WinInitScript.cmd -Outfile $dir/WinInitScript.cmd
powershell.exe -command "cmd.exe /c $dir/WinInitScript.cmd"