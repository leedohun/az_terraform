Ncloud Terraform
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

         ![마이페이지](https://objectstorage.ap-seoul-1.oraclecloud.com/p/PqEI9b5WyXfYw8rOV8KRu6Vmc2uk3wpez6kWMBgY2NyXEzHiw1TELCATXj0R0X9H/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80.png)

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

네이버 [VM 생성 인증키가 없을때](https://www.ncloud.com/guideCenter/guide/1),

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

         ![Terraform_exe 실행](https://objectstorage.ap-seoul-1.oraclecloud.com/p/sBPr_TVmUalVBtAQ2zqjqRI4BsjVYR9JECDWvo4UpVNa3ZBMD6WCV8U9MqCc3pgh/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/terraform_exe%20%EC%8B%A4%ED%96%89.png)

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

   1. **Download [Terraform data](https://objectstorage.ap-seoul-1.oraclecloud.com/p/T1KjlDXIcedXa59nAo3Jjx5lEjwE39a76qlCWfm9Z9OcNnOcDCIyvX0qlIVIBGXv/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/NBP_terraform.zip)**

   2. **Unzip OCI Terraform data**

      ![Ncloud terraform data](https://objectstorage.ap-seoul-1.oraclecloud.com/p/nm7G6MoiHQmCtLhT8YbSkpRlhUgixwlxRgiQWm9_lP-wa2-QgF2viZLssB0ZF2Sm/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/Unzip.png)



## Terraform 시작

   1. **원하는 서버에 맞게 vars.tfvars 파일을 수정**

      ![vars.tfvars](https://objectstorage.ap-seoul-1.oraclecloud.com/p/Ti1ET7cJke1eJysmdCONyCps49CAsoSfP8jHOrvEZgbb0PKiZdPspIWqUJQy0HSo/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/vars.tfvars.png)

      * vars.tfvars data 정보:
         + access_key_ID : 플랫폼 인증키에서 메모해둔 Access_Key_ID.
         + secret_key : 플랫폼 인증키에서 메모해둔 Secret_Key.
         + region : Use the absolute path of private_key downloaded from API Key generation.
            | | | | | | | |
            |-|-|-|-|-|-|-|
            | region | KR | HK | SGN | JPN | USWN | DEN | 
         + display_name : 생성할 VM의 이름
         + server_image_product_code : 서버 이미지
         + server_product_code : 서버 타입(서버의 크기)
            Ncloud image data를 다운 받은 뒤 server_image_product_code, server_product_code를 기입 (**주의 : 서버 이미지에 맞는 서버 타입을 선택해야 됩니다. windows 서버 이미지의 서버 타입과 linux 서버 이미지의 서버 타입은 다릅니다.**)
            [Ncloud image data](https://objectstorage.ap-seoul-1.oraclecloud.com/p/OnBeJKUea1Q7LbOuZnf2sDBo7ReWJzQXSLKSdIMcLEnqezsch9nu4_0vUBDHXQsE/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/Ncloud_images.txt)
         + zone : region에 맞게 설정해야 됩니다.
            |  KR  |  HK  |  SGN  |  JPN  |  USWN  |  DEN  |
            |------|------|-------|-------|--------|-------|
            | KR-1 | HK-1 | SGN-1 | JPN-1 | USWN-1 | DEN-1 |
            | KR-2 |      |       |       |        |       |
         + access_control_group_configuration_no_list : ACG 생성에서 메모해둔 ACG_ID
         + user_data_path :
            * 다운로드 한 NBP_terraform file의 스크립트 폴더에 **파일 경로를** 기입합니다
            * Linux 계열 운영 체제의 경우 Linux_cloud_init.sh 파일을 사용하고, Windows 계열 운영 체제의 경우 Windows_cloud_init.vbs 파일을 사용합니다.
            * user_data의 스크립트는 수정 가능합니다.
            * **주의 : 경로를 선택할 때는 \ (역슬래쉬)를 2개씩 넣어줍니다. ex. C:\\User\\PC\\Desktop\\NBP_teraform\\~~**
         + login_key : Ncloud 인증키 생성 단계에서 메모한 인증키 이름을 기입합니다.

         + storage_count : 생성을 원하는 Server의 storage 갯수
         + storage_display_name : 생성을 원하는 Server의 storage 이름
         + storage_size : 생성을 원하는 Server의 storage 크기

      ![vars.tfvars example](https://objectstorage.ap-seoul-1.oraclecloud.com/p/fHtcI_vhHkTJ5zHyQlbdnS-3EniyeobFd8LwqfF_4h3IKsu-mGaB7FLhYiU_Wvvt/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/vars.tfvars2.png)

   2. **명령 프롬프트 실행**

      ![cmd](https://objectstorage.ap-seoul-1.oraclecloud.com/p/XzXmdi7e-eQrmxk3S9QpiC62EmqKS7Mui5rav_-8bLONUsFPqIGk24P-FoJmQTu5/n/cnfyb6dq82p9/b/test_bucket/o/start%20cmd.png)

   3. **Terraform.exe 경로로 들어간 뒤 Terraform configuration file이 포함된 디렉토리 초기화**

      ```script
      terraform.exe -chdir={terraform data file path} init
      ```

      **Note**
      * -chdir : Terraform을 실행하는 일반적인 방법은 먼저 .tf루트 모듈에 대한 파일이 포함 된 디렉토리로 전환하여 (예 : cd명령 사용) Terraform이 해당 파일을 자동으로 찾을 수 있도록 하는 것입니다.

      ![terraform init](https://objectstorage.ap-seoul-1.oraclecloud.com/p/3Up84cXPL-nvTG6EOEnQJ_0VbWVZz1ddijuBeXQGexLeHD4syM7yri8-LLMZBpnb/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/terraform%20init.png)
   
      ![terraform init result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/WzWliwHizw7RRVLFuoKlUymc-kZjHBL0W3gswM0LYlpteWTmGDPHTgdKb59H-ZBL/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/terraform%20init%20result.png)


   4. **Terraform이 인프라에 적용하려는 변경 사항을 미리 볼 수있는 실행 계획을 생성합니다. 기본적으로 Terraform이 계획을 생성하면 다음이 수행됩니다.**

      * 이미 존재하는 원격 개체의 현재 상태를 읽고 Terraform 상태가 최신 상태인지 확인합니다.
      * 현재 구성을 이전 상태와 비교하고 차이점을 확인합니다.
      * 적용된 경우 원격 개체가 구성과 일치하도록해야하는 일련의 변경 작업을 제안합니다.

      ```script
      terraform.exe -chdir={terraform data file path} plan -var-file={vars file with user specified name}
      ```

      **Note**
      * -var-file : ["tfvars"파일의 정의](https://www.terraform.io/docs/language/values/variables.html#variable-definitions-tfvars-files)를 사용하여 구성의 루트 모듈에 선언 된 잠재적으로 많은 [입력 변수에](https://www.terraform.io/docs/language/values/variables.html) 대한 값을 설정 [합니다](https://www.terraform.io/docs/language/values/variables.html#variable-definitions-tfvars-files).
      * 이 파일의 이름은 변경하여 사용가능 합니다..

      ![terraform plan](https://objectstorage.ap-seoul-1.oraclecloud.com/p/p383W1M_QfNLOrVgWF4mE00YvY1ZAK4Zas5GeOZ_KuboIFIwZ01ZwBY-6CKtmEtI/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/terraform%20plan.png)

   5. **Terraform 계획에 제안 된 작업을 실행합니다.**

      ```script
      terraform.exe -chdir={terraform data file path} apply -var-file={vars file with user specified name} -auto-approve
      ```
      **Note**
      * -auto-approve : Skips interactive approval of plan before applying. This option is ignored when you pass a previously-saved plan file, because Terraform considers you passing the plan file as the approval and so will never prompt in that case.

      ![terraform apply](https://objectstorage.ap-seoul-1.oraclecloud.com/p/7uWVQkDg5FtJyPkYpYtWFZ8FtFNOpoiB0K_D9MXBPmGLnpodShI_lREPehOaJGPW/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/terraform%20apply.png)

   6. **Result**

      ![terraform apply result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/XNDqDWRH-bJEsQndFC0EOvOwrcAwWuHzwk-BrILgVRKL7ohIhnsRLjrbe51KPK4O/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/terraform%20apply%20result.png)
