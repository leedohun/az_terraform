OCI Terraform
============

> Before You Begin
> 
> Prepare
> 
> Install Terraform Data
> 
> Start Terraform



## Before You Begin
To successfully perform this tutorial, you must have the following:

   * An Oracle Cloud Infrastructure account. [See Signing Up for Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/GSG/Tasks/signingup.htm)
   * A MacOS, Linux, or Windows environment:
   * MacOS
   * Linux (Any distribution)
      - You can install a Linux VM with an **Always Free** Compute shape, on Oracle Cloud Infrastructure:
         +  [Install an Ubuntu VM](https://docs.oracle.com/iaas/developer-tutorials/tutorials/helidon-on-ubuntu/01oci-ubuntu-helidon-summary.htm#create-ubuntu-vm)
         +  [Install an Oracle Linux VM](https://docs.oracle.com/iaas/developer-tutorials/tutorials/apache-on-oracle-linux/01oci-ol-apache-summary.htm#create-oracle-linux-vm)
   * Oracle Cloud Infrastructure Cloud Shell:
      -  [Cloud Shell](https://docs.oracle.com/iaas/Content/API/Concepts/cloudshellintro.htm)
   * Windows 10
      -  [Windows Subsystem for Linux](https://ubuntu.com/wsl) (WSL)
      -  [Git for Windows](https://gitforwindows.org/) to access a Linux VM.



## Prepare
Prepare your environment for authenticating and running your Terraform scripts. Also, gather the information your account needs to authenticate the scripts.

### Install Terraform
   Install the latest version of Terraform **v13.0+**:

   1. In your environment, check your Terraform version.
      ```script
      terraform -v
      ```

      If you don't have Terraform **v13.0+**, then install Terraform using the following steps.

   2. From a browser, go to [Download Latest Terraform Release](https://www.terraform.io/downloads.html).

   3. Find the link for your environment and then **copy** the link address. Example for Linux 64-bit:
      ```script
      https://releases.hashicorp.com/terraform/0.13.1/terraform_0.13.1_linux_amd64.zip
      ```

      * IF you use Windows os, Use the cmd command line

   4. In your environment, create a temp directory and change to that directory:
      ```script
      mkdir temp
      ```
      ```script
      dc temp
      ```

   5. Download the Terraform zip file. Example:
      ```script
      wget https://releases.hashicorp.com/terraform/0.13.1/terraform_0.13.1_linux_amd64.zip
      ```

   6. Unzip the file. Example:
      ```script
      unzip terraform_0.13.1_linux_amd64.zip
      ```

   7. Move the folder to /usr/local/bin or its equivalent in Mac. Example:
      ```script
      sudo mv terraform /usr/local/bin
      ```

   8. Go back to your home directory:
      ```script
      cd
      ```

   9. Check the Terraform version:
      ```script
      terraform -v
      ```

      Example: `Terraform v0.13.1`.

### Create API-Key
   If you created API keys for the Terraform Set Up Resource Discovery tutorial, then skip this step.

   Create RSA keys for API signing into your **Oracle Cloud Infrastructure account**.

   1. **Log in to the Oracle Cloud site and access the user portal.**

      ![Login](https://objectstorage.ap-seoul-1.oraclecloud.com/p/UintikT5Bz9_ciVuEgqCJ1b1d34PzwoDZM1HV2trqjydCVx7XQbaOLRRR5PWep9T/n/cnfyb6dq82p9/b/test_bucket/o/login.png)  

   2. **Enter the User menu.**

      ![Account User](https://objectstorage.ap-seoul-1.oraclecloud.com/p/ZOKRkEnpLI3IHFs80_aW3Ciy6HTd-skSGzNuZ2fzSywbU6MSdWf2U5dOxN9ID_1X/n/cnfyb6dq82p9/b/test_bucket/o/Select%20Users.png)  

   3. **Choice User Account Name to use.**

      ![Account Users](https://objectstorage.ap-seoul-1.oraclecloud.com/p/Mj3mBoNkl6NWjDLhtxfe63J-4Lq2r6VyKoZIxFOYEus_uUxy4KO4yL8-1O-EXKAX/n/cnfyb6dq82p9/b/test_bucket/o/Account%20Users.png)

   4. **Click api-key in the lower left resource**

      ![Api-Key](https://objectstorage.ap-seoul-1.oraclecloud.com/p/mZP_d9myS9aL_V3lTFWWtr4qU9puC_l3rkUGxclnR-aTUGedd4YEn4faWMU3jww8/n/cnfyb6dq82p9/b/test_bucket/o/Select%20API.png)

   5. **Click add api key**

      ![Api-Key](https://objectstorage.ap-seoul-1.oraclecloud.com/p/wTwhMhRpk_lhRDXu-4RnSznJrNTFkIEI53rONT3YTeCh-QFG-t-NSEeYzvQ2MSQ9/n/cnfyb6dq82p9/b/test_bucket/o/Add%20API%20Key.png)

   6. **Under API Key Pairing, click Download Private Key and Download Public Key, and then click the Add button. If there are more than three API Key, Delete API Key or use another User Account Name.**

      ![Api-Key](https://objectstorage.ap-seoul-1.oraclecloud.com/p/1j-WJIccEQU3XQs6I0Hif6_VQ9hhWtnGp6vAfuXv4iR2yIBLHjunW93NqjAPtvXX/n/cnfyb6dq82p9/b/test_bucket/o/Add%20API.png)

   7. **Copy the results from Configuration File Preview onto the notepad.**

      ![Configuration](https://objectstorage.ap-seoul-1.oraclecloud.com/p/FfXcylPsG9x_WGq1tON5N30HMQEKHWsNZFUWlDAtC3EJKEybxBogSNvdN16niP6z/n/cnfyb6dq82p9/b/test_bucket/o/Configuration.png)
   
   8. **Select Networking from the menu, then select Virtual Cloud Networks**

      ![Networking-Virtual Cloud Network](https://objectstorage.ap-seoul-1.oraclecloud.com/p/Ulj5DJRXrogaUhSUYiYLp4q4LUiht9xkaiGMOpx3QOhFnrZrC8nbQ1SJ49UDTGrD/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/Networking-Virtual%20Cloud%20Network.png)
   
   9. **Choice VCN User Account Name to use**

      ![Select VCM User Account Name](https://objectstorage.ap-seoul-1.oraclecloud.com/p/5prXUWaNWNUVGCUtbHfstzC_jEMIXQGzOoF2VfEQDp4D9DYptUVBlWdOGNSBNv5F/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/Select%20VCN.png)

   1. **Choice Subnets Name to use**

      ![Select Subnets Name](https://objectstorage.ap-seoul-1.oraclecloud.com/p/COkmv-Hnf2SEdSeCJaMj2YGUpdTQxqUOIP6MIOzX_Uw9U0Ag87vhyhR0Xj46tKlW/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/Select%20Subnet.png)

   1. **Copy the Subnet OCID onto the notepad**

      ![Subnet OCID](https://objectstorage.ap-seoul-1.oraclecloud.com/p/L432fY2P28qhOKUfoVtCnnRjJbfSJF-gj6zfHVsya8m07v923kS1NXTEa2zGqtGY/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/Subnet%20OCID.png)

   1. **Result**

      ![Result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/d3DO2uh2rqpVCS2hPOWWju16rVKWNFcGoFTOMpFn00QhnsJYgK4ew5OWAEjcaRbJ/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/result.png)

  

## Install OCI Terraform Data
   Install the **terraform data** you need to make your OCI vm.

   1. **Download [Terraform data](https://objectstorage.ap-seoul-1.oraclecloud.com/p/EDWNpjJwJYr5Uf2SX2cDlIsLdLY4tzTL8p3KGh5OXByBh3qVi120mQEslLS3NWyZ/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/oci_terraform.zip)**

   2. **Unzip OCI Terraform data**

      ![OCI terraform data](https://objectstorage.ap-seoul-1.oraclecloud.com/p/vdefQu1xjF4FFLeaNQwGmBegQr1ji0QwXKoXB4MB6bgsiquRNjiq1qoA3wezVOst/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/terraform%20OCi%20data.png)



## Start Terraform

   1. **Edit a vars.tfvars File you want to create VM**

      ![vars.tfvars](https://objectstorage.ap-seoul-1.oraclecloud.com/p/JCZF2EFjD5hU-isTloeWYfU8osHFwFI0oMoDrKY7dSp8ghvuHF4CHIHEqr2bRcXi/n/cnfyb6dq82p9/b/OCI_Terraform_reference/o/Edit%20a%20vars.tfvars.png)

      * vars.tfvars data info:
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
