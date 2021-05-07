#provider
variable "ncp_access_key" {
    type = string
}
variable "ncp_secret_key" {
    type = string
}
variable "ncp_region" {
    type = string
}

terraform {
  required_providers {
    ncloud = {
      source = "NaverCloudPlatform/ncloud"
    }
  }
  required_version = ">= 0.13"
}

// Configure the ncloud provider
provider "ncloud" {
    access_key = "${var.ncp_access_key}"
    secret_key = "${var.ncp_secret_key}"
    region     = "${var.ncp_region}"
}