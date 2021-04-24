variable "bv_count"{
    type = number
}
variable "bv_display_name" {
    type = list(string)
}
variable "bv_size" {
    type = list(number)
}


#create volume
resource "google_compute_disk" "create_volume" {
  count = "${var.bv_count}"
  name  = "${var.bv_display_name[count.index]}"
  size  = "${var.bv_size[count.index]}"
}

#attached volume
resource "google_compute_attached_disk" "attached_volume" {
  count    = "${var.bv_count}"
  disk     = google_compute_disk.create_volume[count.index].id
  instance = google_compute_instance.create_vm.id
}