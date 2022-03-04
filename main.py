import StudiKasus2
import os
import pandas as pd

case = StudiKasus2.StudiKasus2('localhost', '3306', 'root', os.environ["MYSQLPASS"])
df = case.import_csv('titanic.csv')
print(case.create_db('Titanic'))
print(case.create_table('Titanic', 'passengers', df))
print(case.load_data('Titanic', 'passengers'))