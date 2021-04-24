variable "vm_name" {
    type = string
}
variable "vm_machine_type" {
    type = string
}
variable "vm_metadata_starup_script" {
    type = string
}
variable "vm_network" {
    type = string
    default = "default"
}

#create vm
resource "google_compute_instance" "create_vm" {
  name                       = "${var.vm_name}"
  machine_type               = "${var.vm_machine_type}"
  
  metadata = {
    windows-startup-script-ps1 = "${file("${var.vm_metadata_starup_script}")}"
  }

  boot_disk {
    initialize_params {
      image = "windows-sql-cloud/sql-ent-2016-win-2016"
    }
  }

  network_interface {
    # A default network is created for all GCP projects
    network = "${var.vm_network}"
    access_config {
    }
  }
}
