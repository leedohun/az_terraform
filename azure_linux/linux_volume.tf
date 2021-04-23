variable "bv_count"{
  type = number
}
variable "bv_display_name" {
  type = list(string)
}
variable "bv_account_storage_type"{
  type = string
}
variable "bv_create_option" {
  type = string
}
variable "bv_size"{
  type = list(number)
}
variable "bv_lun" {
  type = list(string)
}
variable "bv_caching" {
  type = string
}


resource "azurerm_managed_disk" "creat_disk" {
  count                = "${var.bv_count}"
  name                 = "${var.bv_display_name[count.index]}"
  location             = "${var.local}"
  resource_group_name  = "${var.group_name}"
  storage_account_type = "${var.bv_account_storage_type}"
  create_option        = "${var.bv_create_option}"
  disk_size_gb         = "${var.bv_size[count.index]}"
}

resource "azurerm_virtual_machine_data_disk_attachment" "attach_disk" {
  count              = "${var.bv_count}"
  virtual_machine_id = azurerm_linux_virtual_machine.create_vm.id
  managed_disk_id    = azurerm_managed_disk.creat_disk[count.index].id
  lun                = "${var.bv_lun[count.index]}"
  caching            = "${var.bv_caching}"
}
