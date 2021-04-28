import os

from azure_define import * #azure define data

def tfvars_data(data, bv_size):
    ret = "#provider\n"
    ret += "az_subscription_id        = \"{az_subscription_id}\"\n".format(az_subscription_id = data["az_subscription_id"])
    ret += "az_tenant_id              = \"{az_tenant_id}\"\n".format(az_tenant_id = data["az_tenant_id"])
    ret += "az_client_id              = \"{az_client_id}\"\n".format(az_client_id = data["az_client_id"])
    ret += "az_client_secret          = \"{az_client_secret}\"\n\n\n".format(az_client_secret = data["az_client_secret"])

    ret += "#create_vm_resource\n"
    ret += "group_name                = \"{group_name}\"\n".format(group_name = data["group_name"])
    ret += "region                    = \"{region}\"\n\n\n".format(region = data["region"])

    ret += "#network, subnet, public_ip, network interface, security group\n"
    ret += "nw_name                   = \"{nw_name}\"\n".format(nw_name = data["vm_name"] + "-network")
    ret += "sb_name                   = \"{sb_name}\"\n".format(sb_name = data["vm_name"] + "-subnet")
    ret += "ip_name                   = \"{ip_name}\"\n".format(ip_name = data["vm_name"] + "-publicIp")
    ret += "nic_name                  = \"{nic_name}\"\n".format(nic_name = data["vm_name"] + "-nic")
    ret += "nic_ip_configuration_name = \"{nic_ip_configuration_name}\"\n".format(nic_ip_configuration_name = data["vm_name"] + "-nicIp")
    ret += "sg_name                   = \"{sg_name}\"\n\n\n".format(sg_name = data["vm_name"] + "-network")

    ret += "#vm_images\n"
    if data["vm_images"] == "centos7":
        ret += "offer     = \"{offer}\"\n".format(offer = azure_images["centos7"]["offer"])
        ret += "publisher = \"{publisher}\"\n".format(publisher = azure_images["centos7"]["publisher"])
        ret += "sku       = \"{sku}\"\n".format(sku = azure_images["centos7"]["sku"])
        ret += "version   = \"{version}\"\n\n\n".format(version = azure_images["centos7"]["version"])

    elif data["vm_images"] == "debian10":
        ret += "offer     = \"{offer}\"\n".format(offer = azure_images["debian10"]["offer"])
        ret += "publisher = \"{publisher}\"\n".format(publisher = azure_images["debian10"]["publisher"])
        ret += "sku       = \"{sku}\"\n".format(sku = azure_images["debian10"]["sku"])
        ret += "version   = \"{version}\"\n\n\n".format(version = azure_images["debian10"]["version"])

    elif data["vm_images"] == "redhat7":
        ret += "offer     = \"{offer}\"\n".format(offer = azure_images["redhat7"]["offer"])
        ret += "publisher = \"{publisher}\"\n".format(publisher = azure_images["redhat7"]["publisher"])
        ret += "sku       = \"{sku}\"\n".format(sku = azure_images["redhat7"]["sku"])
        ret += "version   = \"{version}\"\n\n\n".format(version = azure_images["redhat7"]["version"])

    elif data["vm_images"] == "ubuntu18":
        ret += "offer     = \"{offer}\"\n".format(offer = azure_images["ubuntu18"]["offer"])
        ret += "publisher = \"{publisher}\"\n".format(publisher = azure_images["ubuntu18"]["publisher"])
        ret += "sku       = \"{sku}\"\n".format(sku = azure_images["ubuntu18"]["sku"])
        ret += "version   = \"{version}\"\n\n\n".format(version = azure_images["ubuntu18"]["version"])

    elif data["vm_images"] == "windows2019":
        ret += "offer     = \"{offer}\"\n".format(offer = azure_images["windows2019"]["offer"])
        ret += "publisher = \"{publisher}\"\n".format(publisher = azure_images["windows2019"]["publisher"])
        ret += "sku       = \"{sku}\"\n".format(sku = azure_images["windows2019"]["sku"])
        ret += "version   = \"{version}\"\n\n\n".format(version = azure_images["windows2019"]["version"])

    elif data["vm_images"] == "windows2016":
        ret += "offer     = \"{offer}\"\n".format(offer = azure_images["windows2016"]["offer"])
        ret += "publisher = \"{publisher}\"\n".format(publisher = azure_images["windows2016"]["publisher"])
        ret += "sku       = \"{sku}\"\n".format(sku = azure_images["windows2016"]["sku"])
        ret += "version   = \"{version}\"\n\n\n".format(version = azure_images["windows2016"]["version"])

    elif data["vm_images"] == "windows2012-r2":
        ret += "offer     = \"{offer}\"\n".format(offer = azure_images["windows2012"]["offer"])
        ret += "publisher = \"{publisher}\"\n".format(publisher = azure_images["windows2012"]["publisher"])
        ret += "sku       = \"{sku}\"\n".format(sku = azure_images["windows2012"]["sku"])
        ret += "version   = \"{version}\"\n\n\n".format(version = azure_images["windows2012"]["version"])

    elif data["vm_images"] == "windows2012":
        ret += "offer     = \"{offer}\"\n".format(offer = azure_images["windows2012"]["offer"])
        ret += "publisher = \"{publisher}\"\n".format(publisher = azure_images["windows2012"]["publisher"])
        ret += "sku       = \"{sku}\"\n".format(sku = azure_images["windows2012"]["sku"])
        ret += "version   = \"{version}\"\n\n\n".format(version = azure_images["windows2012"]["version"])

    elif data["vm_images"] == "windows2008-r2":
        ret += "offer     = \"{offer}\"\n".format(offer = azure_images["windows2008-r2"]["offer"])
        ret += "publisher = \"{publisher}\"\n".format(publisher = azure_images["windows2008-r2"]["publisher"])
        ret += "sku       = \"{sku}\"\n".format(sku = azure_images["windows2008-r2"]["sku"])
        ret += "version   = \"{version}\"\n\n\n".format(version = azure_images["windows2008-r2"]["version"])


    ret += "#instnace\n"
    ret += "vm_name           = \"{vm_name}\"\n".format(vm_name = data["vm_name"])
    ret += "vm_size           = \"{vm_size}\"\n".format(vm_size = data["vm_size"])
    ret += "vm_os_disk_name   = \"{vm_os_disk_name}\"\n".format(vm_os_disk_name = data["vm_name"] + "-os-disk")
    ret += "vm_admin_username = \"{vm_admin_username}\"\n".format(vm_admin_username = data["vm_admin_username"])
    if data["vm_images"].find("windows") != -1:
        ret += "vm_admin_password = \"{vm_admin_password}\"\n".format(vm_admin_password = data["vm_admin_password"])
    else:
        ret += "vm_public_key     = \"{vm_admin_password}\"\n".format(vm_admin_password = data["vm_admin_password"])

    
    ret += "#create_block\n"
    bv_lun = []
    count = len(bv_size)

    ret += "bv_count         = \"{bv_count}\"\n".format(bv_count = count)

    #add volume name
    ret += "bv_display_name  = ["
    for cnt in range(0, count):
        bv_lun.append(cnt)

        ret += "\"{bv_diskplay_name}\"".format(bv_diskplay_name = data["vm_name"] + "_" + str(cnt))
        
        if cnt < count - 1:
            ret += ","
        else:
            ret += "]"
    ret += "\n"

    #add volume size
    ret += "bv_size          = {bv_size}\n".format(bv_size = bv_size)
    ret += "bv_lun           = {bv_lun}\n\n\n".format(bv_lun = bv_lun)


    ret += "#run-command\n"
    if data["vm_images"].find("windows") != -1:
        ret += "rc_name   = script\n"
        ret += "rc_script = ./az_win_agent.ps1\n\n"
    else:
        ret += "\"rc_name   = script\"\n"
        ret += "\"rc_script = ./az_linux_agent.sh\"\n\n"

    return ret


def Print_tfvars(data, ret):
    if(data["vm_images"].find("windows") != -1):
        f = open("./azure_win/vars.tfvars", 'w')
        f.write(ret)
    else:
        f = open("./azure_linux/vars.tfvars", 'w')
        f.write(ret)


def make_tfvars(data, bv_size):
    ret = tfvars_data(data, bv_size)
    Print_tfvars(data, ret)
    return