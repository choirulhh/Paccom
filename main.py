from tabulate import tabulate

import math

class User:
    data = {
        'Sumbul' : 'Platinum',
        'Ana' : 'Gold',
        'Cahya' : 'Platinum'
    }

    def __init__(self, username, membership = None):
        self.username = username
        self.membership = membership

    def show_benefit(self):
        benefit = [
            ["Platinum", "15%", "Benefit Gold + Silver + Cashback max. 30%"],
            ["Gold", "10%", "Benefit Silver + Voucher Ojek Online"],
            ["Silver", "8%", "Voucher Makanan"],
        ]

        benefit_headers = ["Membership", "Discount", "Another Benefit"]

        print('Paccommerce Membership Benefit')
        print(tabulate(benefit,benefit_headers,tablefmt ='fancy_grid',stralign = 'center'))

    def show_requirement(self):
        '''
        Fungsi ini digunakan untuk mencetak requirement untuk mencapai benefit tier tertentu
        input: None
        '''
        data_requirement = [
        {
            "Membership": "Platinum",
            "Expense" : 8,
            "Income" : 15
        },
        {
            "Membership": "Gold",
            "Expense" : 6,
            "Income" : 10
        },
        {
            "Membership": "Silver",
            "Expense" : 5,
            "Income" : 7
        }
         ]

        headers_requirement = list(x for x in data_requirement[0].keys())
        content_requirement = list(list(x.values()) for x in data_requirement)

        print("Detail requirement based on membership tier")
        print("")
        table = tabulate(content_requirement, headers = headers_requirement, tablefmt = 'fancy_grid', stralign = 'center')
        print(table)


