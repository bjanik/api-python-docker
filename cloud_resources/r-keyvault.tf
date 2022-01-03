resource "azurerm_key_vault" "kv" {
    name                = "bart-key-vault"
    resource_group_name = azurerm_resource_group.main_rg.name
    location            = local.region
    tenant_id           = local.tenant_id
    sku_name            = "standard"
}

resource "azurerm_key_vault_secret" "acr_user" {
    name         = "acr-user"
    value        = azurerm_container_registry.acr.admin_username
    key_vault_id = azurerm_key_vault.kv.id
}

resource "azurerm_key_vault_secret" "acr_password" {
    name         = "acr-password"
    value        = azurerm_container_registry.acr.admin_password
    key_vault_id = azurerm_key_vault.kv.id
}

resource "azurerm_key_vault_access_policy" "kv_policy" {
    key_vault_id = azurerm_key_vault.kv.id
    tenant_id    = local.tenant_id
    object_id    = local.object_id

    secret_permissions = [
        "List",
        "Get",
        "Set",
        "Delete"
    ]
}