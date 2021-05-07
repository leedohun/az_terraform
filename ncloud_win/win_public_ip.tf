resource "ncloud_public_ip" "public_ip"{
  server_instance_no = ncloud_server.server.id
}
