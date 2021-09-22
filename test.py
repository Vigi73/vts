from models import List
from prettytable import PrettyTable
import re

inp = input('|>')

my_table = PrettyTable()
query = List.select().where(
    List.Fio ** f'%{inp.upper()}%' | List.Name ** f'%{inp.upper()}%' | List.Vts ** f'%{inp.upper()}%')

my_table.field_names = ['№', 'ОТДЕЛ', 'ФИО', 'СОТОВЫЙ', 'ВТС', 'ГОРОДСКОЙ']

for i, data in enumerate(query, start=1):
    mobil = re.findall(r'8-\d\d\d-\d\d\d-\d\d-\d\d', data.Fio)
    FIO = ' '.join(data.Fio.split()[:3])
    my_table.add_row([i, data.Name, FIO, ' '.join(mobil), data.Vts, data.City])

my_table.max_width = 62

print(my_table)
