from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith('.json'):
            json = Inventory.open_and_convert_to_dict_json_file(path)
            return json
        else:
            raise ValueError("Arquivo inválido")
