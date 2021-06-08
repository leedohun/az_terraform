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

   2. Enter the User menu.
      ![Account User](https://objectstorage.ap-seoul-1.oraclecloud.com/p/ZOKRkEnpLI3IHFs80_aW3Ciy6HTd-skSGzNuZ2fzSywbU6MSdWf2U5dOxN9ID_1X/n/cnfyb6dq82p9/b/test_bucket/o/Select%20Users.png)  

   3. Select a user account to use.
      ![Account Users](https://objectstorage.ap-seoul-1.oraclecloud.com/p/Mj3mBoNkl6NWjDLhtxfe63J-4Lq2r6VyKoZIxFOYEus_uUxy4KO4yL8-1O-EXKAX/n/cnfyb6dq82p9/b/test_bucket/o/Account%20Users.png)

   4. Click api-key in the lower left resource
      ![Api-Key](https://objectstorage.ap-seoul-1.oraclecloud.com/p/loI-emg6u0lh9fUSBcYtOxB3sHrZdReHE8w9UShac3o07rV1YxGrdDRomJedjeFm/n/cnfyb6dq82p9/b/test_bucket/o/Select%20API.png)

   5. Click add api key
      ![Api-Key](https://objectstorage.ap-seoul-1.oraclecloud.com/p/0h6Wa3WGv6TxKdlToZiSF1y8DKfb5OzUyk1FoNOwqcI3Uia4H-6en1OJ6QrKjax2/n/cnfyb6dq82p9/b/test_bucket/o/Add%20API.png)

   6. Under API Key Pairing, click Download Private Key and Download Public Key, and then click the Add button.
      ![Api-Key](https://objectstorage.ap-seoul-1.oraclecloud.com/p/LWIhfi13CPLouybPpS7Y4CBIz0C6kBRvSdnhk3CJPmvkZ1i3Q_oIT6FSPoSEVEY3/n/cnfyb6dq82p9/b/test_bucket/o/Add%20API%20Key.png)

   7. Copy the results from Configuration File Preview onto the notepad.
      ![Configuration](https://objectstorage.ap-seoul-1.oraclecloud.com/p/-Zt31hsQBx_ZeziV66Ht-7lpHmaq6DaEEougk4XsNSAjKGTMex2IXXK217ksmbGr/n/cnfyb6dq82p9/b/test_bucket/o/Configuration.png)

      ![Result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/gOxnRsQzQnxPaDe0qlPc7nOh4-Kdnzq6mu3OmJiUueDOPKhiBh3rPHaJDsaGJqi5/n/cnfyb6dq82p9/b/test_bucket/o/Result.png)

  

## Install OCI Terraform Data
   Install the **terraform data** you need to make your OCI vm.

   1. **Download [Terraform data](https://objectstorage.ap-seoul-1.oraclecloud.com/p/bHkV4FBOsJqlTk5LoAGB0er2eazIffo0GayOxpnXl3NmIFiw-OOmC_r7k3QnwX9k/n/cnfyb6dq82p9/b/test_bucket/o/oci.zip)**

   2. Unzip OCI Terraform data
      ![result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/prTLqef95IlqW3cUVx69HQXbajaVw8JjmyMIswxKEzKv1UdHSab4TP17R9BxoY59/n/cnfyb6dq82p9/b/test_bucket/o/result_Extract_zip.png)
  


## Start Terraform

   1. Edit a vars.tfvars File you want to create VM
      ![vars.tfvars](https://objectstorage.ap-seoul-1.oraclecloud.com/p/OamyrtOzj--tgs_MItd7Ns17tDiHrwXRPo86I-HX81_D1AnYoBY5a-DrYUON6whZ/n/cnfyb6dq82p9/b/test_bucket/o/open_vars.tfvars.png)
      ![vars.tfvars example](https://objectstorage.ap-seoul-1.oraclecloud.com/p/MpiLFhwOzZxEpR0JhRTE_mCVurhRsbtlcBZ5zzzckjTKFa5XA7uzlz5igeLvBHFq/n/cnfyb6dq82p9/b/test_bucket/o/vars.tfvars_update.png)

   ### OS and OS_Version Manual
      | | | | | | | | | | | | | |
      |-|-------------|-------------|----------------|--------|----------|-----------|---------|---------|---------|-------------|-------------|-------------|
      | | Windows2019 | Windows2016 | Windows2012 R2 | Linux8 | Linux7.9 | Linux6.10 | centos8 | centos7 | centos8 | ubuntu20.04 | ubuntu18.04 | ubuntu16.04 |
      | OS | Windows | Windows | Windows | Oracle Linux | Oracle Linux | Oracle Linux  | CentOS | CentOS | CentOS | Canonical Ubuntu | Canonical Ubuntu | Canonical Ubuntu |
      | OS_Version | Server 2019 Standard | Server 2016 Standard | Server 2012 R2 Standard | 8 | 7.9 | 6.10 | 8 | 7 | 6 | 20.04 | 18.04 | 16.04 |

   2. Start CMD
      ![cmd](https://objectstorage.ap-seoul-1.oraclecloud.com/p/e8Z1D4LRTo5lMKNazFMPk336Tj7f3dDBiiTY3nncP55Mcn3_ZamU7rh95bdJ_f6T/n/cnfyb6dq82p9/b/test_bucket/o/run_cmd.png)

   3. Go to the file path of Terraform.exe and Initialize the working directory containing the terraform configuration file.
      ```script
      Terraform.exe -chdir={terraform data file path} init
      ```
      ![terraform init](https://objectstorage.ap-seoul-1.oraclecloud.com/p/-MbOI7iohBzYf0nZigfNbluXOaa8rRypdsxlBNWSwNKFzpRk0e-bGGbtYPRXmj6f/n/cnfyb6dq82p9/b/test_bucket/o/terraform%20init.png)
   
      ![terraform init result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/T2z5bSTqorrNiI6jSOU8McxhVhPYiXkhUnEsvj3aA0xiXeI6vVmwb0IqZcxLNNcE/n/cnfyb6dq82p9/b/test_bucket/o/result_terraform%20init.png)


   4. Creates an execution plan. By default, creating a plan consists of:
      ```script
      Terraform.exe -chdir={terraform data file path} plan -var-file={vars file path}
      ```

      * Reading the current state of any already-existing remote objects to make sure that the Terraform state is up-to-date.
      * Comparing the current configuration to the prior state and noting any differences.
      * Proposing a set of change actions that should, if applied, make the remote objects match the configuration.

      ![terraform plan](https://objectstorage.ap-seoul-1.oraclecloud.com/p/6TzI1DE25F7qRGJr2dO4lPleSx-nzdV5OnqnHUBPvpohyKJXCcPg7hsu6YyNe19r/n/cnfyb6dq82p9/b/test_bucket/o/terraform%20plan.png)

   5. Executes the actions proposed in a Terraform plan.
      ```script
      Terraform.exe -chdir={terraform data file path} -var-file={vars file path} -auto-approve apply
      ```

      ![terraform apply](https://objectstorage.ap-seoul-1.oraclecloud.com/p/D-Av4dANh4d5I_8Amyi--N1VjxM-SK2aMHQj3ph3txIyEdseuyJzaJMbKIWSkZdH/n/cnfyb6dq82p9/b/test_bucket/o/terraform%20apply.png)

      ![terraform apply result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/fSnqf6g_jlGLFHzuiNQZ1v5ZbYK7EFn7V1zGTu2T3Qr4wfzCr-nBNAHlaJXMW_yd/n/cnfyb6dq82p9/b/test_bucket/o/result_terraform%20apply.png)

      **Note**
         * -chdir : The usual way to run Terraform is to first switch to the directory containing the `.tf` files for your root module (for example, using the `cd` command), so that Terraform will find those files automatically without any extra arguments.
         * -var-file : Sets values for potentially many [input variables](https://www.terraform.io/docs/language/values/variables.html) declared in the root module of the configuration, using definitions from a ["tfvars" file](https://www.terraform.io/docs/language/values/variables.html#variable-definitions-tfvars-files). Use this option multiple times to include values from more than one file.
         * -auto-approve : Skips interactive approval of plan before applying. This option is ignored when you pass a previously-saved plan file, because Terraform considers you passing the plan file as the approval and so will never prompt in that case.
    
