az group create --name Azuredevops3 --location westus3
az webapp up --sku F1 --name azvargaspred --os-type Linux --resource-group Azuredevops3 --runtime "PYTHON:3.10"
