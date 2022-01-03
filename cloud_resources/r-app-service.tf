resource "azurerm_app_service_plan" "app_service_plan" {
    name                = "bart-app-service-plan"
    resource_group_name = azurerm_resource_group.main_rg.name
    location            = local.region
    kind                = "Linux"
    reserved            = true

    sku {
        tier = "Basic"
        size = "B1"
    }
}

resource "azurerm_app_service" "app_service" {
    name                = "bart-app-service"
    resource_group_name = azurerm_resource_group.main_rg.name
    location            = local.region  
    app_service_plan_id = azurerm_app_service_plan.app_service_plan.id

    site_config {
        linux_fx_version = "DOCKER|${azurerm_container_registry.acr.login_server}/api"
        always_on        = "true"
        cors {
            allowed_origins = ["*"]
        }
    }

    app_settings = {
        "DOCKER_ENABLE_CI" = true
    }
}