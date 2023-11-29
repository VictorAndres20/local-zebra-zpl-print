from zebra import Zebra


def print_zebra(label: str, driver: str):
    label = ("^XA^FX Third section with bar code.^BY3,1,120^FO50,50^BC^FD1234567891234^FS^FX Second section with recipient address and permit information.^CFA,30^FO50,220^FDOrden: 204567^FS^FO50,260^FDMANUFACTURAS LOS YO NO SE QUE SAS^FS^FO50,300^FDRef: 12345678912^FS^FO400,300^FDColor: 9182736453652635^FS^FO50,340^FDCantidad: 1234567 MTS - 4568 KG^FS^^XZ")
    # This is the name of the printer, in my case, is "ZDesigner ZD220-203dpi ZPL"
    z = Zebra(driver)
    z.output(label)
