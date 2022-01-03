resource "azurerm_container_registry" "acr" {
    name                = "bartacr"
    resource_group_name = azurerm_resource_group.main_rg.name
    location            = local.region

    admin_enabled = true
    sku           = "Basic"
}