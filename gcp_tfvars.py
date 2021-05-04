import os

from gcp_define import * #azure define data

def tfvars_data(data, project, bv_size):
    ret = "#provider\n"
    temp = "gcp_credentials           = \"{gcp_credentials_file}\"\n".format(gcp_credentials_file = data["gcp_credentials_file"])
    temp = temp.replace("\\", "\\\\")
    ret += temp
    ret += "gcp_project               = \"{gcp_project}\"\n".format(gcp_project = project)
    ret += "gcp_region                = \"{gcp_region}\"\n".format(gcp_region = data["region"])
    ret += "gcp_zone                  = \"{gcp_zone}\"\n\n\n".format(gcp_zone = data["zone"])


    ret += "#vm_images\n"
    if data["vm_images"] == "centos7":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["centos7"]["image"])

    elif data["vm_images"] == "centos8":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["centos8"]["image"])

    elif data["vm_images"] == "debian9":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["debian9"]["image"])

    elif data["vm_images"] == "debian10":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["debian10"]["image"])

    elif data["vm_images"] == "redhat7":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["redhat7"]["image"])

    elif data["vm_images"] == "redhat8":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["redhat8"]["image"])
    
    elif data["vm_images"] == "ubuntu16pro":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["ubuntu16pro"]["image"])

    elif data["vm_images"] == "ubuntu18pro":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["ubuntu18pro"]["image"])

    elif data["vm_images"] == "ubuntu20pro":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["ubuntu20pro"]["image"])
    
    elif data["vm_images"] == "ubuntu16":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["ubuntu16"]["image"])

    elif data["vm_images"] == "ubuntu18":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["ubuntu18"]["image"])

    elif data["vm_images"] == "windows2019":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["windows2019"]["image"])

    elif data["vm_images"] == "windows2016":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["windows2016"]["image"])

    elif data["vm_images"] == "windows2012-r2":
        ret += "vm_images                 = \"{vm_images}\"\n\n\n".format(vm_images = gcp_images["windows2012-r2"]["image"])


    ret += "#instnace\n"
    ret += "vm_name                   = \"{vm_name}\"\n".format(vm_name = data["vm_name"])
    ret += "vm_size                   = \"{vm_size}\"\n".format(vm_size = data["vm_size"])
    if data["vm_images"].find("windows") != -1:
        ret += "vm_metadata_starup_script = \"GCP_win_agent.ps1\"\n\n\n"
    else:
        ret += "vm_metadata_starup_script = \"GCP_linux_agent.sh\"\n"
        temp = "vm_ssh_keys               = \"{vm_ssh_keys}\"\n\n\n".format(vm_ssh_keys = data["vm_ssh_keys"])
        temp = temp.replace("\\", "\\\\")
        ret += temp

    
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
        f = open("./gcp_win/vars.tfvars", 'w')
        f.write(ret)
    else:
        f = open("./gcp_linux/vars.tfvars", 'w')
        f.write(ret)


def make_tfvars(data, project, bv_size):
    ret = tfvars_data(data, project, bv_size)
    Print_tfvars(data, ret)
    return