variable "vm_name" {
  type = string
}
variable "vm_flavor_id" {
  type = string
}
variable "vm_secrutiy_groups" {
  type = string
}
variable "vm_network_name" {
  type = string
}


#create_vm
resource "openstack_compute_instance_v2" "create_vm" {
  name            = "${var.vm_name}"
  image_id        = "704cb217-a7d3-47f7-a830-a4151c931311"
  flavor_id       = "${var.vm_flavor_id}"

  security_groups = ["${var.vm_security_groups}"]

  user_data       = "${file("./OpenStack_win_agent.ps1")}"

  network {
    name = "${var.vm_network_name}"
  }
}