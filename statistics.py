import pandas

data_for_computing = pandas.read_csv('Titanik.csv', sep=';', encoding='CP866', index_col='PassengerId') 

female_number_stat = data_for_computing[data_for_computing['Sex'] == 'female'].count()['Sex']

male_number_stat = data_for_computing[data_for_computing['Sex'] == 'male'].count()['Sex']

men_stat = round((male_number_stat * 100) / (len(data_for_computing)-1), 2)

women_stat = 100 - men_stat

survived_stat = round((data_for_computing['Survived'].value_counts()[1]*100) / (len(data_for_computing)-1), 3)


ages_of_survived_pips = data_for_computing.loc[(data_for_computing["Survived"] == 1), "Age"].values #список возрастов выживших
sum_age = 0.0
length1=0
for pip in ages_of_survived_pips:
    if ( (type(pip) == str) and (len(pip) <= 3) ):
        pip = float(pip)
        sum_age = sum_age + pip
        length1 = length1 + 1
print("кол-во выживших людей, у которых есть инф. о возрасте- ", length1)
average_surv_age = round(sum_age / length1, 3)


ages_of_dead_pips = data_for_computing.loc[(data_for_computing["Survived"] == 0), "Age"].tolist() #список возрастов погибших ---запись метода эквивалента предыдущему методу с выжившими
sum_age = 0.0
length2 = 0
for pip in ages_of_dead_pips:
    if ( (type(pip) == str) and (len(pip) <= 3) ):
        pip = float(pip)
        sum_age = sum_age + pip
        length2 = length2 + 1

print ("кол-во погибших людей, у которых есть инф. о возрасте-  ", length2)
average_dead_age = round(sum_age / length2, 3)



#print ("Кол-во строк в файле БЕЗ УЧЕТА шапки - ", (len(data_for_computing)-1) )
print ("Процент женщин на корабле - ", women_stat)
print ("Процент мужчин на корабле - ", men_stat)
print ("Процент выживших - ", survived_stat)
print ("Средний возраст выживших - ", average_surv_age)
print ("Средний возраст погибших - ", average_dead_age)
