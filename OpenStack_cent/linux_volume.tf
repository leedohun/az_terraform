variable "bv_count" {
  type = number
}
variable "bv_display_name" {
  type = list(string)
}
variable "bv_size" {
  type = list(number)
}


#create volume
resource "openstack_blockstorage_volume_v2" "volume" {
    count = "${var.bv_count}"
    name  = "${var.bv_display_name[count.index]}"
    size  = "${var.bv_size[count.index]}"
}

#attach volume
resource "openstack_compute_volume_attach_v2" "attached" {
    count       = "${var.bv_count}"
    instance_id = "${openstack_compute_instance_v2.create_vm.id}"
    volume_id   = "${openstack_blockstorage_volume_v2.volume[count.index].id}"
}