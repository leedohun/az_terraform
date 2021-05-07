import os
import sys
import json
import pandas
import json

from ncp_tfvars import *             #create vars.tfvars
from ncp_userdata_handling import *  #userdata handling (에러 처리)


#read json file
def load_C_VM_json(param):
    user_data_path = './{}.json'.format(param)

    with open(user_data_path, 'r') as f:
        json_data = json.load(f)

    return error_handling(json_data)


#error check
def error_handling(json_data):
    count = len(json_data)

    bv_size = []
    #error hadling
    for cnt in range(0, count):
        
        #provider
        try:
            provider(json_data[cnt]["access_key"], json_data[cnt]["secret_key"], json_data[cnt]["region"])
        except Exception as e:
            print(e)
            os.system("timeout /t 10")
            exit(-1)

        #vm_info
        try:
            vm_info(json_data[cnt]["vm_name"], json_data[cnt]["vm_images"], json_data[cnt]["vm_size"], json_data[cnt]["zone"], json_data[cnt]["vm_login_key"])
        except Exception as e:
            print(e)
            os.system("timeout /t 10")
            exit(-1)

        #attach disk
        if json_data[cnt]["bv_size"] == None:
            bv_size.append(50)
        else:
            try:
                bv_size.append(attach_disk_size(json_data[cnt]["bv_size"]))
            except Exception as e:
                print(e)
                os.system("timeout /t 10")
                exit(-1)

    return json_data, bv_size

#excel to json
def e2j(sheet):
    edf = pandas.read_excel('./zconverter.xlsx', sheet_name=sheet)
    str = edf.to_json(orient='records')
    f = open("./{}.json".format(sheet), mode='wt', encoding='utf-8')
    f.write(str)
    f.close()
    
    return load_C_VM_json(sheet)


def run(exe_path):
    data, bv_size = e2j("gcp")
    
    count = len(data)

    for cnt in range(0, count):
        make_tfvars(data[cnt], bv_size[cnt])
    

def main(exe_path):
    run(exe_path)


main(sys.argv[0])