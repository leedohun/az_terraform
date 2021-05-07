variable "vm_name" {
    type = string
}
variable "vm_server_image_product_code" {
    type = string
}
variable "vm_server_product_code" {
    type = string
}
variable "vm_zone" {
    type = string
}
variable "vm_user_data" {
    type = string
}
variable "login_key_name" {
    type = string
}

resource "ncloud_server" "server" {
    name = "${var.vm_name}"
    server_image_product_code = "${var.vm_server_image_product_code}"
    server_product_code = "${var.vm_server_product_code}"

    zone = "${var.vm_zone}"

    user_data = "${file("${var.vm_user_data}")}"

    login_key_name = "${var.login_key_name}"
}