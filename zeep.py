from zeep import Client

client = Client('https://efaturawstest.fitbulut.com/ClientEInvoiceServices/ClientEInvoiceServicesPort.svc')
# result = client.service.ConvertSpeed(
#     100, 'kilometersPerhour', 'milesPerhour')
#
# assert result == 62.137