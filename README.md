NBP Terraform
============

> Ncloud 플랫폼 인증키 생성
>
> Ncloud AGC 생성
>
> Ncloud 인증키 설정
>
> Terraform 실행 파일 설치
>
> Ncloud Terraform 데이터 생성
> 
> Terraform 시작



## Ncloud 플랫폼 인증키 생성

만약 Access Key ID, Secret Key를 알고 있다면 메모장에 Access Key ID와 Secret Key를 메모 후 이 단계를 뛰어 넘어도 됩니다.

네이버 클라우드 플랫폼 계정은 이미 가지고 있다고 가정 :

   * 계정 로그인 후 [마이페이지] - [인증키 관리] - [(API 인증키가 없다면) 신규 API 인증키 생성] - [Access Key ID, Secret Key 메모장에 저장]

      1. 마이페이지 - 인증키 관리

         ![마이페이지](https://objectstorage.ap-seoul-1.oraclecloud.com/p/xpXig7xhgLpVhxTxrfFulQMmFPg8nbU6WWMml4iUBWHlBJz2DFYP3u1OpDDLvrCp/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80.png)

      2. 계정 관리 (로그인)

         ![로그인](https://objectstorage.ap-seoul-1.oraclecloud.com/p/hFP79yi_ZCiuDN0YKUIHu6VFOvBPh_EApNesEF2dOeHRKOn0Lv7T4k12HHA9fc70/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/%EB%A1%9C%EA%B7%B8%EC%9D%B8.png)
      
      3. API KEY

         ![API KEY 생성](https://objectstorage.ap-seoul-1.oraclecloud.com/p/bQZjWhh_GWIjD4H9F_VkIIshpx9u18wxURjBthQBEh6ZjS9dcFWC_F6aNCT0XDQo/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/API%20%ED%82%A4.png)

      4. Result

         ![Result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/M-b9GzJwbpZ6Od2fF7Kn1KOxoTZjXd-ESgrsIZYtd0FyvPHpNWESd2Mx-X7ynfwB/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/API%20%ED%82%A4%20%EA%B2%B0%EA%B3%BC.png)



## Ncloud AGC 생성

만약 이 전에 50000-50005 port를 열었던 AGC가 있다면 AGC ID를 메모 후 이 단계를 뛰어 넘어도 됩니다.

   1. Console로 이동

      ![Console](https://objectstorage.ap-seoul-1.oraclecloud.com/p/U89ci1Qh6lvG2V6SN_ZXfxNIsXunRlzN8h4wIKGkCwUkiuI1pbtgAZC495LW0kEX/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ncloud%20Console.png)

   2. Dashboard - Server - ACG로 이동

      ![Dashboard](https://objectstorage.ap-seoul-1.oraclecloud.com/p/rIiwTKEyMh0ne9cFICSvY-1umBhCim-ag2_nNxiDMHFYtaqQiv8WIxe2gd2J-lbw/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/Dashboard.png)

   3. ACG 생성

      ![Create ACG](https://objectstorage.ap-seoul-1.oraclecloud.com/p/UUZQZY-fHcDE-wpyeb7DTTteMQMpbXEQLkL46gmSe56pm9UMwnCsArabeUv-z1Iy/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ACG%20%EC%83%9D%EC%84%B1.png)
      ![Create ACG 2](https://objectstorage.ap-seoul-1.oraclecloud.com/p/JMa_2YA6Ig9C5UzKydh2GvH-_DGLdKnF4cgZK5ba22Ql5pizQRkdkUFOH8ZRVklY/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ACG%20%EC%83%9D%EC%84%B1%202.png)

   4. 생성된 파일 선택 후 ACG 설정

      ![ACG 설정](https://objectstorage.ap-seoul-1.oraclecloud.com/p/GFtBPchY2Arfr3fUYO8MQDZ1QfFh7qQRDY_aAsVxK_BHUFGQwEVDE3kT1yyAOFEC/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ACG%20%EC%84%A4%EC%A0%95.png)

   5. AGC 규칙 설정

      * ZCONVERTER 서비스를 사용하기 위해서는 50000-50005 port가 열려 있어야 됩니다.

         ![AGC 규칙 설정](https://objectstorage.ap-seoul-1.oraclecloud.com/p/QzfUavwD9ZJB0eEs6FpaTNrXvG6PxglbIdBYzxo_58zyG5JSc8pq8HJctf8IqalY/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ACG%20%EA%B7%9C%EC%B9%99%20%EC%84%A4%EC%A0%95.png)

   6. AGC ID 복사 후 메모장에 저장

      ![AGC ID](https://objectstorage.ap-seoul-1.oraclecloud.com/p/nsiPyG26xJHFsmOPqDtYmI0HmjfzXGdl5VyitQXbqeh-paL8GoU-NT56k8NS2KZo/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ACG%20ID.png)
   
   7. Result

      ![Result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/6dXKWD92e6J0tNkLl9xc0Qf0lzg-n4hV0eatk-1YU3lofimrlAumswobSDGUQxwy/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ACG%20result.png)



## Ncloud 인증키 설정

만약 Ncloud VM 인증키가 있다면, 인증키 이름만 메모 후 이 단계를 뛰어 넘어도 됩니다.

네이버 VM 생성 인증키가 없을때,

   1. Console로 이동

      ![Console](https://objectstorage.ap-seoul-1.oraclecloud.com/p/U89ci1Qh6lvG2V6SN_ZXfxNIsXunRlzN8h4wIKGkCwUkiuI1pbtgAZC495LW0kEX/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ncloud%20Console.png)

   2. Dashboard - Server - Server로 이동

      ![Dashboard](https://objectstorage.ap-seoul-1.oraclecloud.com/p/ZbNhVc7U3-ujGt1K_ptx3ZNTU10atQIYn-6GSfwPIBZVltd2Sr_X_SSuZ45pqU_h/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/Server-Server.png)

   3. 서버 생성
   
      ![Server](https://objectstorage.ap-seoul-1.oraclecloud.com/p/vLsPH7OFzjiKZSBiH8gkAwgVvLYU0gvNqnqxxTkDo4xSGK1oQxLdq7CUiqEWsXe7/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/create-Server.png)

   4. 아무 서버 이미지 선택 - 다음 - 다음

      * 이 단계에서는 서버를 생성하지 않고 인증키만 생성하기 때문에 아무 서버를 선택한 다음, 인증키 생성 화면까지 다음을 눌러주시면 됩니다.

         ![Select Server](https://objectstorage.ap-seoul-1.oraclecloud.com/p/dYR4ITd0fHZc9X6Kgyh1CCkqny4Qis5Ly2Y1WYBzEjlKOGj6V9X-u10UV7JS76EW/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/create-Server2.png)
         ![Select Server](https://objectstorage.ap-seoul-1.oraclecloud.com/p/f8UWAN5dZqY5QaFC0NtVPOFdKL-535T3c_21aif1QpPajUmFZGWd9KclXXqFXsAy/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/create-Server3.png)

   5. 인증키 설정 - 새로운 인증키 생성

      * 인증키 이름은 복사 후 메모장에 저장, 인증키는 따로 저장합니다.

         ![Create Key](https://objectstorage.ap-seoul-1.oraclecloud.com/p/TxFIS9okc0S4pi-wzIdQ0u-_CWkA6yQ6Pg06esxrBhbxj_LwwVus7t1jIwa4EDFz/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/create-Server4.png)
   
   6. result

      ![Result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/UkQQdV23cP9IHkD9lfPhF47s7j-6i-YwygsnRjFOhCEvwi4rtxI6iat4W34NaKkA/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/create-Server5.png)



## Terraform 실행 파일 설치

   Terraform은 단일 바이너리 파일로 배포되고 있어 간단하게 설치가 가능합니다. [Terraform 다운로드](https://www.terraform.io/downloads.html) 페이지에서 실행 환경에 맞는 패키지 다운로드를 한 후 압축을 해제하고 별도의 추가 설치 없이 바로 Terraform을 사용할 수 있습니다

   1. Windows os에서 Terraform 사용
   
      * Terraform Download

         ![Windows Terraform Download](https://objectstorage.ap-seoul-1.oraclecloud.com/p/1_S5wae0jd-A1LLRz06SD6yrGNaWsnbrg-cRwaetYWQV0S6IAdHIAgkH0lAkQxuo/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/Windows%20Terraform%20Download.png)

      * 압축 풀기

      * Terraform.exe 파일과 같은 경로에서 Terraform 설치 확인

         ![Terraform_exe 실행](https://objectstorage.ap-seoul-1.oraclecloud.com/p/hm8RVqtYIHaAXaUWDwMoh1IK9r-B3Z4d_PZu7gS_HYs81-bhDZMHumElBzlJrSSn/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/terraform_exe%20%EC%8B%A4%ED%96%89.png)

   2. Linux OS에서 Terraform 사용

      * 설치

         ```script
         root@base-linux : ~# wget https://releases.hashicorp.com/terraform/0.11.8/terraform_0.11.8_linux_amd64.zip
         root@base-linux : ~# unzip terraform_0.11.8_linux_amd64.zip && mv terraform /usr/bin/​
         ```
    
      * 설치 확인

         ```script
         root@base-linux : ~ # terraform version
         Terraform v0.11.8
         ```



## Ncloud Terraform 데이터 생성
   Ncloud 사용하는 **terraform data** 데이터를 다운 받습니다..

   1. **Download [Terraform data](https://objectstorage.ap-seoul-1.oraclecloud.com/p/lj3ohc9QtSOmOmAJb6P8iA3KiqXCWFV-xFLUs3_w80TE06Q_bg7r-wS4seyNoDil/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/NBP_terraform.zip)**

   2. **Unzip OCI Terraform data**

      ![Ncloud terraform data](https://objectstorage.ap-seoul-1.oraclecloud.com/p/nm7G6MoiHQmCtLhT8YbSkpRlhUgixwlxRgiQWm9_lP-wa2-QgF2viZLssB0ZF2Sm/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/Unzip.png)



## Terraform 시작

   1. **원하는 서버에 맞게 vars.tfvars 파일을 수정**

      ![vars.tfvars](https://objectstorage.ap-seoul-1.oraclecloud.com/p/Ti1ET7cJke1eJysmdCONyCps49CAsoSfP8jHOrvEZgbb0PKiZdPspIWqUJQy0HSo/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/vars.tfvars.png)

      * vars.tfvars data 정보:
         + tenancy : Use the tenancy noted in API Key creation.
         + user : Use the user noted in API Key creation.
         + key_file : Use the absolute path of private_key downloaded from API Key generation.
         + fingerprint : Use the fingerprint noted in API Key creation.
         + region : Use the region noted in API Key creation.
         + compartment : Tenancy or compartment for that account
         + shape : 
            - Flexible Shapes : VM.Standard.E3.Flex, VM.Standard.E4.Flex, VM.Optimized3.Flex, VM.Standard.A1.Flex
            - Standard Shapes : VM.Standard2.1, VM.Standard2.2, VM.Standard2.4, VM.Standard2.8, VM.Standard2.16, VM.Standard2.24
         + os :
         + os_version : 
            | | Windows2019 | Windows2016 | Windows2012 R2 | Linux8 | Linux7.9 | Linux6.10 | centos8 | centos7 | centos8 | ubuntu20.04 | ubuntu18.04 | ubuntu16.04 |
            |-|-------------|-------------|----------------|--------|----------|-----------|---------|---------|---------|-------------|-------------|-------------|
            | OS | Windows | Windows | Windows | Oracle Linux | Oracle Linux | Oracle Linux  | CentOS | CentOS | CentOS | Canonical Ubuntu | Canonical Ubuntu | Canonical Ubuntu |
            | OS_Version | Server 2019 Standard | Server 2016 Standard | Server 2012 R2 Standard | 8 | 7.9 | 6.10 | 8 | 7 | 6 | 20.04 | 18.04 | 16.04 |
         + block_volume_count : Number of volumes on server you want to create
         + block_volume_size : Size of volume on server you want to create
         + block_volume_diskplay_name : Name of volume on server you want to create
         + blcok_volume_device_path : Specifies the path to the disk when you add it to the Linux family operating system.
         + diskplay_name : Name of Server you want to
         + subet_ocid : Use the account's subnet_ocid.
         + user_data_path :
            - Enter the path to the txt file in the scripts folder of the downloaded oci_terraform. 
            - Use the file oci_linux_cloud_init_txt for Linux-like operating systems and the file oci_windows_cloud_init_txt for Windows-like operating systems.
         + ssh_public_key_path : Linux-like operating systems require the file path of the user's ssh_public key.
         + ocpus : You must enter the number of CPUs when using Flexible_shape. The range is from 1 to 64.
         + memory_in_gbs : When using Flexible_shape, you must select memory capacity. The range is from cpu count to 1024.

      ![vars.tfvars example](https://objectstorage.ap-seoul-1.oraclecloud.com/p/UUb0M_3gy8hI1CCLZM5cO3q3PLKRyzaoA2GbHs6h4ZRTIO4TJd-lYk61_e1LBboy/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/vars.tfvars%20result.png)

   2. **Start CMD**

      ![cmd](https://objectstorage.ap-seoul-1.oraclecloud.com/p/XzXmdi7e-eQrmxk3S9QpiC62EmqKS7Mui5rav_-8bLONUsFPqIGk24P-FoJmQTu5/n/cnfyb6dq82p9/b/test_bucket/o/start%20cmd.png)

   3. **Go to the file path of Terraform.exe and Initialize the working directory containing the terraform configuration file.**

      ```script
      terraform.exe -chdir={terraform data file path} init
      ```

      **Note**
      * -chdir : The usual way to run Terraform is to first switch to the directory containing the `.tf` files for your root module (for example, using the `cd` command), so that Terraform will find those files automatically without any extra arguments.

      ![terraform init](https://objectstorage.ap-seoul-1.oraclecloud.com/p/PxVvenXLonevJC75fqTtJBehD7AHcSMOaWFoM1OSfUyquxl_uFZ0Z2kjBheE_rz8/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/terraform%20init.png)
   
      ![terraform init result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/5mzjf9AlmTRbUvg2QeSV3RzpqSvDWjqeQVmji9vYBxYqKTeTIrBdqvYySFTweOCC/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/terraform%20init%20result.png)


   4. **Creates an execution plan. By default, creating a plan consists of:**

      * Reading the current state of any already-existing remote objects to make sure that the Terraform state is up-to-date.
      * Comparing the current configuration to the prior state and noting any differences.
      * Proposing a set of change actions that should, if applied, make the remote objects match the configuration.

      ```script
      terraform.exe -chdir={terraform data file path} plan -var-file={vars file with user specified name}
      ```

      **Note**
      * -var-file : Sets values for potentially many [input variables](https://www.terraform.io/docs/language/values/variables.html) declared in the root module of the configuration, using definitions from a ["tfvars" file](https://www.terraform.io/docs/language/values/variables.html#variable-definitions-tfvars-files). Use this option multiple times to include values from more than one file.
      * The file name of vars.tfvars can be changed.

      ![terraform plan](https://objectstorage.ap-seoul-1.oraclecloud.com/p/FvA5NEq3E1wlqv-8HD4SVMjAyXVSWl7Kc8Ot98rs5w3vBgNBIxAp4856DPqTrAiU/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/terraform%20plan.png)

   5. **Executes the actions proposed in a Terraform plan.**

      ```script
      terraform.exe -chdir={terraform data file path} apply -var-file={vars file with user specified name} -auto-approve
      ```
      **Note**
      * -auto-approve : Skips interactive approval of plan before applying. This option is ignored when you pass a previously-saved plan file, because Terraform considers you passing the plan file as the approval and so will never prompt in that case.

      ![terraform apply](https://objectstorage.ap-seoul-1.oraclecloud.com/p/SoxEo0Ow-RjYmndQ6_7Zq03BabF2XEl2TutQCz4WcvWnh0eUIl6T5Shhl-YTyrIy/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/terraform%20apply.png)

   6. **Result**

      ![terraform apply result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/tqi-vkce_08TSsvkoZh-VL1lPxiqWAFaeMGwhKI2RiuFJ08G7buB8ePms0kS-mad/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/terraform%20apply%20result.png)
