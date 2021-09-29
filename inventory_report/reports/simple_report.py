from datetime import datetime


class SimpleReport(object):

    @staticmethod
    def generate(list_dict):
        '''
            1. data de fabricação mais antiga
            2. data de validade mais próxima
            3. empresa com maior estoque de produtos
        '''
        def earliest_manufacture_date(list_dict):
            '''
                averíguo se a lista está vazia, pois em caso positivo não
                haverá produto mais antigo
            '''
            if len(list_dict) == 0:
                return 'Lista de produtos vazia'
            '''
                averíguo se existe 1 produto, pois em caso positivo ele
                será o mais antigo
            '''
            if len(list_dict) == 1:
                return list_dict[0]['data_de_fabricacao']
            '''
                caso chegue aqui, então temos mais de um produto para
                averiguar qual é o mais antigo
            '''
            obj = list_dict[0]

            for i in range(1, len(list_dict)):
                formatted_date1 = datetime.strptime(
                    obj['data_de_fabricacao'], '%Y-%m-%d'
                ).date()
                formatted_date2 = datetime.strptime(
                    list_dict[i]['data_de_fabricacao'], '%Y-%m-%d'
                ).date()

                if formatted_date1 > formatted_date2:
                    obj = list_dict[i]

            return obj['data_de_fabricacao']

        def closest_expiration_date(list_dict):
            if len(list_dict) == 0:
                return 'Lista de produtos vazia'

            if len(list_dict) == 1:
                return list_dict[0]['data_de_validade']
            '''
                caso chegue aqui, então temos mais de um produto para
                averiguar qual tem a data de validade mais próxima, mas
                antes faremos uma nova lista sem os produtos vencidos
            '''
            new_list = []

            for each_obj in list_dict:
                formatted_date = datetime(
                    int(each_obj['data_de_validade'].split('-')[0]),
                    int(each_obj['data_de_validade'].split('-')[1]),
                    int(each_obj['data_de_validade'].split('-')[2])
                )

                if formatted_date >= datetime.now():
                    new_list.append(each_obj)

            '''
                averíguo se há produtos na nova lista, pois se não
                houver todos estão vencidos
            '''
            if len(new_list) < 1:
                return 'Todos produtos vencidos'

            obj = new_list[0]

            for i in range(1, len(new_list)):
                formatted_date1 = datetime.strptime(
                    obj['data_de_validade'], '%Y-%m-%d'
                ).date()
                formatted_date2 = datetime.strptime(
                    list_dict[i]['data_de_validade'], '%Y-%m-%d'
                ).date()

                if formatted_date1 > formatted_date2:
                    obj = new_list[i]

            return obj['data_de_validade']

        def largest_stocked_products(list_dict):
            if len(list_dict) == 0:
                return 'Lista de produtos vazia'

            if len(list_dict) == 1:
                return list_dict[0]['nome_da_empresa']

            '''
                passaremos o nome da empresa de cada produto
                para uma lista. assim, podemos contar a frequência
                de cada uma posteriormente
            '''
            companies_list = []
            for each_obj in list_dict:
                companies_list.append(each_obj['nome_da_empresa'])

            max = 0
            company = companies_list[0]
            for each_company in companies_list:
                freq = companies_list.count(each_company)
                if freq > max:
                    max = freq
                    company = each_company

            return company

        out = (
            "Data de fabricação mais antiga: " +
            earliest_manufacture_date(list_dict) + "\n" +
            "Data de validade mais próxima: " +
            closest_expiration_date(list_dict) + "\n" +
            "Empresa com maior quantidade de produtos estocados: " +
            largest_stocked_products(list_dict) + "\n"
        )

        return out


list = [
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
        "nome_da_empresa": "Newton Laboratories, Inc.",
        "data_de_fabricacao": "2019-11-08",
        "data_de_validade": "2019-11-25",
        "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
        "instrucoes_de_armazenamento": "velit eu est congue elementum",
    },
]

SimpleReport.generate(list)
