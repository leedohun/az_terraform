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

   2. **Enter the User menu.**

      ![Account User](https://objectstorage.ap-seoul-1.oraclecloud.com/p/ZOKRkEnpLI3IHFs80_aW3Ciy6HTd-skSGzNuZ2fzSywbU6MSdWf2U5dOxN9ID_1X/n/cnfyb6dq82p9/b/test_bucket/o/Select%20Users.png)  

   3. **Select a user account to use.**

      ![Account Users](https://objectstorage.ap-seoul-1.oraclecloud.com/p/Mj3mBoNkl6NWjDLhtxfe63J-4Lq2r6VyKoZIxFOYEus_uUxy4KO4yL8-1O-EXKAX/n/cnfyb6dq82p9/b/test_bucket/o/Account%20Users.png)

   4. **Click api-key in the lower left resource**

      ![Api-Key](https://objectstorage.ap-seoul-1.oraclecloud.com/p/mZP_d9myS9aL_V3lTFWWtr4qU9puC_l3rkUGxclnR-aTUGedd4YEn4faWMU3jww8/n/cnfyb6dq82p9/b/test_bucket/o/Select%20API.png)

   5. **Click add api key**

      ![Api-Key](https://objectstorage.ap-seoul-1.oraclecloud.com/p/wTwhMhRpk_lhRDXu-4RnSznJrNTFkIEI53rONT3YTeCh-QFG-t-NSEeYzvQ2MSQ9/n/cnfyb6dq82p9/b/test_bucket/o/Add%20API%20Key.png)

   6. **Under API Key Pairing, click Download Private Key and Download Public Key, and then click the Add button.**

      ![Api-Key](https://objectstorage.ap-seoul-1.oraclecloud.com/p/1j-WJIccEQU3XQs6I0Hif6_VQ9hhWtnGp6vAfuXv4iR2yIBLHjunW93NqjAPtvXX/n/cnfyb6dq82p9/b/test_bucket/o/Add%20API.png)

   7. **Copy the results from Configuration File Preview onto the notepad.**

      ![Configuration](https://objectstorage.ap-seoul-1.oraclecloud.com/p/FfXcylPsG9x_WGq1tON5N30HMQEKHWsNZFUWlDAtC3EJKEybxBogSNvdN16niP6z/n/cnfyb6dq82p9/b/test_bucket/o/Configuration.png)


      ![Result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/JdXybfHHENL__Pivov6QdvoQ-P0Om2Rv7J2KpZs4uJJ0X24bJ2H3HvXx6uAN0Q69/n/cnfyb6dq82p9/b/test_bucket/o/Result.png)

  

## Install OCI Terraform Data
   Install the **terraform data** you need to make your OCI vm.

   1. **Download [Terraform data](https://objectstorage.ap-seoul-1.oraclecloud.com/p/bHkV4FBOsJqlTk5LoAGB0er2eazIffo0GayOxpnXl3NmIFiw-OOmC_r7k3QnwX9k/n/cnfyb6dq82p9/b/test_bucket/o/oci.zip)**

   2. **Unzip OCI Terraform data**
      ![result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/HLcZ1BexX5bj_CuTPBMIxREh7JGyJG0A-T1exKMpSrYmRh123lo5CJbBo5JAqMXe/n/cnfyb6dq82p9/b/test_bucket/o/Unzip%20OCI%20Terraform%20data.png)
  


## Start Terraform

   1. **Edit a vars.tfvars File you want to create VM**

      ![vars.tfvars](https://objectstorage.ap-seoul-1.oraclecloud.com/p/chAL1E_3a-ucI79AZnLM1PpvcYyBh5IB8qjdQf8-_NZz8M4ZtVVfaCi_90MV4e8T/n/cnfyb6dq82p9/b/test_bucket/o/Edit%20a%20vars.tfvars.png)

      ![vars.tfvars example](https://objectstorage.ap-seoul-1.oraclecloud.com/p/RQ6xeNPFJHrX_N_UX5WmLxFj99aPKMRzgn94gWMopEYqdM7B_ue-M-DSkwRh0yFC/n/cnfyb6dq82p9/b/test_bucket/o/vars.tfvars%20result.png)

   ### OS and OS_Version Manual
   | | | | | | | | | | | | | |
   |-|-------------|-------------|----------------|--------|----------|-----------|---------|---------|---------|-------------|-------------|-------------|
   | | Windows2019 | Windows2016 | Windows2012 R2 | Linux8 | Linux7.9 | Linux6.10 | centos8 | centos7 | centos8 | ubuntu20.04 | ubuntu18.04 | ubuntu16.04 |
   | OS | Windows | Windows | Windows | Oracle Linux | Oracle Linux | Oracle Linux  | CentOS | CentOS | CentOS | Canonical Ubuntu | Canonical Ubuntu | Canonical Ubuntu |
   | OS_Version | Server 2019 Standard | Server 2016 Standard | Server 2012 R2 Standard | 8 | 7.9 | 6.10 | 8 | 7 | 6 | 20.04 | 18.04 | 16.04 |

   2. **Start CMD**

      ![cmd](https://objectstorage.ap-seoul-1.oraclecloud.com/p/XzXmdi7e-eQrmxk3S9QpiC62EmqKS7Mui5rav_-8bLONUsFPqIGk24P-FoJmQTu5/n/cnfyb6dq82p9/b/test_bucket/o/start%20cmd.png)

   3. **Go to the file path of Terraform.exe and Initialize the working directory containing the terraform configuration file.**

      ```script
      terraform.exe -chdir={terraform data file path} init
      ```
      ![terraform init](https://objectstorage.ap-seoul-1.oraclecloud.com/p/o3ND_XFU9-56CWa_-BeetXwzVm3PyJJO7KvqfX8HQa5cpaaK9Q8Re9ccJvQqUAKx/n/cnfyb6dq82p9/b/test_bucket/o/terraform%20init.png)
   
      ![terraform init result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/NqZBWtKkyXdEa1CNcpLMlmJGFeCGR4rldVFdVesAJVjCwpCkEKnwDNlRbA4GNtOS/n/cnfyb6dq82p9/b/test_bucket/o/terraform%20init%20result.png)


   4. **Creates an execution plan. By default, creating a plan consists of:**

      ```script
      terraform.exe -chdir={terraform data file path} plan -var-file=vars.tfvars
      ```

      * Reading the current state of any already-existing remote objects to make sure that the Terraform state is up-to-date.
      * Comparing the current configuration to the prior state and noting any differences.
      * Proposing a set of change actions that should, if applied, make the remote objects match the configuration.

      ![terraform plan](https://objectstorage.ap-seoul-1.oraclecloud.com/p/J9w6W5B9UJhYyT7jlquqpsthCtqWP-8PcSbixeyivpOveUiRv86Tqvd8SsixOD3t/n/cnfyb6dq82p9/b/test_bucket/o/terraform%20plan.png)

   5. **Executes the actions proposed in a Terraform plan.**

      ```script
      terraform.exe -chdir={terraform data file path} -var-file=vars.tfvars -auto-approve apply
      ```

      ![terraform apply](https://objectstorage.ap-seoul-1.oraclecloud.com/p/Ms3aiK6vFToHI7SCm25ZJ9_-ZErLDCNEl2cK9J0DqvOOKwdr3rRmZWR9-7SNYV8v/n/cnfyb6dq82p9/b/test_bucket/o/terraform%20apply.png)

      ![terraform apply result](https://objectstorage.ap-seoul-1.oraclecloud.com/p/sHKXhKrmQ8fLVxDOcpApRnabVm4qGTa4eP4naW9EBg1o3ieT7-BS0dQG8yvMOfW5/n/cnfyb6dq82p9/b/test_bucket/o/terraform%20apply%20result.png)

      **Note**
         * -chdir : The usual way to run Terraform is to first switch to the directory containing the `.tf` files for your root module (for example, using the `cd` command), so that Terraform will find those files automatically without any extra arguments.
         * -var-file : Sets values for potentially many [input variables](https://www.terraform.io/docs/language/values/variables.html) declared in the root module of the configuration, using definitions from a ["tfvars" file](https://www.terraform.io/docs/language/values/variables.html#variable-definitions-tfvars-files). Use this option multiple times to include values from more than one file.
         * -auto-approve : Skips interactive approval of plan before applying. This option is ignored when you pass a previously-saved plan file, because Terraform considers you passing the plan file as the approval and so will never prompt in that case.
    
