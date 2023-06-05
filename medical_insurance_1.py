__author__ = 'xuanzee'

'''
A basic analysis via dicts and lists.
File reading with standard CSV library.
'''

import csv

list_of_age = []
list_of_sex = []
list_of_children = []
list_of_smoker = []

list_of_charges = []

list_of_charges_f = [] #female
list_of_charges_m = []
list_of_charges_f_ns = [] #female, non-smoker
list_of_charges_f_ns_c = [] #female, non-smoker, has children
list_of_charges_m_ns = []
list_of_charges_m_ns_c = []
	
with open('insurance.csv', newline='') as csv_file:
	insurance_dict = csv.DictReader(csv_file)

	for row in insurance_dict:
		list_of_age.append(row['age'])
		list_of_sex.append(row['sex'])
		list_of_children.append(row['children'])
		list_of_smoker.append(row['smoker'])

		list_of_charges.append(float(row['charges']))
		
		if row['sex'] == 'female':
			list_of_charges_f.append(float(row['charges']))
			if row['smoker'] == 'no':
				list_of_charges_f_ns.append(float(row['charges']))
				if row['children'] != '0':
					list_of_charges_f_ns_c.append(float(row['charges']))			
		else:
			list_of_charges_m.append(float(row['charges']))
			if row['smoker'] == 'no':
				list_of_charges_m_ns.append(float(row['charges']))
				if row['children'] != '0':
					list_of_charges_m_ns_c.append(float(row['charges']))

def list_item_percentage(one_list, item):
	item_count = one_list.count(item)
	item_percentage = round(item_count / len(one_list), 3) * 100
	result = str(item_percentage) + '%'
	return result

def list_item_avg(one_list):
	total_sum = 0
	for item in one_list:
		total_sum += int(item)
		list_avg = round(total_sum / len(one_list), 2)
	return list_avg

def calc_diff_percent(num_of_interest, num_as_reference):
	if num_of_interest > num_as_reference:
		relation = 'higher'
	else:
		relation = 'lower'
	diff = abs(round(num_of_interest / num_as_reference - 1, 3)) * 100
	return str(diff) + '% ' + relation
	
print('\nTotal participants:', len(list_of_age))
print('Average age:', round(list_item_avg(list_of_age)))
print('% of female participants: ' + list_item_percentage(list_of_sex, 'female'))
print('% of non-smoking participants: ' + list_item_percentage(list_of_smoker, 'no'))
print('% of child-less participants: ' + list_item_percentage(list_of_children, '0'))

print('\nAverage cost: $' + str(list_item_avg(list_of_charges)) + '.')

print('\nAverage cost for a female: $' + str(list_item_avg(list_of_charges_f)) + '.')
print('Average cost for a male: $' + str(list_item_avg(list_of_charges_m)) + '.')
print('Female vs. Male: ' + calc_diff_percent(list_item_avg(list_of_charges_f),
	list_item_avg(list_of_charges_m)))

print('\nAverage cost for a non-smoking female: $' + str(list_item_avg(list_of_charges_f_ns)) + '.')
print('Average cost for a non-smoking male: $' + str(list_item_avg(list_of_charges_m_ns)) + '.')
print('Female vs. Male: ' + calc_diff_percent(list_item_avg(list_of_charges_f_ns),
	list_item_avg(list_of_charges_m_ns)))

print('\nAverage cost for a non-smoking female with children: $' + str(list_item_avg(list_of_charges_f_ns_c)) + '.')
print('Average cost for a non-smoking male with children: $' + str(list_item_avg(list_of_charges_m_ns_c)) + '.')
print('Female vs. Male: ' + calc_diff_percent(list_item_avg(list_of_charges_f_ns_c),
	list_item_avg(list_of_charges_m_ns_c)) +'\n')