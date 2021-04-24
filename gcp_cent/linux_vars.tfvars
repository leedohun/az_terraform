#provider
gcp_credentials = "file.json"
gcp_project     = "project"
gcp_region      = "asia-northeast3"
gcp_zone        = "asia-northeast3-a"


#create vm
vm_name                   = "target-gcp-centos7"
vm_machine_type           = "e2-standard-2"
vm_metadata_starup_script = "GCP_linux_agent.sh"
vm_ssh_keys               = "./RIM/RIM.pub"


#volume
bv_count        = 4
bv_display_name = ["linux1", "linux2", "linux3", "linux4"]
bv_size         = [10, 20, 30, 40]


