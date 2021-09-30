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
        file_dict = []
        for each_register in registers:
            obj = {}
            for tag in each_register:
                obj[tag.tag] = tag.text
            file_dict.append(obj)

        return file_dict

    @classmethod
    def import_data(self, path, report_type):
        if path.endswith('.csv'):
            file_dict = self.open_and_convert_to_dict_csv_file(path)
        if path.endswith('.json'):
            file_dict = self.open_and_convert_to_dict_json_file(path)
        if path.endswith('.xml'):
            file_dict = self.open_and_convert_to_dict_xml_file(path)
        if report_type == 'simples':
            report = SimpleReport.generate(file_dict)
        else:
            report = CompleteReport.generate(file_dict)

        return report
