#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:18:51 2024

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please define the parameters for data preprocessing pipeline
"""
import pongamia_data_preprocessing as dp

project_name = "NEF: Final Evaluation of the ASRD project"

file_type = 'xlsx' 
# Original data format: xlsx, xls, csv

file_path = "Data/24-NEF-GLO-1 - Raw_data"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/24-NEF-GLO-1 - Open-End.xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

respondent_name = 'Respondent Name'
enumerators = 'Enumerator'
# Original column names for respondents' and enumerators' names (for anonymisation and duplicate removal)

identifiers = [respondent_name, 'end', 'Enumerator', '_uuid','130','131','132']
# Identifiers for detecting duplicates (list, do not remove respondent_name)
# Recommendation: At least three identifiers

dates = ['2024-11-18','2024-11-21','2024-11-23','2024-11-24','2024-11-22'] 
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['start','end','today','deviceid','Enumerator',
 '0', 'Respondent Name', '2','3', '4', '5-1', '5-2', '5-3', '6-1', '6-2', '6-3', '7', '8',
 '9a', '9-1', '9-2', '9-3', '9-4', '9-5', '9-6','9-7', '9-8', '9-9', '9-10', "10",
 '11', '12', '13', '14', '15',
 '16a','16-1','16-2', '16-3', '16-4', '16-5', '16-6', '16-7', '16-8',
 '17', '18', '19a', '19-1','19-2','19-3', '19-4','19-5','19-6','19-7','19-8',
 '20','21','22','23','24', '25', '26', '27', '28', '29', '30', '31', '32', '33a', '33-1', '33-2', '33-3', '33-4',
 '33-5', '33-6', '33-7', '33-8', '33-9', '34', '35', '36a', '36-1', '36-2', '36-3', '36-4', '36-5',
 '36-6', '36-7','37a', '37-1', '37-2', '37-3', '37-4', '37-5', '37-6', '37-7',
 '38a', '38-1', '38-2', '38-3', '38-4', '38-5', '38-6', '38-7', '38-8', '39', '40', '41',
 '42', '43', '44', '45', '46a', '46-1', '46-2', '46-3', '46-4', '47', '48', '49', '50', '51', '52', '53',
 '54a', '54-1', '54-2', '54-3', '54-4', '54-5', '55', '56', '57', '58a',
 '58-1', '58-2', '58-3', '58-4', '59','60', '61','62', '63', '64', '65', '66a', '66-1', '66-2', '66-3',
 '66-4', '66-5', '67', '68', '69', '70', '71', '72',
 '73','74a','74-d1','74-d2','74-d3','74-d4','74-d5', '74-1', '74-2','74-3', '74-4', '74-5',
 '75', '76', '77', '78', '79', '80', '81', '82', "83a", "83-1", "83-2",
 "83-3","83-4", "83-5", "83-6",'84', '85', '86', '87', "88", "89", '90', '91', '92',
 '93', '94', '95', '96', '97', '98', '99a', '99-1', '99-2','99-3', '99-4', '99-5',
 '100', '101', '102', '103', "104",'105a', '105-1', '105-2', '105-3','105-4', '105-5', '105-6',
 '105-7', '105-8', '105-9', '105-10', '105-11', '105-12', '105-13', '105-14', '105-15', "105-I-1",
 "105-I-2", "105-I-3", "105-I-4", "105-I-5", "105-I-6", "105-I-7", "105-I-8", "105-I-9", "105-I-10", "105-I-11",
 "105-I-12", "105-I-13", "105-I-14", '106', '107', '108a', '108-1', '108-2', '108-3', '108-4', '108-5', '108-6',
 '108-7', '108-8', '108-9', '108-10', '108-11','108-12', '108-13', '108-14', '108-15',
 '109', '110', "111", "112", '113', '114a', '114-1', '114-2', '114-3', '114-4', '114-5','114-6', '114-7',
 '115a', '115-1', '115-2', '115-3', '115-4','115-5', '115-6', '115-7', '116', '117', "118", '119',
 '120', '121', '122-1', '122-2', '122-3', '122-4', '122-5', '122-6', '122-7', '122-8', '123-1',
 '123-2', '123-3', '123-4', '123-5', '124', '125', '126', '127', '128', '129', 'DD', '130', '131', '132', '133',
 '134', '135', '136', '137', '138', '139', '140', '141', '142',
 'start-geopoint', '_start-geopoint_latitude', '_start-geopoint_longitude', '_start-geopoint_altitude', '_start-geopoint_precision',
 '19-old', "83-old", '_107-old', '_107-old2', '_107-old3', '_107-old4', '_107-old5', '_107-old6', '_107-old7', '_107-old8', '_108-old',
 '_108-old2', '_108-old3', '_108-old4', '_108-old5', '_108-old6', '_108-old7', '_108-old8', '_115-old', '_116-old',
 '_128-old', '_id', '_uuid', '_submission_time', '_validation_status', '_notes', '_status', '_submitted_by', '__version__', '_tags', '_index']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = ['start','end','deviceid','Enumerator','9a','16a','19a','33a','36a','37a', '46a', '54a', '58a', '66a', '74a','74-d1','74-d2','74-d3',
 '74-d4', '74-d5', "83a", '99a', '105a', '108a', '114a', '115a', 'DD', 'start-geopoint',
 '_start-geopoint_latitude', '_start-geopoint_longitude', '_start-geopoint_altitude', '_start-geopoint_precision',
 '19-old', "83-old", '_107-old', '_107-old2', '_107-old3', '_107-old4', '_107-old5', '_107-old6',
 '_107-old7', '_107-old8', '_108-old', '_108-old2', '_108-old3', '_108-old4', '_108-old5', '_108-old6', '_108-old7',
 '_108-old8', '_115-old', '_116-old', '_128-old', '_id', '_uuid', '_submission_time', '_validation_status', '_notes',
 '_status', '_submitted_by', '__version__', '_tags', '_index']
# Specify the columns to be excluded from the data analysis

miss_col = ['139', '141','0']
# Specify all columns that apply to all respondents for missing value detection

open_cols = ['140','142']
# Specify the open-ended columns (which will be saved in a separate Excel sheet and removed from the data frame)

age_col = None
# If we don't have age group in this dataset, please specify the age columns (as str)

diss_cols = ['20', '21', '22', '23', '24', '25']
# If we have WG-SS questions in the dataset, please specify the columns (as list [])

states = ['5-1', '6-1']

locations = ['5-2', '5-3', '6-2', '6-3']


"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

pongamia = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, respondent_name, enumerators, identifiers, open_cols, cols_new, states, locations, age_col, diss_cols, del_type = 0, file_type=file_type)
pongamia.processing()