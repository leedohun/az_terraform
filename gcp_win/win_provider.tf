variable "gcp_credentials" {
    type = string
}
variable "gcp_project" {
    type = string
}
variable "gcp_region" {
    type = string
}
variable "gcp_zone" {
    type = string
}

// Configure the Google Cloud provider
provider "google" {
    credentials = "${"${var.gcp_credentials}"}"
    project     = "${var.gcp_project}"
    region      = "${var.gcp_region}"
    zone        = "${var.gcp_zone}"
}