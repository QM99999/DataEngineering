
variable "credentials_file" {
  description = "Path to the service account key file."
  type        = string
  default     = "./keys/my-creds.json"
}

variable "project_id" {
  description = "The ID of the project in which to create resources."
  type        = string
  default     = "dataengineer-498819"
}

variable "region" {
  description = "The region in which to create resources."
  type        = string
  default     = "europe-west3"
}

variable "location" {
  description = "The location of the resources."
  type        = string
  default     = "EU"
}

variable "bigquery_dataset_id" {
  description = "The ID of the BigQuery dataset."
  type        = string
  default     = "demo_dataset"
}