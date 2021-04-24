#provider
gcp_credentials = "file.json"
gcp_project     = "project"
gcp_region      = "asia-northeast3"
gcp_zone        = "asia-northeast3-a"


#create vm
vm_name                   = "target-gcp-win"
vm_machine_type           = "e2-standard-2"
vm_metadata_starup_script = "GCP_win_agent.ps1"


#volume
bv_count        = 4
bv_display_name = ["win1", "win2", "win3", "win4"]
bv_size         = [10, 20, 30, 40]


