resource "azurerm_resource_group" "main_rg" {
    name     = "bart-rg"
    location = local.region
}
