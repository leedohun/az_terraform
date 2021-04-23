variable "ip_name" {
    type = string
}
variable "ip_allocation_method" {
    type = string
}


# Create public IPs
resource "azurerm_public_ip" "publicIp" {
    name                         = "${var.ip_name}"
    location                     = "${var.local}"
    resource_group_name          = "${var.group_name}"
    allocation_method            = "${var.ip_allocation_method}"
}