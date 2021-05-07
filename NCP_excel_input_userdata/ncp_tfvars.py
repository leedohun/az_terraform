import os

from ncp_define import * #azure define data

def tfvars_data(data, bv_size):
    ret = "#provider\n"
    ret += "ncp_access_key = \"{ncp_access_key}\"\n".format(ncp_access_key = data["access_key"])
    ret += "ncp_secret_key = \"{ncp_secret_key}\"\n".format(ncp_secret_key = data["secret_key"])
    ret += "ncp_region     = \"{ncp_region}\"\n\n\n".format(ncp_region = data["region"])


    ret += "#vm instnace\n"
    ret += "vm_name                      = \"{vm_name}\"\n".format(vm_name = data["vm_name"])
    if data["vm_images"] == "centos6":
        ret += "vm_server_image_product_code = \"{vm_images}\"\n".format(vm_images = ncp_images["centos6"]["image"])

    elif data["vm_images"] == "centos7":
        ret += "vm_server_image_product_code = \"{vm_images}\"\n".format(vm_images = ncp_images["centos7"]["image"])
    
    elif data["vm_images"] == "ubuntu16":
        ret += "vm_server_image_product_code = \"{vm_images}\"\n".format(vm_images = ncp_images["ubuntu16"]["image"])

    elif data["vm_images"] == "ubuntu18":
        ret += "vm_server_image_product_code = \"{vm_images}\"\n".format(vm_images = ncp_images["ubuntu18"]["image"])

    elif data["vm_images"] == "windows2012-r2":
        ret += "vm_server_image_product_code = \"{vm_images}\"\n".format(vm_images = ncp_images["windows2012-r2"]["image"])

    elif data["vm_images"] == "windows2016":
        ret += "vm_server_image_product_code = \"{vm_images}\"\n".format(vm_images = ncp_images["windows2016"]["image"])

    ret += "vm_server_product_code       = \"{vm_size}\"\n".format(vm_size = data["vm_size"])
    ret += "vm_zone                      = \"{vm_zone}\"\n".format(vm_zone = data["zone"])
    if data["vm_images"].find("windows") != -1:
        ret += "vm_user_data = \"ncp_win_agent.ps1\"\n\n\n"
    else:
        ret += "vm_user_data = \"ncp_linux_agent.sh\"\n\n\n"


    ret += "#vm login key\n"
    ret += "login_key_name = \"{vm_login_key_name}\"\n\n\n".format(vm_login_key_name = data["vm_login_key"])
        
    
    ret += "#create_block\n"
    count = len(bv_size)
    ret += "bv_count                  = \"{bv_count}\"\n".format(bv_count = count)

    #add volume name
    ret += "bv_display_name           = ["
    for cnt in range(0, count):
        ret += "\"{bv_diskplay_name}\"".format(bv_diskplay_name = data["vm_name"] + "-" + str(cnt))
        
        if cnt < count - 1:
            ret += ","
        else:
            ret += "]"
    ret += "\n"

    #add volume size
    ret += "bv_size                   = {bv_size}\n".format(bv_size = bv_size)

    return ret


def Print_tfvars(data, ret):
    if(data["vm_images"].find("windows") != -1):
        f = open("./ncloud_win/vars.tfvars", 'w')
        f.write(ret)
    else:
        f = open("./ncloud_lin/vars.tfvars", 'w')
        f.write(ret)


def make_tfvars(data, bv_size):
    ret = tfvars_data(data, bv_size)
    Print_tfvars(data, ret)
    return