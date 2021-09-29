from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from csv import reader
import json
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def create_dict_from_file_matrix(self, file_matrix):
        file_dict = []

        for line in range(1, len(file_matrix)):
            obj = {}
            for col in range(0, len(file_matrix[0])):
                obj[file_matrix[0][col]] = file_matrix[line][col]

            file_dict.append(obj)

        return file_dict

    @classmethod
    def import_data(self, path, report_type):
        file_dict = []

        if path.endswith('.csv'):
            list_file_matrix = []

            with open(path, 'r') as csv_file:
                csv_reader = reader(csv_file)
                list_of_rows = list(csv_reader)
                list_file_matrix.append(list_of_rows)

            file_dict = self.create_dict_from_file_matrix(list_file_matrix[0])

        elif path.endswith('.json'):
            with open(path) as json_file:
                file = json.load(json_file)

            file_dict = file

        elif path.endswith('.xml'):
            root = ET.parse(path).getroot()
            registers = root.findall("record")
            file = []
            for each_register in registers:
                file_dict = {}
                for tag in each_register:
                    file_dict[tag.tag] = tag.text
                file.append(file_dict)

            file_dict = file

        else:
            return 'Formato de arquivo não tratado'

        if report_type == 'simples':
            return SimpleReport.generate(file_dict)
        elif report_type == 'completo':
            return CompleteReport.generate(file_dict)
        else:
            return 'Erro no parâmetro report_type'
