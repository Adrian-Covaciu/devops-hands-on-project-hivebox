variable "application_name" {
  type = string
}
variable "environment_name" {
  type = string
}
variable "primary_region" {
  type = string
}
variable "vpc_cidr_block" {
  type = string
}
variable "kubernetes_version"{
  type = string
  default = 1.33
}
variable "node_image_type" {
  type = string
  default = "AL2023_x86_64_STANDARD"
}
variable "node_size" {
  type = string
  default = "t3.small"
}
variable "eks_addons" {
  type = list(object({
    name          = string
    version       = string
  }))
  default = [
    {
      name          = "coredns"
      version       = "v1.12.2-eksbuild.4"
    },
    {
      name          = "kube-proxy"
      version       = "v1.33.3-eksbuild.4"
    },
    {
      name          = "vpc-cni"
      version       = "v1.20.1-eksbuild.1"
    }
  ]
}
variable "k8s_namespace" {
  type = string
}
variable "k8s_service_account_name" {
  type = string
}
