from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith('.csv'):
            csv = Inventory.open_and_convert_to_dict_csv_file(path)
            return csv
        else:
            raise ValueError("Arquivo inválido")
