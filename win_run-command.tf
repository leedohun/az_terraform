variable "rc_name" {
    type = string
}
variable "rc_publisher" {
    type = string
}
variable "rc_type" {
    type = string
}
variable "rc_type_handler_version" {
    type = string
}
variable "rc_script" {
    type = string
}


#azure run-command
resource "azurerm_virtual_machine_extension" "run_script" {
  name                 = "${var.rc_name}"
  virtual_machine_id   = azurerm_windows_virtual_machine.create_vm.id
  publisher            = "${var.rc_publisher}"
  type                 = "${var.rc_type}"
  type_handler_version = "${var.rc_type_handler_version}"

  protected_settings = <<SETTINGS
  {
     "commandToExecute": "powershell -encodedCommand ${textencodebase64(file("${var.rc_script}"), "UTF-16LE")}"
  }
  SETTINGS
}
