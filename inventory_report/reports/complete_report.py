from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def quantity_product_per_employ(self, list_dict):
        out = "Produtos estocados por empresa: \n"

        if len(list_dict) == 0:
            return out + '- Lista de produtos vazia'

        if len(list_dict) == 1:
            return out + "- " + list_dict[0]['nome_da_empresa'] + ": " + "1"

        '''
            guardaremos todas as empresas e posteriormente guardaremos
            todas as empresas, sem repetições, para contarmos quantas vezes
            elas se repetem na lista de produtos
        '''
        companies_list = [
            each_company["nome_da_empresa"] for each_company in list_dict
        ]
        companies_freq = Counter(companies_list)

        out = "Produtos estocados por empresa: \n"
        for company in companies_freq:
            out += "- "+str(company)+": "+str(companies_freq[company])+"\n"

        return out

    @classmethod
    def generate(self, list_dict):
        '''
            quantidade de produtos estocados por empresa
        '''
        out = (
            super().generate(list_dict) + "\n" +
            self.quantity_product_per_employ(list_dict)
        )

        return out
