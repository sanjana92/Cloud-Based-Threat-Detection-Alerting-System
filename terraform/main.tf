provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "web_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  tags = {
    Name = "CTDAS-EC2"
  }
}

resource "aws_s3_bucket" "log_bucket" {
  bucket = "ctdas-log-bucket"
  force_destroy = true
}

resource "aws_sns_topic" "alert_topic" {
  name = "ctdas-alerts"
}