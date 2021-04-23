variable "vm_name" {
    type = string
}
variable "vm_size" {
    type = string
}
variable "vm_os_disk_name" {
    type = string
}
variable "vm_os_disk_caching" {
    type = string
}
variable "vm_os_disk_storage_account_type" {
    type = string
}
variable "vm_admin_username" {
    type = string
}
variable "vm_admin_password" {
    type = string
}

# Create virtual machine
resource "azurerm_windows_virtual_machine" "create_vm" {
    #VM info
    name                  = "${var.vm_name}"
    location              = "${var.local}"
    resource_group_name   = "${var.group_name}"
    size                  = "${var.vm_size}"

    network_interface_ids = [azurerm_network_interface.nic.id]

    #VM os_disk
    os_disk {
        name              = "${var.vm_os_disk_name}"
        caching           = "${var.vm_os_disk_caching}"
        storage_account_type = "${var.vm_os_disk_storage_account_type}"
    }
    
    #VM image
    source_image_reference {
        publisher = "MicrosoftWindowsServer"
        offer     = "WindowsServer"
        sku       = "2016-Datacenter"
        version   = "latest"
    }

    admin_username = "${var.vm_admin_username}"
    admin_password = "${var.vm_admin_password}"
}

