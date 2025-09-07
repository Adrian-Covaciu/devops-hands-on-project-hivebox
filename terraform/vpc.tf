locals {
  public_subnets = {
    0 = { cidr_block = "10.0.0.0/24"
      availability_zone = "us-east-1a"
    }
    1 = { cidr_block = "10.0.1.0/24",
      availability_zone = "us-east-1b"
    }
  }

  private_subnets = {
    0 = { cidr_block = "10.0.2.0/24",
      availability_zone = "us-east-1a"
    }
    1 = { cidr_block = "10.0.3.0/24",
      availability_zone = "us-east-1b"
    }
  }
}

## VPC
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr_block

  tags = {
    Name        = "${var.application_name}-${var.environment_name}-network"
    application = var.application_name
    environment = var.environment_name
  }
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  depends_on = [aws_vpc.main]
}


## PUBLIC SUBNET
resource "aws_subnet" "public" {

  for_each = local.public_subnets

  vpc_id                  = aws_vpc.main.id
  availability_zone       = each.value.availability_zone
  cidr_block              = each.value.cidr_block
  map_public_ip_on_launch = true

  tags = {
    "Name" = "public-${each.value.availability_zone}"
  }

}

# must allow IGW access to the internet
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  depends_on = [
    aws_vpc.main,
    aws_internet_gateway.main
  ]
}

resource "aws_route_table_association" "public" {

  for_each = aws_subnet.public

  subnet_id      = each.value.id
  route_table_id = aws_route_table.public.id

}


## PRIVATE SUBNET
resource "aws_subnet" "private" {

  for_each = local.private_subnets

  vpc_id            = aws_vpc.main.id
  availability_zone = each.value.availability_zone
  cidr_block        = each.value.cidr_block

  tags = {
    "Name" = "private-${each.value.availability_zone}"
  }

}

resource "aws_route_table" "private" {

  for_each = local.private_subnets

  vpc_id = aws_vpc.main.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat[each.key].id
  }
}

resource "aws_route_table_association" "private" {

  for_each = local.private_subnets

  subnet_id      = aws_subnet.private[each.key].id
  route_table_id = aws_route_table.private[each.key].id

}

resource "aws_eip" "nat" {

  for_each = local.private_subnets

}

resource "aws_nat_gateway" "nat" {

  for_each = local.private_subnets

  allocation_id = aws_eip.nat[each.key].id
  subnet_id     = aws_subnet.public[each.key].id

  depends_on = [
    aws_internet_gateway.main,
    aws_eip.nat
  ]

}
