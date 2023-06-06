__author__ = 'xuanzee'

'''
A basic analysis via dicts and lists, with file reading with standard CSV library.
'''

import csv

#List initialization
list_of_sex = []
list_of_age = []
list_of_children = []
list_of_smoker = []
list_of_bmi = []
list_of_region = []

list_of_age_f= [] #ages of females
list_of_children_f = []
list_of_smoker_f = []
list_of_bmi_f = []
list_of_region_f = []

list_of_age_m= []
list_of_children_m = []
list_of_smoker_m = []
list_of_bmi_m = []
list_of_region_m = []

list_of_charges = []
list_of_charges_f = [] #costs of females
list_of_charges_f_ns = [] #costs of non-smoking females
list_of_charges_f_ns_c = [] #costs of non-smoking females with children
list_of_charges_m = []
list_of_charges_m_ns = []
list_of_charges_m_ns_c = []

list_of_age_f_ns_c = [] #ages of non-smoking females with children
list_of_age_m_ns_c = []

#Compile lists	
with open('insurance.csv', newline='') as csv_file:
	insurance_dict = csv.DictReader(csv_file)

	for row in insurance_dict:
		list_of_sex.append(row['sex'])
		list_of_age.append(row['age'])
		list_of_children.append(row['children'])
		list_of_smoker.append(row['smoker'])
		list_of_bmi.append(row['bmi'])
		list_of_region.append(row['region'])

		list_of_charges.append(float(row['charges']))
		
		if row['sex'] == 'female':
			list_of_age_f.append(row['age'])
			list_of_children_f.append(row['children'])
			list_of_smoker_f.append(row['smoker'])
			list_of_bmi_f.append(row['bmi'])
			list_of_region_f.append(row['region'])
			list_of_charges_f.append(float(row['charges']))
			if row['smoker'] == 'no':
				list_of_charges_f_ns.append(float(row['charges']))
				if row['children'] != '0':
					list_of_charges_f_ns_c.append(float(row['charges']))
					list_of_age_f_ns_c.append(row['age'])
		else:
			list_of_age_m.append(row['age'])
			list_of_children_m.append(row['children'])
			list_of_smoker_m.append(row['smoker'])
			list_of_bmi_m.append(row['bmi'])
			list_of_region_m.append(row['region'])
			list_of_charges_m.append(float(row['charges']))
			if row['smoker'] == 'no':
				list_of_charges_m_ns.append(float(row['charges']))
				if row['children'] != '0':
					list_of_charges_m_ns_c.append(float(row['charges']))
					list_of_age_m_ns_c.append(row['age'])

#Define functions
def list_item_percentage(one_list, item):
	'''
	Calculate the percentage of a specified item in one list.
	'''
	item_count = one_list.count(item)
	item_percentage = round(item_count / len(one_list) * 100, 1)
	result = str(item_percentage) + '%'
	return result

def list_item_avg(one_list):
	'''
	Calculate the average of all items in one list.
	'''
	total_sum = 0
	for item in one_list:
		total_sum += float(item)
		list_avg = round(total_sum / len(one_list), 2)
	return list_avg

def calc_diff_percent(num_of_interest, num_as_reference):
	'''
	Calculate the percentage difference between the two values.
	'''
	if num_of_interest > num_as_reference:
		relation = 'higher'
	else:
		relation = 'lower'
	diff = abs(round(num_of_interest / num_as_reference - 1, 3)) * 100
	return str(diff) + '% ' + relation

def unique_in_list(one_list):
	'''
	Create a new list with unique values from an existing list.
	'''
	unique_list = []
	for i in one_list:
		if i not in unique_list:
			unique_list.append(i)
	return unique_list

def majority_item(one_list):
	'''
	Find the most prevelant item(s) (up to 2) in a list.
	'''
	item = unique_in_list(one_list)
	count_per_item = []
	for i in item:
		count_per_item.append(one_list.count(i))
	sorted_tuple = sorted(zip(count_per_item, item), reverse=True)
	if sorted_tuple[0][0] != sorted_tuple[1][0]:
		item_of_majority = sorted_tuple[0][1]
	elif sorted_tuple[1][0] != sorted_tuple[2][0]:
		item_of_majority = (sorted_tuple[0][1], sorted_tuple[1][1])
	else:
		item_of_majority = '>2 values'
	return item_of_majority

#Organize data
Categories = ['Persons#', 'AvgAge', 'Childless%', 'Non-smoker%', 'AvgBMI', 'TopRegion']
All = [len(list_of_age), round(list_item_avg(list_of_age)), list_item_percentage(list_of_children, '0'),
	 list_item_percentage(list_of_smoker, 'no'), round(list_item_avg(list_of_bmi), 1), majority_item(list_of_region)]
Female = [len(list_of_age_f), round(list_item_avg(list_of_age_f)), list_item_percentage(list_of_children_f, '0'), 
	list_item_percentage(list_of_smoker_f, 'no'), round(list_item_avg(list_of_bmi_f), 1), majority_item(list_of_region_f)]
Male = [len(list_of_age_m), round(list_item_avg(list_of_age_m)), list_item_percentage(list_of_children_m, '0'), 
	list_item_percentage(list_of_smoker_m, 'no'), round(list_item_avg(list_of_bmi_m), 1), majority_item(list_of_region_m)]

#Describe data
print('\n1.')
print('Category:', Categories)
print('All:', All)
print('Female:', Female)
print('Male:', Male)

#Additional relevant info
print('\nAverage cost: $' + str(list_item_avg(list_of_charges)))
print('% of female participants: ' + list_item_percentage(list_of_sex, 'female'))

#General average cost comparison as a baseline reference.
print('\n2.')
print('Average cost for a female: $' + str(list_item_avg(list_of_charges_f)))
print('Average cost for a male: $' + str(list_item_avg(list_of_charges_m)))
print('Female vs. Male: ' + calc_diff_percent(list_item_avg(list_of_charges_f),
	list_item_avg(list_of_charges_m)))

#Average cost comparison for non-smokers (assuming smoking has a big impact on cost)
print('\n3.')
print('Average cost for a non-smoking female: $' + str(list_item_avg(list_of_charges_f_ns)))
print('Average cost for a non-smoking male: $' + str(list_item_avg(list_of_charges_m_ns)))
print('Female vs. Male: ' + calc_diff_percent(list_item_avg(list_of_charges_f_ns),
	list_item_avg(list_of_charges_m_ns)))

#Average cost comparison for non-smokers with children (assuming having children is big differenciator between male and female)
print('\nAverage cost for a non-smoking female with children: $' + str(list_item_avg(list_of_charges_f_ns_c)))
print('Average cost for a non-smoking male with children: $' + str(list_item_avg(list_of_charges_m_ns_c)))
print('Female vs. Male: ' + calc_diff_percent(list_item_avg(list_of_charges_f_ns_c),
	list_item_avg(list_of_charges_m_ns_c)))

#Cost percentage change comparison for when the children condition is added.
print('\nPercentage change in cost for non-smokers when the children element is added:')
print('Female: ' + calc_diff_percent(list_item_avg(list_of_charges_f_ns_c), list_item_avg(list_of_charges_f_ns)))
print('Male: ' + calc_diff_percent(list_item_avg(list_of_charges_m_ns_c), list_item_avg(list_of_charges_m_ns)))

#Average age comparison for non-smokers with children
print('\nAverage age for a non-smoking female with children:', round(list_item_avg(list_of_age_f_ns_c)))
print('Average age for a non-smoking male with children:', round(list_item_avg(list_of_age_m_ns_c)))