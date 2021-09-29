from simple_report import SimpleReport


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


'''
products = [
    {
        "id": 1,
        "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
        "instrucoes_de_armazenamento": "in blandit ultrices enim",
    },
    {
        "id": 2,
        "nome_do_produto": "sodium ferric gluconate complex",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2020-05-31",
        "data_de_validade": "2023-01-17",
        "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
        "instrucoes_de_armazenamento": "duis bibendum morbi",
    },
    {
        "id": 3,
        "nome_do_produto": "Dexamethasone Sodium Phosphate",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2019-09-13",
        "data_de_validade": "2023-02-13",
        "numero_de_serie": "BA52 2034 8595 7904 7131",
        "instrucoes_de_armazenamento": "morbi quis tortor id",
    },
    {
        "id": 4,
        "nome_do_produto": "Uricum acidum, Benzoicum acidum",
        "nome_da_empresa": "Newton Laboratories",
        "data_de_fabricacao": "2019-11-08",
        "data_de_validade": "2019-11-25",
        "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
        "instrucoes_de_armazenamento": "velit eu est congue elementum",
    },
]

CompleteReport.generate(products)
'''
