from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def open_and_convert_to_dict_csv_file(self, path):
        with open(path) as csv_file:
            file_dict = list(csv.DictReader(csv_file))

        return file_dict

    @classmethod
    def open_and_convert_to_dict_json_file(self, path):
        with open(path) as json_file:
            file_dict = json.load(json_file)

        return file_dict

    @classmethod
    def open_and_convert_to_dict_xml_file(self, path):
        root = ET.parse(path).getroot()
        registers = root.findall("record")
        file = []
        for each_register in registers:
            file_dict = {}
            for tag in each_register:
                file_dict[tag.tag] = tag.text
            file.append(file_dict)

        return file

    @classmethod
    def import_data(self, path, report_type):
        file_dict = []

        if path.endswith('.csv'):
            file_dict = self.open_and_convert_to_dict_csv_file(path)
        elif path.endswith('.json'):
            file_dict = self.open_and_convert_to_dict_json_file(path)
        elif path.endswith('.xml'):
            file_dict = self.open_and_convert_to_dict_xml_file(path)
        else:
            return 'Formato de arquivo não tratado'

        if report_type == 'simples':
            return SimpleReport.generate(file_dict)
        elif report_type == 'completo':
            return CompleteReport.generate(file_dict)
        else:
            return 'Erro no parâmetro report_type'
