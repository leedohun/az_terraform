#provider
os_provider = "openstack"


#create_vm
vm_name            = "target-openstack-win"
vm_flavor_id       = "4"
vm_security_groups = "default"
vm_network_name    = "Private_Net"


#attach volume
bv_count        = 4
bv_display_name = ["win-1", "win-2", "win-3", "win-4"]
bv_size         = [10, 20, 30, 40]


