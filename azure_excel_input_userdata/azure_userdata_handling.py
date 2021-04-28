from azure_define import * #azure define data

#provider error handling
def provider(az_subscription_id, az_tenant_id, az_client_id, az_client_secret):
    if az_subscription_id == None:
        raise Exception("userdata_az_subscription_id_err")
    if az_tenant_id == None:
        raise Exception("userdata_az_tenant_id_err")
    if az_client_id == None:
        raise Exception("userdata_az_client_id_err")
    if az_client_secret == None:
        raise Exception("userdata_az_client_secret_err")



#resource_group / region error handling
def resource_region(group_name, region):
    if group_name == None:
        raise Exception("userdata_group_name_err")
    if region == None:
        raise Exception("userdata_region_err")
    else:
        cnt = len(azure_region)

        #azure 내에 존재하는 region인지 판별
        for n in range(0, cnt):
            if azure_region[n] == region:
                break

            if n == cnt - 1:
                raise Exception("userdata_region_err")



def vm_info(vm_images, vm_name, vm_size):  
    if vm_images == None:
        raise Exception("userdata_vm_images_err")

    else:
        #vm_images matching
        if vm_images != "centos7" and vm_images != "debian10" and vm_images != "redhat7" and vm_images != "ubuntu18" and vm_images != "windows2019" and vm_images != "windows2016" and vm_images != "windows2012-r2" and vm_images != "windows2012" and vm_images != "windows2008-r2":
            raise Exception("userdata_vm_images_err")

    if vm_name == None:
        raise Exception("userdata_vm_name_err")
    if vm_size == None:
        raise Exception("userdata_vm_size_err")



def vm_admin(vm_admin_username, vm_admin_password):
    if vm_admin_username == None:
        raise Exception("userdata_vm_admin_username_err")
    else:
        if vm_admin_username[0] == "-" or "0" <= vm_admin_username[0] <= "9":
            raise Exception("userdata_vm_admin_username_err")
        elif 64 < len(vm_admin_username):
            raise Exception("userdata_vm_admin_username_err")

        for n in vm_admin_username:
            if n == "-" or "0" <= n <= "9" or "A" <= n <= "Z" or "a" <= n <= "z":
                continue
            else:
                raise Exception("userdata_vm_admin_username_err")

    if vm_admin_password == None:
        raise Exception("userdata_vm_admin_username_err")



def attach_disk_size(bv_size):
    temp = []
    data = ""
    
    for n in bv_size:
        if n == "[" or n == " ":
            continue

        elif n == "," or n == "]":
            temp.append(int(data))
            if temp[-1] < 10:
                raise Exception("userdata_disk_size_err")
            data = ""

        elif n == "0" or n == "1" or n == "2" or n == "3" or n == "4" or n == "5" or n == "6" or n == "7" or n == "8" or n == "9":
            data += n

        else:
            raise Exception("invalid value")

    return temp
