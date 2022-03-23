from prettytable import PrettyTable
table = PrettyTable()

table.add_column('rank', ['1','2','3','4'])
table.add_column('points', ['12','10','9','6'])


print(table)