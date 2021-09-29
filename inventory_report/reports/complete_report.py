from inventory_report.reports.simple_report import SimpleReport


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
        companies_list = []
        for each_obj in list_dict:
            companies_list.append(each_obj['nome_da_empresa'])

        companies_list_unique = []
        quantity_product = []

        for each_company in companies_list:
            if each_company not in companies_list_unique:
                companies_list_unique.append(each_company)

        for each_company in companies_list_unique:
            freq = companies_list.count(each_company)
            quantity_product.append(str(freq))

        for i in range(len(companies_list_unique)):
            out += "- "+companies_list_unique[i]+": "+quantity_product[i]+"\n"

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

        # print(out)

        return out
