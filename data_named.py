import pandas as pd
import numpy as np

data = pd.read_csv('data_num.csv', delimiter=",")
data = data.drop(['StartDate', 'EndDate', 'Status', 'IPAddress', 'Progress', 'Finished', 'RecordedDate', 'ResponseId', 'RecipientLastName'], axis=1)
data = data.drop(['RecipientFirstName', 'RecipientEmail', 'ExternalReference', 'LocationLatitude', 'LocationLongitude', 'DistributionChannel'], axis=1)
data = data.drop(['Q3_5_TEXT', 'Q4_6_TEXT', 'Q25_Last Click', 'Q25_Page Submit', 'Q25_Click Count', 'Q25_First Click', 'Q21'], axis=1)
data = data.rename(columns={'Q1':'participant_number', 'Q2':'age', 'Q3':'gender', 'Q4':'ethnicity', 'Q5':'political_orientation', 'Q5_4_TEXT':'political_orientation_text', 'Q6':'achieved_education', 'Q6_8_TEXT':'achieved_education_text', 'Q23_1':'bothered_pre', 'Q23_2':'uneasy_pre', 'Q23_3':'uncomfortable_pre', 'Q27':'C_time_alone', 'Q25':'C_academic_performance', 'Q8':'T_time_alone', 'Q24':'T_academic_performance', 'Q9':'value_activation', 'Q13_1':'bothered_post', 'Q13_2':'uneasy_post', 'Q13_3':'uncomfortable_post', 'Q17':'sandwich', 'Q18':'diet', 'Q18_7_TEXT':'diet_text', 'Q19':'reason_for_choice', 'Q20':'labels_attention', 'Q22':'feeling_observed', 'Q21.1':'did_value_activation_affect_choice' })
data = data.drop([2,7,11,23,32,0,13,16,30,31,33,3,10,15], axis=0)

data['value_activation'] = data['value_activation'].fillna('control')
data['uneasy_pre'] = data['uneasy_pre'].fillna(int(0))
data['bothered_pre'] = data['bothered_pre'].fillna(int(0))
data['uncomfortable_pre'] = data['uncomfortable_pre'].fillna(int(0))
data['uneasy_post'] = data['uneasy_post'].fillna(int(0))
data['bothered_post'] = data['bothered_post'].fillna(int(0))
data['uncomfortable_post'] = data['uncomfortable_post'].fillna(int(0))
data['C_academic_performance'] = data['C_academic_performance'].fillna('test')
data['C_time_alone'] = data['C_time_alone'].fillna('test')
data['T_academic_performance'] = data['T_academic_performance'].fillna('control')
data['T_time_alone'] = data['T_time_alone'].fillna('control')
data['did_value_activation_affect_choice'] = data['did_value_activation_affect_choice'].fillna('empty')

labels = data.keys()
variable_values = {}
for label in labels:
    variable_values[label] = {}
variable_values['gender'][1] = 'male'
variable_values['gender'][2] = 'female'
variable_values['gender'][3] = 'non-binary/third gender'
variable_values['gender'][4] = 'prefer not to say'
variable_values['gender'][5] = 'other'
variable_values['ethnicity'][1] = 'white/caucasian'
variable_values['ethnicity'][2] = 'hispanic/latino'
variable_values['ethnicity'][3] = 'asian'
variable_values['ethnicity'][4] = 'african/carribbean'
variable_values['ethnicity'][5] = 'middle-eastern'
variable_values['ethnicity'][6] = 'other'
variable_values['political_orientation'][1] = 'left-leaning'
variable_values['political_orientation'][2] = 'centrist'
variable_values['political_orientation'][3] = 'right-leaning'
variable_values['political_orientation'][4] = 'other'
variable_values['achieved_education'][1] = 'Mandatory school'
variable_values['achieved_education'][2] = 'High-school'
variable_values['achieved_education'][3] = 'Bachelor'
variable_values['achieved_education'][4] = 'Master'
variable_values['achieved_education'][5] = 'PhD'
variable_values['achieved_education'][6] = 'Apprenticeship'
variable_values['achieved_education'][7] = 'Federal maturity'
variable_values['achieved_education'][8] = 'other'
variable_values['value_activation'][1] = 'Yes'
variable_values['value_activation'][2] = 'No'
variable_values['value_activation']['control'] = 'control group, did not see the question'
variable_values['Duration (in seconds)'] = 'total time of the experiment in seconds'
variable_values['UserLanguage']['FR'] = 'French'
variable_values['UserLanguage']['EN'] = 'English'
variable_values['participant_number'] = 'control if <= 70, test if else'
variable_values['age'] = 'age in years'
variable_values['political_orientation_text'] = 'text answer to /political_orientation/'
variable_values['achieved_education_text'] = 'text answer to /achieved_education/'
variable_values['bothered_pre'] = 'from 0 to 100, 0: no not at all, 100: yes very'
variable_values['uneasy_pre'] = 'from 0 to 100, 0: no not at all, 100: yes very'
variable_values['uncomfortable_pre'] = 'from 0 to 100, 0: no not at all, 100: yes very'
variable_values['bothered_post'] = 'from 0 to 100, 0: no not at all, 100: yes very'
variable_values['uneasy_post'] = 'from 0 to 100, 0: no not at all, 100: yes very'
variable_values['uncomfortable_post'] = 'from 0 to 100, 0: no not at all, 100: yes very'
variable_values['C_academic_performance'][1] = 'Yes'
variable_values['C_academic_performance'][2] = 'No'
variable_values['C_academic_performance']['test'] = 'test group, did not see the question'
variable_values['C_time_alone'][1] = 'Yes'
variable_values['C_time_alone'][2] = 'No'
variable_values['C_time_alone']['test'] = 'test group, did not see the question'
variable_values['T_academic_performance'][1] = 'Yes'
variable_values['T_academic_performance'][2] = 'No'
variable_values['T_academic_performance']['control'] = 'control group, did not see the question'
variable_values['T_time_alone'][1] = 'Yes'
variable_values['T_time_alone'][2] = 'No'
variable_values['T_time_alone']['control'] = 'control group, did not see the question'
variable_values['sandwich'][1] = 'Pesto and Vegetables'
variable_values['sandwich'][2] = 'Hummus and Cucumber'
variable_values['sandwich'][3] = 'Ham and Cheese'
variable_values['sandwich'][4] = 'Cured Beef'
variable_values['sandwich'][5] = 'No sandwich taken'
variable_values['diet'][1] = 'Vegetarian'
variable_values['diet'][2] = 'Vegan'
variable_values['diet'][3] = 'Omnivorous'
variable_values['diet'][4] = 'Gluten-free'
variable_values['diet'][5] = 'Dairy-free'
variable_values['diet'][6] = 'Low-carb'
variable_values['diet'][7] = 'If other, please specify:'
variable_values['diet_text'] = 'Text answer to /diet/'
variable_values['reason_for_choice'] = 'Text answer'
variable_values['labels_attention'][1] = 'Yes'
variable_values['labels_attention'][2] = 'No'
variable_values['labels_attention'][3] = 'Which labels?'
variable_values['feeling_observed'][1] = 'Yes'
variable_values['feeling_observed'][2] = 'No'
variable_values['feeling_observed'][3] = "I don't know"
variable_values['did_value_activation_affect_choice'][1] = 'Yes'
variable_values['did_value_activation_affect_choice'][2] = 'No'
variable_values['did_value_activation_affect_choice']['empty'] = "Empty in the original csv"
