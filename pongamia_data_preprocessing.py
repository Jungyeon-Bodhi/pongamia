#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 09:07:52 2024

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please download following Python Libraries:
1. Pandas
2. Numpy
3. uuid
4. openpyxl
"""

import pandas as pd
import numpy as np
import uuid
from openpyxl import load_workbook

class Preprocessing:
    
    def __init__(self, name, file_path, file_path_others, list_del_cols, dates, miss_col, anon_col, anon_col2, identifiers, opened_cols, cols_new, regions
                 ,locations, age_col = None, diss_cols = None, del_type = 0, file_type='xlsx'):
        """
        - Initialise the Performance Management Framework class

        name: str, Name of the project
        file_path: str, Directory of the raw dataset
        file_path_others: str, Directory of the opened-end questions' answers
        list_del_cols: list, Columns list for deleting
        dates: list, Dates on which the pilot test was conducted from the data
        miss_col: list, 
        anon_col: str, Column for anonymisation (Respondent Name)
        anon_col2: str, Column for anonymisation (Enumerator Name)
        identifiers: list, Columns for checking duplicates 
        opened_cols: list, Opened-end question columns
        cols_new: list, New names for the columns (for data analysis purpose)
        age_col: str, Column of age infromation (for age-grouping purpose)
        diss_cols: list, Column of WG-SS questions in the dataset (for disability-grouping purpose)
        del_type: int, [0 or 1]
        -> 0: Remove all missing values from the columns where missing values are detected
        -> 1: First, remove columns where missing values make up 10% or more of the total data points
              Then, remove all remaining missing values from the columns where they are detected
        file_type: str, filetype of the raw dataset
        """
        self.name = name
        self.file_path = file_path
        self.file_path_others = file_path_others
        self.file_type = file_type
        self.list_del_cols = list_del_cols
        self.dates = dates
        self.miss_col = miss_col
        self.anon_col = anon_col
        self.anon_col2 = anon_col2
        self.identifiers = identifiers
        self.opened_cols = opened_cols
        self.cols_new = cols_new
        self.regions = regions
        self.locations = locations
        self.age_col = age_col
        self.diss_cols = diss_cols
        self.del_type = del_type
        self.df = None
    
    def data_load(self):
        """
        - To load a dataset
        """
        file_path = self.file_path
        file_type = self.file_type
        if file_type == 'xlsx' or file_type == 'xls':
            df = pd.read_excel(f"{file_path}.{file_type}")
            self.df = df
            return True
        elif file_type == 'csv':
            df = pd.read_csv(f"{file_path}.{file_type}")
            self.df = df
            return True
        else:
            print("Please use 'xlsx', 'xls' or 'csv' file")
            return False
        
    def delete_columns(self):
        """
        - To drop unnecessary columns
        """
        df = self.df
        list_cols = self.list_del_cols
        df = df.drop(columns = list_cols)
        print(f'Number of columns: {len(df.columns)} | After removing the columns that are not needed for the analysis')
        self.df = df
        return True

    def date_filter(self):
        """
        - To remove dates on which the pilot test was conducted from the dataset
        """
        df = self.df 
        dates = self.dates
        for date in dates:
            df = df[df['today'] != date]
        self.df = df
        return True
        
    def missing_value_clean(self):
        """
        - To detect and remove missing values
        """
        miss_col = self.miss_col
        df = self.df
        del_type = self.del_type
        initial_data_points = len(df)
        num_missing_cols = {}
        print("")
        for col in miss_col:
            missing_count = df[col].isnull().sum()
            num_missing_cols[col] = missing_count
            print(f'Column {col} has {missing_count} missing values')
    
        if del_type == 0: # Remove all missing values from the columns where missing values are detected
            df_cleaned = df.dropna(subset=miss_col)

        # First, remove columns where missing values make up 10% or more of the total data points
        # Then, remove all remaining missing values from the columns where they are detected
        elif del_type == 1:
            threshold = 0.1 * initial_data_points
            cols_to_drop = [col for col, missing_count in num_missing_cols.items() if missing_count > threshold]
            df_cleaned = df.drop(columns=cols_to_drop)
            print("")
            print(f'Number of columns: {len(df.columns)} | After removing the columns that contained missing values more than 10% of data points')
            print(f'Dropped columns = {cols_to_drop}')
            df_cleaned = df_cleaned.dropna(subset=miss_col)
        
        remaind_data_points = len(df_cleaned)
        print("")
        print(f'Number of deleted missing values: {initial_data_points - remaind_data_points}')
        print(f"Number of data points after missing value handling: {remaind_data_points}")
        print("")
        self.df = df_cleaned
        return True
    
    def save_data(self):
        """
        - To save the new dataframe
        """
        df = self.df
        file_path = self.file_path
        file_type = self.file_type
        if file_type == 'xlsx' or file_type == 'xls':
            df.reset_index(drop=True, inplace = True)
            df.to_excel(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        elif file_type == 'csv':
            df.reset_index(drop=True, inplace = True)
            df.to_csv(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        else: 
            print("Please use 'xlsx', 'xls' or 'csv' file")
            return False
        if file_type == 'xlsx':
            df.reset_index(drop=True, inplace = True)
            df.to_excel(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        elif file_type == 'csv':
            df.reset_index(drop=True, inplace = True)
            df.to_csv(f"{file_path}.{file_type}", index=False)
            self.df = df
            print("The revised dataset has been saved")
            return True
        else: 
            print("Please use 'xlsx' or 'csv' file")
            return False
        
    def data_anonymisation(self):
        """
        - To implement a dataframe anonymisation
        """
        df = self.df
        col = self.anon_col
        col2 = self.anon_col2
        file_path = self.file_path
    
        def generate_unique_strings(prefix, series):
            unique_values = series.unique()
            key_mapping = {value: f"{prefix}{uuid.uuid4()}" for value in unique_values}
            return series.map(key_mapping), key_mapping
        
        df[col], respondent_mapping = generate_unique_strings('respondent_', df[col])
        df[col2], respondent_mapping = generate_unique_strings('enumerator_', df[col2])
        original = self.file_path
        self.file_path = f'{file_path}_anonymised'
        self.save_data()
        self.file_path = original
        self.df = df
        print("The respondent name has been anonymised")
        return True
    
    def duplicates(self):
        """
        - To detect and remove duplicates
        """
        df = self.df
        col = self.identifiers
        duplicates = df[df.duplicated(subset=col, keep=False)]
        print("")
        print(f"Number of duplicate based on '{col}': {len(duplicates)}")

        if not duplicates.empty:
            print("Duplicate rows:")
            print(duplicates)
    
        df_cleaned = df.drop_duplicates(subset=col, keep='first')
    
        print(f"Number of data points: {len(df_cleaned)} | After removing duplicates")
        print("")
        self.df = df_cleaned
        return True

    def open_ended_cols(self):
        """
        - To save opened-ended columns and remove these from the dataset
        """
        df = self.df
        cols = self.opened_cols
        file_path = self.file_path_others
        empty_df = pd.DataFrame()
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            empty_df.to_excel(writer, sheet_name='basic', index=False)
        
            max_length = 0
            unique_data = {}

            for col in cols:
                unique_values = df[col].dropna().unique()
                unique_data[col] = unique_values
                max_length = max(max_length, len(unique_values))
        
            combined_df = pd.DataFrame({col: pd.Series(unique_data[col]) for col in cols})
            combined_df.to_excel(writer, sheet_name='open_ended', index=False)
        
        print(f"Open-ended columns have been saved to '{file_path}': {cols} ")
        df = df.drop(columns=cols)
        print(f'Number of columns: {len(df.columns)} | After removing the open-ended columns')
        self.df = df
        return True

    def columns_redefine(self):
        """
        - To change column names for smoother data analysis
        """
        df = self.df
        new_cols = self.cols_new
        file_path = f'{self.file_path}_columns_book.xlsx'
        original_cols = list(df.columns)
        df.columns = new_cols
    
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            empty_df = pd.DataFrame()
            empty_df.to_excel(writer, sheet_name='basic', index=False)

            columns_df = pd.DataFrame({'Column Names': new_cols,'Original Names': original_cols})
        
            columns_df.to_excel(writer, sheet_name='Column_Info', index=False)

            workbook = writer.book
            worksheet = workbook['Column_Info']
        
            for col in worksheet.columns:
                max_length = max(len(str(cell.value)) for cell in col)
                adjusted_width = max(max_length, 12)
                worksheet.column_dimensions[col[0].column_letter].width = adjusted_width

        print(f"Column information has been saved: {file_path}")
        self.df = df
        return True

    def age_group(self):
        """
        - To create new age group variable
        """
        df = self.df
        col = self.age_col
        bins = [17, 24, 34, 44, 54, 64, float('inf')]
        labels = ['18 - 24','25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Above 65 years']
        df[col] = df[col].astype(int)
        df['Age Group'] = pd.cut(df[col], bins=bins, labels=labels, right=True)
        print('New age group variable (Age Group) has been created in this dataset')
        self.df = df
        return True
    
    def disability_wgss(self):
        """
        - To create disability group (based on the WG-SS)
        """
        df = self.df
        cols = self.diss_cols
        try:
            df['WG-Disability'] = ''
            
            def wg_ss(row, cols):
                values = row[cols]
                some_difficulty_count = (values == 'Some difficulty').sum()
                a_lot_of_difficulty = (values == 'A lot of difficulty').any() or (values == 'Cannot do at all').any()
                cannot_do_at_all = (values == 'Cannot do at all').any()
                if cannot_do_at_all:
                    return 'DISABILITY4'
                elif a_lot_of_difficulty:
                    return 'DISABILITY3'
                elif some_difficulty_count >= 2:
                    return 'DISABILITY2'
                elif some_difficulty_count >= 1:
                    return 'DISABILITY1'
                else:
                    return 'No_disability'
            df['WG-Disability'] = df.apply(lambda row: wg_ss(row, cols), axis=1)
            df['Disability'] = df['WG-Disability'].apply(lambda x: 'Disability' if x in ['DISABILITY4', 'DISABILITY3'] else 'No Disability')
            print('New disability variable (Disability) has been created in this dataset (Based on WG-SS)')
            self.df = df
            return True
        except Exception as e:
               print('New disability variable has not been created in this dataset')
               
    def poverty(self):
        df = self.df
        def assign_poverty_status(row):
            if row['4'] == 'Sudan':
                threshold = round(2.15 * 30 * 601.5 * row['8'], 0)
            elif row['4'] == 'South Sudan':
                threshold = round(2.15 * 30 * 130.26 * row['8'], 0)
            else:
                return np.nan
        
            return 'Poverty' if row['10'] < threshold else 'Not poverty'

        df['National poverty'] = df.apply(assign_poverty_status, axis=1)
        self.df = df
        
    def decent_work(self):
        df = self.df
        df['decent_work'] = np.where((df['90'] == 'Yes') | (df['98'] == 'Yes'), 'Yes', 'No')
        self.df = df

    def sri_index(self):
        df = self.df
        condition1a = [
            (df['26'] == 'No shelter'),
            (df['26'] == 'Makeshift shelter (shack, kiosk, vehicle)/Shelter not fit for safe habitation'),
            (df['26'] == 'Temporarily hosted by friends, family, community/faith group, or emergency shelter'),
            (df['26'] == 'Traditional hut, inadequate'),
            (df['26'] == 'Traditional hut, adequate')]
        
        condition1b = [
            (df['28'] == '2-3 times'),
            (df['28'] == '1 time'),
            (df['28'] == 'None'),
            (df['28'] == 'Not applicable')]
        
        condition2 = [
            (df['29'] == 'Household did not eat yesterday'),
            (df['29'] == 'Household was able to eat, but not even a full meal'),
            (df['29'] == 'Household was able to eat 1 full meal'),
            (df['29'] == 'Household was able to eat 2-3 full meals')]
        
        condition3 = [
            (df['30'] == 'No school-aged children in household'),
            (df['30'] == 'None are in school'),
            (df['30'] == 'Some are in school'),
            (df['30'] == 'All are in school')]
        
        condition4 = [
            (df['31'] == 'Have not needed health care in last 3 months'),
            (df['31'] == 'Did not receive the needed health care'),
            (df['31'] == 'Received some of the needed health care'),
            (df['31'] == 'Received all of the needed health care')]
        
        condition5 = [
            (df['32'] == 'Adult(s) in household has health condition that interferes with adult employment'),
            (df['32'] == 'Dependent(s) in household has health condition that interferes with adult employment'),
            (df['32'] == 'None of the above')]
        
        condition7 = [
            (df['35'] == 'No employment'),
            (df['35'] == 'Temporary, irregular, seasonal'),
            (df['35'] == 'Regular part-time (including self-employment)'),
            (df['35'] == 'Full-time (including self-employment), without necessary legal documentation'),
            (df['35'] == 'Full-time (including self-employment), with legal documentation'),]
        
        condition8 = [
            (df['36-7'] == 1) & (df[['36-1', '36-2', '36-3', '36-4', '36-5', '36-6']].sum(axis=1) == 0),  # 35-7 is 1, and all other columns are 0
            (df['36-6'] == 1) & (df[['36-1', '36-2', '36-3', '36-4', '36-5', '36-7']].sum(axis=1) == 0),  # 35-6 is 1, and all other columns are 0
            (df['36-6'] == 1) & ((df[['36-1', '36-2', '36-3', '36-4', '36-5', '36-7']].sum(axis=1) > 0)),  # 35-6 is 1, and any other column is 1
            (df['36-7'] == 0) & (df['36-6'] == 0)]
        
        condition11 = [
            (df['39'] == 'No, no savings or saleable assets'),
            (df['39'] == 'Yes, but not enough to cover one month’s expenses (basic needs)'),
            (df['39'] == 'Yes, enough to cover one month’s expenses (basic needs)'),
            (df['39'] == 'Yes, enough to cover one month’s expenses (basic needs) plus enough to purchase an asset, or reinvest into one’s business, or to sustain a moderate health crisis')]

        condition12a = [
            (df['40'] == 'Knows no one who could lend money'),
            (df['40'] == 'Knows someone/ has community support that could lend money')]
        
        condition12b = [
            (df['41'] == 'Neither'),
            (df['41'] == 'Household members ask others for advice/information ONLY'),
            (df['41'] == 'People ask household members for advice/information ONLY)'),
            (df['41'] == 'Both of them')]
        
        values1a = [1, 2, 3, 4, 5]
        values1b = [1, 3, 5, 0]
        values2 = [1, 2, 3, 5]
        values3 = [0, 1, 3, 5]
        values4 = [0, 1, 3, 5]
        values5 = [1, 3, 5]
        values7 = [1, 2, 3, 4, 5]
        values8 = [3, 5, 3, 1]
        values11 = [1, 3, 4, 5]
        values12a = [1, 5]
        values12b = [1, 3, 3, 5]
        df['sri_1a'] = np.select(condition1a, values1a, default=np.nan)
        df['sri_1b'] = np.select(condition1b, values1b, default=np.nan)
        df['sri_2'] = np.select(condition2, values2, default=np.nan)
        df['sri_3'] = np.select(condition3, values3, default=np.nan)
        df['sri_4'] = np.select(condition4, values4, default=np.nan)
        df['sri_5'] = np.select(condition5, values5, default=np.nan)
        df['sri_6'] = np.where(df['33-9'] == 1, 5, np.where(df['34'] == 'Yes', 1, 3))
        df['sri_7'] = np.select(condition7, values7, default=np.nan)
        df['sri_8'] = np.select(condition8, values8, default=np.nan)
        df['sri_9'] = df[['37-2', '37-3', '37-4', '37-5', '37-6']].eq(1).sum(axis=1)
        df['sri_9'] = df['sri_9'].map({3: 1, 4: 1, 5: 1, 2: 2, 1: 3})
        df['sri_9'] = np.where(df['36-1'] == 1, 5, df['sri_9'])
        df['sri_10'] = df[['38-2', '38-3', '38-4', '38-5', '38-6', '38-7']].eq(1).sum(axis=1)
        df['sri_10'] = df['sri_10'].map({5: 1, 4: 1, 3: 2, 2: 2, 1: 3})
        df['sri_10'] = np.where(df['38-1'] == 1, 5, df['sri_10'])
        df['sri_11'] =np.select(condition11, values11, default=np.nan)
        df['sri_12a'] =np.select(condition12a, values12a, default=np.nan)
        df['sri_12b'] =np.select(condition12b, values12b, default=np.nan)
        df['sri_12'] = df[['sri_12a', 'sri_12b']].mean(axis=1)
        
        columns_to_fill = ['sri_1a', 'sri_1b', 'sri_2','sri_3', 'sri_4', 'sri_5', 'sri_6', 'sri_9', 
                   'sri_7', 'sri_8', 'sri_10', 'sri_11', 'sri_12']

        df[columns_to_fill] = df[columns_to_fill].fillna(0)

        df['sri'] = np.where(
    df['sri_1b'] == 0, 
    (df['sri_1a'] + df['sri_3'] + df['sri_4'] + df['sri_6'] + df['sri_7'] + df['sri_8'] + df['sri_10'] + df['sri_11'] + df['sri_12']) / 9 - (5 - df['sri_2']) * 0.15 - (3 - df['sri_5']) * 0.05 - (5 - df['sri_9']) * 0.2, 
    (df['sri_1a'] + df['sri_1b'] + df['sri_3'] + df['sri_4'] + df['sri_6'] + df['sri_7'] + df['sri_8'] + df['sri_10'] + df['sri_11'] + df['sri_12']) / 10 - (5 - df['sri_2']) * 0.15 - (3 - df['sri_5']) * 0.05 - (5 - df['sri_9']) * 0.2)
        df['sri'] = df['sri'].apply(lambda x: 1 if x < 1 else (5 if x > 5 else x))
        self.df = df

    def output121(self):
        df = self.df
        
        source_conditions = ['Handpump or borehole', 'Protected shallow well', 'Protected dug well', 'Tube well', 'Tap stand']
        df['dry_access_source'] = np.where(df['43'].isin(source_conditions), 1, 0)
        df['rainy_access_source'] = np.where(df['55'].isin(source_conditions), 1, 0)
    
        df['dry_access_time'] = round((df['51'] * 2 + df['52']) / 30, 2)
        df['rainy_access_time'] = round((df['63'] * 2 + df['64']) / 30, 2)
        
        df['dry_availability'] = np.where(df['44'] == 'Yes', 1, round(df['45'] / 7, 2))
        df['rainy_availability'] = np.where(df['56'] == 'Yes', 1, round(df['57'] / 7, 2))
        
        df['dry_status'] = np.where(df['47'] == 'Yes', 1, np.nan)
        df['rainy_status'] = np.where(df['59'] == 'Yes', 1, np.nan)
        
        status_mapping = {
            'Minor repair': 0.67,
            'Major repair': 0.33,
            'It is beyond repair': 0}
        
        df['dry_status'] = df['dry_status'].fillna(df['48'].map(status_mapping))
        df['rainy_status'] = df['dry_status'].fillna(df['60'].map(status_mapping))
        
        df['dry_animal'] = np.where(df['50'] == 'Yes', 0, 1)
        df['rainy_animal'] = np.where(df['62'] == 'Yes', 0, 1)
  
        df['dry_fencing'] = np.where(df['49'] == 'Yes', 1, 0)
        df['rainy_fencing'] = np.where(df['61'] == 'Yes', 1, 0)

        quality_mapping = {
            'Very Poor': 0,
            'Poor': 0.25,
            'Average': 0.5,
            'Good': 0.75,
            'Excellent': 1}
        df['dry_quality'] = df['53'].map(quality_mapping)
        df['rainy_quality'] = df['65'].map(quality_mapping)
        
        df['dry_access'] = df.apply(lambda row: 'Yes' if row['dry_access_source'] == 1 and row['dry_access_time'] <= 1 else 'No', axis=1)
        df['rainy_access'] = df.apply(lambda row: 'Yes' if row['rainy_access_source'] == 1 and row['rainy_access_time'] <= 1 else 'No', axis=1)

        def calculate_dry_score(row):
            if row['dry_access'] == 'No':
                return np.nan
            else:
                cols_to_avg = ['dry_access_time', 'dry_availability', 'dry_status', 'dry_animal', 'dry_fencing', 'dry_quality']
                return row[cols_to_avg].mean()
            
        def calculate_rainy_score(row):
            if row['rainy_access'] == 'No':
                return np.nan
            else:
                cols_to_avg = ['rainy_access_time', 'rainy_availability', 'rainy_status', 'rainy_animal', 'rainy_fencing', 'rainy_quality']
                return row[cols_to_avg].mean()
        
        df['dry_score'] = df.apply(calculate_dry_score, axis=1)
        df['rainy_score'] = df.apply(calculate_rainy_score, axis=1)
        
        df['output_121'] = df.apply(lambda row: 'Improved' if row['dry_access'] =='Yes' and row['rainy_access'] =='Yes' else 'Not improved', axis=1)
        df['output_121_score'] = np.where((df['dry_score'] != np.nan) & (df['rainy_score'] != np.nan),round((df['dry_score'] + df['rainy_score']) / 2),'No access')
        self.df = df

    def output122(self):
        df = self.df
        conditions = ['Home latrine', 'Shared latrine', 'Communal latrine']
        df['latrine_usage'] = np.where(df['73'].isin(conditions), 1, 0)
        df['handwashing'] = np.where(df['78'] == 'Yes', 1, 0)
        df['ownership'] = np.where(df['latrine_usage'] == 0,0,np.where(df['73'] == 'Home latrine', 1,
        np.where(df['73'] == 'Shared latrine', 0.67,np.where(df['73'] == 'Communal latrine', 0.33, None))))
        df['sanitation_accessibility'] = np.where(df['latrine_usage'] == 0,0,np.where(df['75'] == 'Yes', 1, 0))
        df['sanitation_features'] = np.where(df['latrine_usage'] == 0,0, round(df[['74-1', '74-2', '74-3', '74-4']].sum(axis=1) / 4,2))
        df['sanitation_safety'] = np.where(df['latrine_usage'] == 0,0,
        (df[['79', '80', '81']].applymap(lambda x: 1 if x == 'Yes' else 0).sum(axis=1) +df['82'].map({'Agree': 1,'Neither agree nor disagree': 0.5,'Disagree': 0,'I do not use latrines': 0})) / 4)
        df['sanitation_clean'] = np.where(df['latrine_usage'] == 0,0,np.where(df['76'].isin(['No', 'I do not use latrines']),0,
                                                                              df['77'].map({'Daily': 1,'Weekly': 0.67}).fillna(0.33)))  
        df['output_122'] = df.apply(lambda row: 'Improved' if row['latrine_usage'] + row['handwashing'] == 2 else 'Not improved', axis=1)  
        df['output_122_score'] = np.where(df['output_122'] == 'No','No access',
                                          df[['ownership', 'sanitation_accessibility', 'sanitation_features', 'sanitation_safety', 'sanitation_clean']].mean(axis=1))
        
        self.df = df
  
    def output213(self):
        df = self.df
        
        for i in range(1, 15):
            agri_col = f'agri-{i}'
            value_col = f'105-{i}'
            df[agri_col] = np.where(df[value_col] == 1, 2, np.nan) 

        for i in range(1, 15):
            agri_col = f'agri-{i}'
            value_col_99 = f'105-I-{i}'

            df[agri_col] = np.where(
                df[agri_col].notna(),
                np.where(df[value_col_99] == 'Yes', 1, 
                         np.where(df[value_col_99] == 'No', 2, df[agri_col])), np.nan)
            
        df['agri_avg'] = df[[f'agri-{i}' for i in range(1, 15)]].mean(axis=1, skipna=True)
        df['agri_increased'] = np.where(df['agri_avg'] < 2, 'Increased', 'Not increased')
        df['agri_diversified'] = np.where((df['106'] == 'Yes, and I still produce the existing crops') & (df['107'] >= 1),'Diversified','Not diversified')
        
        df['output_213'] = np.where((df['agri_increased'] == 'Increased') | (df['agri_diversified'] == 'Diversified'),'Increased/Diversified','No changes')

    def output214(self):
        df = self.df
        df['output_214'] = np.where(
        (df['4'] == 'South Sudan') & ((df[['111', '112']].mean(axis=1)) > 45875), 'Increased', 
        np.where((df['4'] == 'Sudan') & ((df[['111', '112']].mean(axis=1)) > 40000), 'Increased', 'Not increased'))
        self.df = df
        
    def output215(self):
        df = self.df
        df['output_215'] = np.where((df['output_122'] == 'Improved') | (df['output_121'] == 'Improved'),'Increased','Not increased')
        self.df = df
        
    def region_location(self):
        """
        - Merge the regions and locations information into separate columns
        """
        df = self.df
        df['state'] = df[self.regions].bfill(axis=1).iloc[:, 0]
        df['locality'] = df[self.locations].bfill(axis=1).iloc[:, 0]
        df.drop(columns=self.regions + self.locations, inplace=True)
        self.df = df
        return True
    
    def unify(self):
        df = self.df
        for col in ['110','117','138','141']:
            df[col].replace('Average', 'Moderate', inplace=True)
        for col in ['130', '132', '134']:            
            df[col].replace(' No', 'No', inplace=True)
            df[col].replace(' Unsure', 'Unsure', inplace=True)
            
        df['survey_type'] = np.where(df['0'] == 'Yes', 'Livelihoods', 'WASH')
        self.df = df
        

    def processing(self):
        """
        - To conduct data pre-processing
        1. Load the raw dataset
        2. Re-define variable names
        3. Handle duplicates
        4. Anonymise data (Respondents' names)
        5. Remove pilot test data points
        6. Drop unnecessary columns
        7. Handle missing values
        8. Extract answers from open-ended questions
        9. Create age and disability groups
        10. Save the cleaned dataset
        """
        self.data_load()
        self.columns_redefine()
        print(f'Initial data points: {len(self.df)}')
        self.duplicates()
        self.data_anonymisation()
        if len(self.dates) != 0:
            self.date_filter()
        print(f'Initial number of columns: {len(self.df.columns)}')
        self.delete_columns()
        self.missing_value_clean()
        self.open_ended_cols()
        self.unify()
        self.region_location()
        self.poverty()
        self.decent_work()
        self.sri_index()      
        self.output121()
        self.output122()
        self.output213()
        self.output214()     
        self.output215()     
        if self.age_col != None:
            self.age_group()
        if self.diss_cols != None:
            self.disability_wgss()
        original = self.file_path
        self.file_path = f'{self.file_path}_cleaned'
        self.save_data()
        self.file_path = original
        print("")
        print(f'Final number of data points: {len(self.df)}')
        print(f"Cleaned dataframe has been saved: {self.file_path}_cleaned.{self.file_type}")
        return True