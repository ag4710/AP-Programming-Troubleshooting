tot_list = [['Australia', '0', '2', '1'], ['Austria', '4', '8', '5'], ['Belarus', '5', '0', '1'], ['Canada', '10', '10', '5'], ['China', '3', '4', '2'], ['Croatia', '0', '1', '0'], ['Czech Republic', '2', '4', '2'], ['Finland', '1', '3', '1'], ['France', '4', '4', '7'], ['Germany', '8', '6', '5'], ['Great Britain', '1', '1', '2'], ['Italy', '0', '2', '6'], ['Japan', '1', '4', '3'], ['Kazakhstan', '0', '0', '1'], ['Latvia', '0', '2', '2'], ['Netherlands', '8', '7', '9'], ['Norway', '11', '5', '10'], ['Poland', '4', '1', '1'], ['Russia', '13', '11', '9'], ['Slovakia', '1', '0', '0'], ['Slovenia', '2', '2', '4'], ['South Korea', '3', '3', '2'], ['Sweden', '2', '7', '6'], ['Switzerland', '6', '3', '2'], ['Ukraine', '1', '0', '1'], ['United States', '9', '7', '12']]

countries = ["Australia", "Austria", "Belarus", "Canada", "China", "Croatia", "Czech Republic", "Finland", "France", "Germany", "Great Britain", "Italy", "Japan", "Kazakhstan", "Latvia", "Netherlands", "Norway", "Poland", "Russia", "Slovakia", "Slovenia", "South Korea", "Sweden", "Switzerland", "Ukraine", "United States"]
gold = ["0", "4", "5", "10", "3", "0", "2", "1", "4", "8", "1", "0", "1", "0", "0", "8", "11", "4", "13", "1", "2", "3", "2", "6", "1", "9"]
silver = ["2", "8", "0", "10", "4", "1", "4", "3", "4", "6", "1", "2", "4", "0", "2", "7", "5", "1", "11", "0", "2", "3", "7", "3", "0", "7"]
bronze = ["1", "5", "1", "5", "2", "0", "2", "1", "7", "5", "2", "6", "3", "1", "2", "9", "10", "1", "9", "0", "4", "2", "6", "2", "1", "12"]

for country in countries:
    print(country)

for i in range(len(countries)):
    print(countries[i], int(gold[i])+int(silver[i])+int(bronze[i]))

totals = []
for i in range(len(countries)):
    medals = int(gold[i])+int(silver[i])+int(bronze[i])
    totals.append( (medals, countries[i]) )

print(totals)

totals.sort()
totals.reverse()

top_ten = totals[:10]
for p in top_ten:
    medals, country = p
    print(medals, country)

table = []
for i in range(len(countries)):
    table.append( (gold[i], silver[i], bronze[i],
    countries[i]) ) 
    table.sort()
    top_ten = table[-10:]
    top_ten.reverse()
for g, s, b, country in top_ten: 
    print(country, g, s, b)