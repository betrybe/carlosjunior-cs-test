from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from csv import reader


class Inventory:
    @classmethod
    def create_dict_from_arq_matrix(self, arq_matrix):
        arq_dict = []

        for line in range(1, len(arq_matrix)):
            obj = {}
            for col in range(0, len(arq_matrix[0])):
                obj[arq_matrix[0][col]] = arq_matrix[line][col]

            arq_dict.append(obj)

        return arq_dict

    @classmethod
    def import_data(self, path, report_type):
        list_arq_matrix = []
        with open(path, 'r') as csv_file:
            csv_reader = reader(csv_file)
            list_of_rows = list(csv_reader)
            list_arq_matrix.append(list_of_rows)

        arq_dict = self.create_dict_from_arq_matrix(list_arq_matrix[0])

        if report_type == 'simples':
            return SimpleReport.generate(arq_dict)
        elif report_type == 'completo':
            return CompleteReport.generate(arq_dict)
        else:
            return 'Erro no parâmetro report_type'
