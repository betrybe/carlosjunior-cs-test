from datetime import datetime


class SimpleReport:

    @classmethod
    def earliest_manufacture_date(self, list_dict):
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

    @classmethod
    def closest_expiration_date(self, list_dict):
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

    @classmethod
    def largest_stocked_products(self, list_dict):
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

    @classmethod
    def generate(self, list_dict=[]):
        '''
            1. data de fabricação mais antiga
            2. data de validade mais próxima
            3. empresa com maior estoque de produtos
        '''
        out = (
            "Data de fabricação mais antiga: " +
            self.earliest_manufacture_date(list_dict) + "\n" +
            "Data de validade mais próxima: " +
            self.closest_expiration_date(list_dict) + "\n" +
            "Empresa com maior quantidade de produtos estocados: " +
            self.largest_stocked_products(list_dict) + "\n"
        )

        return out
