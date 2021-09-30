from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    pass
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)
    else:
        _, path, report_type = sys.argv
        if path.endswith('.csv'):
            instance = InventoryRefactor(CsvImporter)
        elif path.endswith('.json'):
            instance = InventoryRefactor(JsonImporter)
        elif path.endswith('.xml'):
            instance = InventoryRefactor(XmlImporter)
        else:
            return print("Formato de arquivo não tratado")

        report = instance.import_data(path, report_type)
        print(report, end="")
