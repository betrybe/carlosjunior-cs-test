from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith('.xml'):
            xml = Inventory.open_and_convert_to_dict_xml_file(path)
            return xml
        else:
            raise ValueError("Arquivo inválido")
