#provider
az_subscription_id = "fecb4c6d-7a6b-4ba4-b321-4cbfce95f967"
az_tenant_id       = "f79bb0dc-9587-4af1-af54-f79861fcda92"
az_client_id       = "b678f8fa-228b-4236-bb3a-e88ba26cf81b"
az_client_secret   = "a0dpcfPG1dPqRgEmQQRbzS0zs-U6lh.m95"


#create_vm_resource
group_name         = "mig-test"
local              = "koreasouth"


#network
nw_name                                            = "target-azure-nework"

#subnet
sb_name                                            = "target-azure-subnet"

#public_ip
ip_name                                            = "target-azure-publicIp"
ip_allocation_method                               = "Dynamic"

#network interface
nic_name                                           = "target-azure-NIC"
nic_ip_configuration_name                          = "target-azure-nicConfiguration"
nic_ip_configuration_private_ip_address_allocation = "Dynamic"

#security group
sg_name                                            = "target-auzre-ssh"


#images



#instance
vm_name                         = "azure-win"
vm_size                         = "Standard_DS1_v2"
vm_os_disk_name                 = "taget-azure-myOsDisk"
vm_os_disk_caching              = "ReadWrite"
vm_os_disk_storage_account_type = "Premium_LRS"
vm_admin_username               = "zconverter"
vm_admin_password               = "zconp@ssw0rd"


#create_block
bv_count                  = 4
bv_display_name           = ["win_1", "win_2", "win_3", "win_4"]
bv_account_storage_type   = "Standard_LRS"
bv_create_option          = "Empty"
bv_size                   = [10, 20, 30, 40]
bv_lun                    = ["10", "11", "12", "13"]
bv_caching                = "ReadWrite"


#run-command
rc_name                 = "script"
rc_publisher            = "Microsoft.Compute"
rc_type                 = "CustomScriptExtension"
rc_type_handler_version = "1.9"
rc_script               = "az_win_agent.ps1"

