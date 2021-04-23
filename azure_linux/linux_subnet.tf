variable "sb_name" {
    type = string
}

# Create subnet
resource "azurerm_subnet" "subnet" {
    name                 = "${var.sb_name}"
    resource_group_name  = "${var.group_name}"
    virtual_network_name = azurerm_virtual_network.network.name
    address_prefixes       = ["10.0.1.0/24"]
}