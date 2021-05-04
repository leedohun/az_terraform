from gcp_define import * #azure define data

#provider error handling
def provider(provider_data):
    if provider_data == None:
        raise Exception("userdata_gcp_credentials_err")
    if provider_data["type"] == None:
        raise Exception("userdata_ gcp_credentials_type_err")
    if provider_data["project_id"] == None:
        raise Exception("userdata_ gcp_credentials_project_id_err")
    if provider_data["private_key_id"] == None:
        raise Exception("userdata_ gcp_credentials_private_key_id_err")
    if provider_data["private_key"] == None:
        raise Exception("userdata_ gcp_credentials_private_key_err")
    if provider_data["client_email"] == None:
        raise Exception("userdata_ gcp_credentials_client_email_err")
    if provider_data["client_id"] == None:
        raise Exception("userdata_ gcp_credentials_client_id_err")
    if provider_data["auth_uri"] == None:
        raise Exception("userdata_ gcp_credentials_auth_uri_err")
    if provider_data["token_uri"] == None:
        raise Exception("userdata_ gcp_credentials_token_uri_err")
    if provider_data["auth_provider_x509_cert_url"] == None:
        raise Exception("userdata_ gcp_credentials_auth_provider_x509_cert_url_err")
    if provider_data["client_x509_cert_url"] == None:
        raise Exception("userdata_ gcp_credentials_client_x509_cert_url_err")
    
    return provider_data["project_id"]



#resource_group / region error handling
def region(region, zone):
    if region == None:
        raise Exception("userdata_region_err")
    else:
        cnt = len(gcp_region)

        #gcp 내에 존재하는 region인지 판별
        for n in range(0, cnt):
            if gcp_region[n] == region:
                break

            if n == cnt - 1:
                raise Exception("userdata_region_err")
    
    if zone == None:
        raise Exception("userdata_zone_err")
    else:
        cnt = len(gcp_zone)

        #gcp 내에 존재하는 zone인지 판별
        for n in range(0, cnt):
            if gcp_zone[n] == zone:
                break

            if n == cnt - 1:
                raise Exception("userdata_zone_err")



#vm_info
def vm_info(vm_images, vm_name, vm_size, vm_ssh_key):  
    if vm_images == None:
        raise Exception("userdata_vm_images_err")

    else:
        #vm_images matching
        if vm_images != "centos7" and vm_images != "centos8" and vm_images != "debian9" and vm_images != "debian10" and vm_images != "redhat7" and vm_images != "redhat8" and vm_images != "ubuntu16pro" and vm_images != "ubuntu18pro" and vm_images != "ubuntu20pro" and vm_images != "ubuntu16" and vm_images != "ubuntu18" and vm_images != "windows2019" and vm_images != "windows2016" and vm_images != "windows2012-r2":
            raise Exception("userdata_vm_images_err")

    if vm_name == None:
        raise Exception("userdata_vm_name_err")
    else:
        if vm_name[0] == "-" or "0" <= vm_name[0] <= "9":
            raise Exception("userdata_vm_name_err")
        elif 60 < len(vm_name):
            raise Exception("userdata_vm_name_err")

        for n in vm_name:
            if n == "-" or "0" <= n <= "9" or "A" <= n <= "Z" or "a" <= n <= "z":
                continue
            else:
                raise Exception("userdata_vm_name_err")
    
    if vm_size == None:
        raise Exception("userdata_vm_size_err")

    if vm_images.find("windows") == -1:
        if vm_ssh_key == None:
            raise Exception("userdata_vm_ssh_key_err")


#attach disk
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
