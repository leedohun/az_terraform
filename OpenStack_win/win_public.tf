variable "pi_pool" {
  type    = string
  default = "public"
}

#attach public Ip
resource "openstack_networking_floatingip_v2" "floatingIp" {
  pool = "${var.pi_pool}"
}

resource "openstack_compute_floatingip_associate_v2" "floatingIp" {
  floating_ip = "${openstack_networking_floatingip_v2.floatingIp.address}"
  instance_id = "${openstack_compute_instance_v2.create_vm.id}"
}