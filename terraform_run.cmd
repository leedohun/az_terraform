#echo

#rem terraform init
terraform.exe -chdir={terraform_file_path} init

#rem terraform apply
terraform.exe -chdir={terraform_file_path} apply -var-file=vars.tfvars -auto-approve -state-out={result_path}
