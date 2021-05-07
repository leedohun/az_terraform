from ncp_define import * #azure define data


#provider error handling
def provider(ncp_access_key, ncp_secret_key, ncp_region):
    if ncp_access_key == None:
        raise Exception("userdata_ncp_access_key_err")
    if ncp_secret_key == None:
        raise Exception("userdata_ ncp_secret_key_err")
    if ncp_region == None:
        raise Exception("userdata_ ncp_region_err")
    else:
        cnt = len(region)
        #ncp 내에 존재하는 region인지 판별
        for n in range(0, cnt):
            if ncp_region == region[n]:
                break
            if n == cnt - 1:
                raise Exception("userdata_ ncp_region_err")



#vm_info
def vm_info(vm_name, vm_images, vm_size, vm_zone, vm_login_key):  
    if vm_images == None:
        raise Exception("userdata_vm_images_err")

    else:
        #vm_images matching
        if vm_images != "centos6" and vm_images != "centos7" and vm_images != "ubuntu16" and vm_images != "ubuntu18" and vm_images != "windows2016" and vm_images != "windows2012-r2":
            raise Exception("userdata_vm_images_err")

    if vm_name == None:
        raise Exception("userdata_vm_name_err")
    else:
        if 3 > len(vm_name) or 15 < len(vm_name):
            raise Exception("userdata_vm_name_err")
    
    if vm_size == None:
        raise Exception("userdata_vm_size_err")
    else:
        if vm_images == "centos6":
            cnt = len(ncp_centos6_vm_size)
            
            for n in range(0, cnt):
                if vm_size == ncp_centos6_vm_size[n]:
                    break
                if n == cnt - 1:
                    raise Exception("userdata_centos6_vm_size_err")

        elif vm_images == "centos7":
            cnt = len(ncp_centos7_vm_size)
            
            for n in range(0, cnt):
                if vm_size == ncp_centos7_vm_size[n]:
                    break
                if n == cnt - 1:
                    raise Exception("userdata_centos7_vm_size_err")

        elif vm_images == "ubuntu16":
            cnt = len(ncp_ubuntu16_vm_size)
            
            for n in range(0, cnt):
                if vm_size == ncp_ubuntu16_vm_size[n]:
                    break
                if n == cnt - 1:
                    raise Exception("userdata_ubuntu16_vm_size_err")
        
        elif vm_images == "ubunutu18":
            cnt = len(ncp_ubuntu18_vm_size)
            
            for n in range(0, cnt):
                if vm_size == ncp_ubuntu18_vm_size[n]:
                    break
                if n == cnt - 1:
                    raise Exception("userdata_ubunutu18_vm_size_err")
        
        elif vm_images == "windows2012-r2":
            cnt = len(ncp_windows2012_r2_vm_size)
            
            for n in range(0, cnt):
                if vm_size == ncp_windows2012_r2_vm_size[n]:
                    break
                if n == cnt - 1:
                    raise Exception("userdata_windows2012-r2_vm_size_err")

        elif vm_images == "windows2016":
            cnt = len(ncp_windows2016_vm_size)
            
            for n in range(0, cnt):
                if vm_size == ncp_windows2016_vm_size[n]:
                    break
                if n == cnt - 1:
                    raise Exception("userdata_windows2016_vm_size_err")


    if vm_zone == None:
        raise Exception("userdata_vm_zone_err")

    if vm_login_key == None:
        raise Exception("userdata_vm_login_key_err")



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