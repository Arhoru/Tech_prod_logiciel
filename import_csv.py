# sources:  https://docs.python.org/3.6/library/csv.html#csv.reader
#           https://docs.python.org/3.6/library/csv.html#csv-fmt-params
#           https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
#           https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
import csv

with open('src_csv/23440003400026_J335_installations_table.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    #for row in spamreader:
    #    print(', '.join(row))
