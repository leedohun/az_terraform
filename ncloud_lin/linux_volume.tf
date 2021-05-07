variable "bv_count" {
    type = number
}
variable "bv_display_name" {
    type = list(string)
}
variable "bv_size" {
    type = list(number)
}

resource "ncloud_block_storage" "storage" {
    count = "${var.bv_count}"
    server_instance_no = ncloud_server.server.id
    name = "${var.bv_display_name[count.index]}"
    size = "${var.bv_size[count.index]}"
}