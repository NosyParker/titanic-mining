import pandas

data_for_computing = pandas.read_csv(
        'Titanik.csv', sep=';', encoding='CP866', index_col='PassengerId')

data_for_computing['FirstName'] = data_for_computing['Name'].str.extract(
    '(Mr\. |Dr\. |Don\. |Rev\. |Major\. |Capt\. |Miss\. |Master\. |Mrs\.[A-Za-z ]*\()([A-Za-z]*)')[1]

names = data_for_computing['FirstName'].value_counts()
print(names)


# print (data_for_computing.loc[data_for_computing["FirstName"] =='William'].count()["Name"])
#print(data_for_computing["FirstName"])