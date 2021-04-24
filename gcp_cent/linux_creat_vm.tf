variable "vm_name" {
    type = string
}
variable "vm_machine_type" {
    type = string
}
variable "vm_metadata_starup_script" {
    type = string
}
variable "vm_ssh_key" {
    type = string
}
variable "vm_network" {
    type = string
    default = "default"
}

#create vm
resource "google_compute_instance" "create_vm" {
  name                    = "${var.vm_name}"
  machine_type            = "${var.vm_machine_type}"
  metadata_startup_script = "${file("${var.vm_metadata_starup_script}")}"

  metadata = {
    ssh-keys = "zconverter:${file("${var.vm_ssh_keys}")}"
  }

  boot_disk {
    initialize_params {
      image = "centos-cloud/centos-7"
    }
  }

  network_interface {
    # A default network is created for all GCP projects
    network = "${var.vm_network}"
    access_config {
    }
  }
}
