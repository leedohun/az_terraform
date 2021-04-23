variable "nic_name" {
    type = string
}
variable "nic_ip_configuration_name" {
    type = string
}
variable "nic_ip_configuration_private_ip_address_allocation" {
    type = string
}


# Create network interface
resource "azurerm_network_interface" "nic" {
    name                      = "${var.nic_name}"
    location                  = "${var.local}"
    resource_group_name       = "${var.group_name}"

    ip_configuration {
        name                          = "${var.nic_ip_configuration_name}"
        subnet_id                     = azurerm_subnet.subnet.id
        private_ip_address_allocation = "${var.nic_ip_configuration_private_ip_address_allocation}"
        public_ip_address_id          = azurerm_public_ip.publicIp.id
    }
}