resource "aws_instance" "artifactory" {
  ami           = "${lookup(var.AMIS, var.AWS_REGION)}"
  instance_type = "t2.micro"

  associate_public_ip_address = true
  availability_zone           = "${data.aws_availability_zones.available.names[0]}"
  security_groups             = ["${aws_security_group.lab-ci-sg.name}"]

  key_name = "${aws_key_pair.default.key_name}"

  connection {
    user        = "ec2-user"
    private_key = "${file(var.PRIVATE_KEY_PATH)}"
  }

  provisioner "file" {
    source      = "ec2-artifactory.sh"
    destination = "~/artifactory.sh"
  }

  provisioner "remote-exec" {
    inline = [
      "chmod +x ~/artifactory.sh",
      "./artifactory.sh",
    ]
  }

  provisioner "file" {
    source      = "www-data"
    destination = "~"
  }

  provisioner "file" {
    source      = "shared/nginx/nginx.conf"
    destination = "nginx.conf"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum install nginx -y",
      "sed -i -e s/__PORT__/8081/ nginx.conf",
      "sed -i -e s/__DOMAIN__/artifactory-/ nginx.conf",
      "sudo mv ~/nginx.conf /etc/nginx/nginx.conf",
      "sudo service nginx start",
      "sudo chkconfig nginx on",
    ]
  }
}

// asdsadasda

output "instance_ip_addr" {
  value = "${aws_instance.artifactory.public_ip}"
}


resource "aws_instance" "host" {
  ami                         = "${lookup(var.AMIS, var.AWS_REGION)}"
  instance_type               = "t2.micro"
  associate_public_ip_address = true
  availability_zone           = "${data.aws_availability_zones.available.names[0]}"
  security_groups             = ["${aws_security_group.lab-ci-sg.name}"]
  key_name                    = "${aws_key_pair.default.key_name}"

  connection {
    user        = "ec2-user"
    private_key = "${file(var.PRIVATE_KEY_PATH)}"
  }
}

resource "aws_key_pair" "default" {
  key_name   = "lab_key_pair"
  public_key = "${file(var.PUBLIC_KEY_PATH)}"
}

resource "aws_security_group" "lab-ci-sg" {
  name = "lab-ci-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["${var.cidr_blocks}"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["${var.cidr_blocks}"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["${var.cidr_blocks}"]
  }

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["${var.cidr_blocks}"]
  }

  ingress {
    from_port   = 8079
    to_port     = 8099
    protocol    = "tcp"
    cidr_blocks = ["${var.cidr_blocks}"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["${var.cidr_blocks}"]
  }
}

output "host_made_ua" {
  value = "${aws_instance.host.public_ip}"
}
