NBP Terraform
============

> Ncloud 플랫폼 인증키 생성
>
> Ncloud AGC 생성
>
> Terraform 실행 파일 설치
>
> Ncloud Terraform 데이터 생성
> 
> Terraform 시작



## Ncloud 플랫폼 인증키 생성

네이버 클라우드 플랫폼 계정은 이미 가지고 있다고 가정 :

   * 계정 로그인 후 [마이페이지] - [인증키 관리] - [(API 인증키가 없다면) 신규 API 인증키 생성] - [Access Key ID, Secret Key 메모장에 저장]

      1. 마이페이지 - 인증키 관리

         ![마이페이지](https://objectstorage.ap-seoul-1.oraclecloud.com/p/xpXig7xhgLpVhxTxrfFulQMmFPg8nbU6WWMml4iUBWHlBJz2DFYP3u1OpDDLvrCp/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/%EB%A7%88%EC%9D%B4%ED%8E%98%EC%9D%B4%EC%A7%80.png)

      2. 계정 관리 (로그인)

         ![로그인](https://objectstorage.ap-seoul-1.oraclecloud.com/p/hFP79yi_ZCiuDN0YKUIHu6VFOvBPh_EApNesEF2dOeHRKOn0Lv7T4k12HHA9fc70/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/%EB%A1%9C%EA%B7%B8%EC%9D%B8.png)
      
      3. API KEY

         ![API KEY 생성](https://objectstorage.ap-seoul-1.oraclecloud.com/p/bQZjWhh_GWIjD4H9F_VkIIshpx9u18wxURjBthQBEh6ZjS9dcFWC_F6aNCT0XDQo/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/API%20%ED%82%A4.png)

      4. Result

         ![결과](https://objectstorage.ap-seoul-1.oraclecloud.com/p/M-b9GzJwbpZ6Od2fF7Kn1KOxoTZjXd-ESgrsIZYtd0FyvPHpNWESd2Mx-X7ynfwB/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/API%20%ED%82%A4%20%EA%B2%B0%EA%B3%BC.png)



## Ncloud AGC 생성

   * Console로 이동

      * ![Console](https://objectstorage.ap-seoul-1.oraclecloud.com/p/U89ci1Qh6lvG2V6SN_ZXfxNIsXunRlzN8h4wIKGkCwUkiuI1pbtgAZC495LW0kEX/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ncloud%20Console.png)

   * Dashboard - Server - ACG로 이동

     * ![Dashboard](https://objectstorage.ap-seoul-1.oraclecloud.com/p/rIiwTKEyMh0ne9cFICSvY-1umBhCim-ag2_nNxiDMHFYtaqQiv8WIxe2gd2J-lbw/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/Dashboard.png)

   * ACG 생성

     * ![Create ACG](https://objectstorage.ap-seoul-1.oraclecloud.com/p/UUZQZY-fHcDE-wpyeb7DTTteMQMpbXEQLkL46gmSe56pm9UMwnCsArabeUv-z1Iy/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ACG%20%EC%83%9D%EC%84%B1.png)
     * ![Create ACG 2](https://objectstorage.ap-seoul-1.oraclecloud.com/p/JMa_2YA6Ig9C5UzKydh2GvH-_DGLdKnF4cgZK5ba22Ql5pizQRkdkUFOH8ZRVklY/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ACG%20%EC%83%9D%EC%84%B1%202.png)

   * 생성된 파일 선택 후 ACG 설정

      * ![ACG 설정](https://objectstorage.ap-seoul-1.oraclecloud.com/p/GFtBPchY2Arfr3fUYO8MQDZ1QfFh7qQRDY_aAsVxK_BHUFGQwEVDE3kT1yyAOFEC/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ACG%20%EC%84%A4%EC%A0%95.png)

   * AGC 규칙 설정

      1. ZCONVERTER 서비스를 사용하기 위해서는 50000-50005 port가 열려 있어야 됩니다.

      * ![AGC 규칙 설정](https://objectstorage.ap-seoul-1.oraclecloud.com/p/QzfUavwD9ZJB0eEs6FpaTNrXvG6PxglbIdBYzxo_58zyG5JSc8pq8HJctf8IqalY/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ACG%20%EA%B7%9C%EC%B9%99%20%EC%84%A4%EC%A0%95.png)

   *  AGC ID 복사 후 메모장에 저장

      * ![AGC ID](https://objectstorage.ap-seoul-1.oraclecloud.com/p/nsiPyG26xJHFsmOPqDtYmI0HmjfzXGdl5VyitQXbqeh-paL8GoU-NT56k8NS2KZo/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ACG%20ID.png)
   
   * Result

      ![결과](https://objectstorage.ap-seoul-1.oraclecloud.com/p/6dXKWD92e6J0tNkLl9xc0Qf0lzg-n4hV0eatk-1YU3lofimrlAumswobSDGUQxwy/n/cnfyb6dq82p9/b/NBP_Terraform_reference/o/ACG%20result.png)



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
