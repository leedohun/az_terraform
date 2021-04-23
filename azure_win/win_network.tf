variable "group_name" {
    type = string
}
variable "local" {
    type = string
}
variable "nw_name" {
    type = string
}


# Create virtual network
resource "azurerm_virtual_network" "network" {
    name                = "${var.nw_name}"
    address_space       = ["10.0.0.0/16"]
    location            = "${var.local}"
    resource_group_name = "${var.group_name}"
}
