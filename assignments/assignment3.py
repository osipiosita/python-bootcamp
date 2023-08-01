def min_index(mylist):
    smallest = mylist[0]
    for i in range(len(mylist)):
        if mylist[i] < smallest:
            smallest = mylist[i]
            ind = mylist.index(smallest)
    return ind
print(min_index([40,50,10,90,100,5, 20, 2, 45]))

def max_index(mylist):
    largest = mylist[0]
    for i in range(len(mylist)):
        if mylist[i] > largest:
            largest = mylist[i]
            ind = mylist.index(largest)
    return ind
print(max_index([40,50,10,90,100,5, 20, 2, 45]))

def smaller_indices(list1, list2):
    list3 = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] < list2[i]:
                list3.append(i)
        return list3
    else:
        print('lists MUST be of equal length!')
print(smaller_indices([40,50,10,90,100,70], [60,20,19,95,30,20]))


def pairwise_product(list1,list2):
    list3 = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            product = list1[i] * list2[i]
            list3.append(product)
        return list3
    else:
        print('lists MUST be of equal length!')
print(pairwise_product([40,50,10,90], [6,2,2,5]))


def pairwise_ratio(list1,list2):
    list3 = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            ratio = list1[i] / list2[i]
            list3.append(round(ratio,3))
        return list3
    else:
        print('lists MUST be of equal length!')
print(pairwise_ratio([40,50,10,90], [60,20,19,95]))
with open('CountryData.csv', 'r') as f:
    country_name = []
    population = []
    literacy_rate = []
    mobile_subscriptions = []
    internet_users = [] 
    elec_production = []
    elec_consumption = []
    produce_more_elec = []
    consume_more_elec = []
    country_and_index = {}
    list_of_lines = f.readlines()
    for line in range(1,len(list_of_lines)):
        newline = list_of_lines[line].strip('\n')
        each_line = newline.split(',')
        country_name.append(each_line[0])
        population.append(each_line[1])
        literacy_rate.append(each_line[2])
        mobile_subscriptions.append(each_line[3])
        internet_users.append(each_line[4])
        elec_production.append(each_line[5])
        elec_consumption.append(each_line[6])
   
    for country in range(len(country_name)):
        country_and_index[country_name[country]] = country
    #print(my_dict)
    def country_data():
        coun_name = input('Enter country of choice: ').lower()
        for i in country_and_index:
            if coun_name == i.lower():
                ind = country_and_index[i]
                subs_per_capita = float(mobile_subscriptions[ind]) / float(population[ind])
                internet_per_capita = float(internet_users[ind]) / float(population[ind])
                value = f'{country_name[ind]}    {subs_per_capita}    {internet_per_capita}'
    
        print(f"{country_name[ind]} has a population of {int(population[ind]):,} and a\
 literacy rate of {literacy_rate[ind]}%.\nThe estimate of the number of mobile Subscriptions is {int(mobile_subscriptions[ind]):,}, \n\
while that of internet Users is {int(internet_users[ind]):,}. \n{country_name[ind]} produces {elec_production[ind]} billion kWh of electricity\
 annually, while it consumes {elec_consumption[ind]} kWh of electricity.")
        return value
    
    def func2():
        max_subscription_percapita = int(mobile_subscriptions[0]) / int(population[0])
        min_subscription_percapita = int(mobile_subscriptions[0]) / int(population[0])
        max_internet_perxapita = int(internet_users[0]) / int(population[0])
        min_internet_perxapita = int(internet_users[0]) / int(population[0])
        largest_literacy_rate = float(literacy_rate[0])
        lowest_literacy_rate = float(literacy_rate[0])
        largest_pop = int(population[0])
        total_pop = 0
        lit_rate_by_pop = 0
        for i in population:
          total_pop+= int(i)
        print(f"Africa's population is {total_pop:,}")
        for j in range(len(population)):
            if int(population[j]) > largest_pop:
                largest_pop = int(population[j])
                most_populated_country = country_name[j]
            if float(literacy_rate[j]) > largest_literacy_rate:
                largest_literacy_rate = float(literacy_rate[j])
                country_highest_literacy = country_name[j]
            if float(literacy_rate[j]) < lowest_literacy_rate:
                lowest_literacy_rate = float(literacy_rate[j])
                country_lowest_literacy = country_name[j]
            if (int(mobile_subscriptions[j])/int(population[j])) > max_subscription_percapita:
                max_subscription_percapita = (int(mobile_subscriptions[j])/int(population[j]))
                subs_country_max = country_name[j]
            if (int(mobile_subscriptions[j])/int(population[j])) < min_subscription_percapita:
                min_subscription_percapita = (int(mobile_subscriptions[j])/int(population[j]))
                subs_country_min = country_name[j]
            if (int(internet_users[j])/int(population[j])) > max_internet_perxapita:
                max_internet_perxapita = (int(internet_users[j])/int(population[j]))
                internet_max = country_name[j]
            if (int(internet_users[j])/int(population[j])) < min_internet_perxapita:
                min_internet_perxapita = (int(internet_users[j])/int(population[j]))
                internet_min = country_name[j]
            if int(elec_production[j]) > int(elec_consumption[j]):
                produce_more_elec.append(country_name[j])
            if int(elec_production[j]) < int(elec_consumption[j]):
                consume_more_elec.append(country_name[j])
            
            lit_rate_by_pop += (float(literacy_rate[j])/100) * float(population[j])
        statement1 = ''
        statement2 = ''
        for i in produce_more_elec:
            statement1 = statement1 + i + ', '
        for m in consume_more_elec:
            statement2 = statement2 + m + ','
        print(f'Most populated African country is {most_populated_country}')
        print(f'{country_highest_literacy} has the highest literacy rate')
        print(f'{country_lowest_literacy} has the lowest literacy rate')
        average_lit_rate = round((lit_rate_by_pop/total_pop)*100, 2)
        print(f'The average literacy rate in Africa is {average_lit_rate}')
        print(f'{subs_country_max} has the highest mobile subscriptions per capita being {max_subscription_percapita}')
        print(f'{subs_country_min} has the lowest mobile subscriptions per capita being {min_subscription_percapita}')
        print(f'{internet_max} has the lowest mobile subscriptions per capita being {max_internet_perxapita}')
        print(f'{internet_min} has the lowest mobile subscriptions per capita being {min_internet_perxapita}')
        print(f'{statement1} produce more electricity than they consume.')
        print(f'{statement2} consume more electricity than they produce.')
    func2()
    
               
            


with open('myfile.txt', 'a') as wfile:
    def func():
        wfile.write('\n'+ str(country_data()))
    #func()
