variable "sg_name" {
    type = string
}


# Create Network Security Group and rule
resource "azurerm_network_security_group" "securitu_group" {
    name                       = "${var.sg_name}"
    location                   = "${var.local}"
    resource_group_name        = "${var.group_name}"


  security_rule {
    name                       = "SSH"
    priority                   = 1001
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
   
    security_rule {
    name                       = "RDP"
    priority                   = 1002
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "3389"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
   security_rule {
    name                       = "zconverter"
    priority                   = 1003
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_ranges    = ["50000-50005"]
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}


# Connect the security group to the network interface
resource "azurerm_network_interface_security_group_association" "attached_security_group" {
    network_interface_id      = azurerm_network_interface.nic.id
    network_security_group_id = azurerm_network_security_group.securitu_group.id
}