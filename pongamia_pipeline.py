#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:52:03 2024

@author: ijeong-yeon
"""

import pongamia_indicator as bd
import pongamia_PMF as pmf
import pandas as pd

"""
Evaluation
"""
# Specify the file path for the clean dataset
df = pd.read_excel('data/24-NEF-GLO-1 - Data_cleaned.xlsx')

# Create indicators and provide additional details as needed (Evaluation)
def create_indicators(df):
    indicators = []
    # social demographics
    
    s_country = bd.Indicator(df, "country", None, ['4'], i_cal=None, i_type='count', description='Country', period='endline', target = None)
    indicators.append(s_country)
    
    s_type = bd.Indicator(df, "Survey Type", None, ['survey_type'], i_cal=None, i_type='percentage', description="Survey Type: Livelihoods and WASH", period='endline', target = None)
    s_type.add_breakdown({'4':'Country'})
    s_type.add_var_order(['Livelihoods', "WASH"])
    indicators.append(s_type)
    
    chl = bd.Indicator(df, "any challenges", None, ['139'], i_cal=None, i_type='percentage', description="Did you encounter any challenges while participating in the project?", period='endline', target = None)
    chl.add_breakdown({'4':'Country'})
    chl.add_var_order(['Yes', "No"])
    indicators.append(chl)
    
    os_p = bd.Indicator(df, "overall satisfaction", None, ['141'], i_cal=None, i_type='percentage', description="To what extent are you satisfied with the ASRD project?", period='endline', target = None)
    os_p.add_breakdown({'4':'Country'})
    os_p.add_var_order(['Very low', "Low", "Moderate","High","Very high"])
    indicators.append(os_p)
    
    return indicators


def create_indicators_wash(df):
    indicators = []
    # WASH indicators
    
    s_country = bd.Indicator(df, "country", None, ['4'], i_cal=None, i_type='count', description='Country', period='endline', target = None)
    indicators.append(s_country)

    improve = bd.Indicator(df, "WASH rehabilitated", None, ['42'], i_cal=None, i_type='count', description='WASH Rehabilitated?', period='endline', target = None)
    improve.add_breakdown({'4':'Country'})
    indicators.append(improve)

    output121 = bd.Indicator(df, "output121", 121, ['output_121'], i_cal=None, i_type='percentage', description='Number of displacement-affected persons who report gained or improved access to safe drinking integrated water services', period='endline', target = None)
    output121.add_baseline(20.8)
    output121.add_breakdown({'4':'Country'})
    output121.add_var_order(['Not improved', 'Improved'])
    indicators.append(output121)
    
    output122 = bd.Indicator(df, "output122", 122, ['output_122'], i_cal=None, i_type='percentage', description='Number of displacement-affected persons who report gained or improved access to integrated safe sanitation facilities', period='endline', target = None)
    output122.add_baseline(8.3)
    output122.add_breakdown({'4':'Country'})
    output122.add_var_order(['Not improved', 'Improved'])
    indicators.append(output122)
    
    output215 = bd.Indicator(df, "output215", 215, ['output_215'], i_cal=None, i_type='percentage', description='Number of displacement affected persons who report increased capacity to meet basic needs', period='endline', target = None)
    output215.add_baseline(24.5)
    output215.add_breakdown({'4':'Country'})
    output215.add_var_order(['Not increased', 'Increased'])
    indicators.append(output215)
    
    important_wash = bd.Indicator(df, "Washing important", None, ["83-1", "83-2", "83-3","83-4", "83-5", "83-6"], i_cal=None, i_type='percentage', description="Can you please tell me the five critical times when it is most important to wash one's hand?", period='endline', target = None)
    important_wash.add_breakdown({'4':'Country'})
    important_wash.add_var_change({1: "Yes", 0: "No"})
    important_wash.add_label(['After defecation/using the toilet', 'Before eating', "After changing diapers or cleaning a child's bottom", "Before preparing food", "Before feeding an infant", "No mentions of any of the five options above"])
    indicators.append(important_wash)
    
    child_suffer = bd.Indicator(df, "child_diarrhoea", None, ['84'], i_cal=None, i_type='percentage', description="Is there a child of age under 5 years old in your household?", period='endline', target = None)
    child_suffer.add_breakdown({'4':'Country'})
    child_suffer.add_var_order(['Yes', "No", "I do not know/refuse to answer"])
    indicators.append(child_suffer)
    
    child_suffer2 = bd.Indicator(df, "child_diarrhoea2", None, ['85'], i_cal=None, i_type='percentage', description="Has this child suffered from diarrhoea in the past 2 weeks (14 days)?", period='endline', target = None)
    child_suffer2.add_breakdown({'4':'Country'})
    child_suffer2.add_var_order(['Yes', "No", "I do not know/refuse to answer"])
    indicators.append(child_suffer2)
    
    information_sani = bd.Indicator(df, "information_sanitation", None, ['86'], i_cal=None, i_type='percentage', description="Have you received any information about hygiene or sanitation in the past 12 months?", period='endline', target = None)
    information_sani.add_breakdown({'4':'Country'})
    information_sani.add_var_order(['Yes', "No", "I do not know/refuse to answer"])
    indicators.append(information_sani)
    
    information_sani2 = bd.Indicator(df, "information_sanitation2", None, ['87'], i_cal=None, i_type='percentage', description="What was the information about?", period='endline', target = None)
    information_sani2.add_breakdown({'4':'Country'})
    information_sani2.add_var_order(['Waterborne illnesses', "Water safety practices", "Hygiene or sanitation practices", "Other", "I do not know/refuse to answer"])
    indicators.append(information_sani2)
    
    satisfaction_sanitation = bd.Indicator(df, "satisfaction sanitation", None, ['88'], i_cal=None, i_type='percentage', description="How satisfied are you with the project's implementation and delivery of water supply, sanitation and hygiene promotion?", period='endline', target = None)
    satisfaction_sanitation.add_breakdown({'4':'Country'})
    satisfaction_sanitation.add_var_order(['Satisfied', "Neither agree nor disagree", "Not Satisfied", "I do not know/refuse to answer"])
    indicators.append(satisfaction_sanitation)
    
    return indicators

def create_indicators_livelihood(df):
    indicators = []
    # Livelihoods indicators
    s_age = bd.Indicator(df, "age", None, ['2'], i_cal=None, i_type='count', description='Age Group', period='endline', target = None)
    s_age.add_breakdown({'3':'Gender', '4':'Country', 'state':'State', '7':'Residency status', 'Disability':'Disability'})
    indicators.append(s_age)
    
    s_sex = bd.Indicator(df, "sex", None, ['3'], i_cal=None, i_type='count', description='Gender', period='endline', target = None)
    s_sex.add_breakdown({'2':'Age group', '4':'Country', 'state':'State', '7':'Residency status', 'Disability':'Disability'})
    indicators.append(s_sex)
    
    s_country = bd.Indicator(df, "country", None, ['4'], i_cal=None, i_type='count', description='Country', period='endline', target = None)
    s_country.add_breakdown({'3':'Gender', '2':'Age group', 'state':'State', '7':'Residency status', 'Disability':'Disability'})
    indicators.append(s_country)
    
    s_residency = bd.Indicator(df, "residency status", None, ['7'], i_cal=None, i_type='count', description='Residency Status', period='endline', target = None)
    s_residency.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State', 'Disability':'Disability'})
    indicators.append(s_residency)
    
    s_disability = bd.Indicator(df, "disability", None, ['Disability'], i_cal=None, i_type='count', description='Residency Status', period='endline', target = None)
    s_disability.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State', '7':'Residency status'})
    indicators.append(s_disability)
    
    s_state = bd.Indicator(df, "states", None, ['state'], i_cal=None, i_type='count', description='States', period='endline', target = None)
    s_state.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', '7':'Residency status', 'Disability':'Disability'})
    indicators.append(s_state)
    
    feel_decent_work = bd.Indicator(df, "perceived decentwork", None, ['decent_work'], i_cal=None, i_type='percentage', description="Do you feel that you have access to decent work?", period='endline', target = None)
    feel_decent_work.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State','7':'Residency status', 'Disability':'Disability'})
    feel_decent_work.add_var_order(['Yes', "No", "Unsure"])
    indicators.append(feel_decent_work)
    
    agri_yes = bd.Indicator(df, "agriculture work", None, ['102'], i_cal=None, i_type='percentage', description="In the last year, was your household engaged in any types of agricultural production, processing, or pastoralism?", period='endline', target = None)
    agri_yes.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State','7':'Residency status', 'Disability':'Disability'})
    agri_yes.add_var_order(['Yes', "No"])
    indicators.append(agri_yes)
    
    agri1 = bd.Indicator(df, "which agri", None, ['105-1', '105-2', '105-3', '105-4', '105-5', '105-6', '105-7', '105-8', '105-9', '105-10','105-11', '105-12', '105-13', '105-14', '105-15'], i_cal=None, i_type='count', description='In the last year, which of the following types of agricultural production/processing/pastoralism does your household engage in?', period='endline', target = None)
    agri1.add_var_change({1: "Yes", 0: "No"})
    agri1.add_var_order([1, 0])
    agri1.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State','7':'Residency status', 'Disability':'Disability'})
    agri1.add_label(["Onion", "Okra", "Tomato", "Cucumber", "Eggplant", "Watermelon", "Cereals", "Livestock"
                     , "Potato", "Cowpea", "Hibiscus", "Groundnuts", "Sesame", "Gum arabic (NTFP)", "Other"])
    indicators.append(agri1)
 
    basic_need = bd.Indicator(df, "perceived need", None, ['116'], i_cal=None, i_type='percentage', description="Do you think your capacity to meet basic needs has been enhanced?", period='endline', target = None)
    basic_need.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State','7':'Residency status', 'Disability':'Disability'})
    basic_need.add_var_order(['Yes', "No", "Unsure"])
    indicators.append(basic_need)
    
    basic_need2 = bd.Indicator(df, "perceived need2", None, ['117'], i_cal=None, i_type='percentage', description="To what extent has your capacity to meet basic needs enhanced?", period='endline', target = None)
    basic_need2.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State','7':'Residency status', 'Disability':'Disability'})
    basic_need2.add_var_order(['Very low', "Low", "Moderate","High","Very high"])
    indicators.append(basic_need2)
    
    food_s1 = bd.Indicator(df, "food security1", None, ['118'], i_cal=None, i_type='percentage', description="How would you describe your household's food intake yesterday?", period='endline', target = None)
    food_s1.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State','7':'Residency status', 'Disability':'Disability'})
    food_s1.add_var_order(['Household did not eat yesterday', "Household was able to eat, but did not eat a full meal", "Household was able to eat 1 full meal","Household was able to eat 2-3 full meals"])
    indicators.append(food_s1)
    
    food_s2 = bd.Indicator(df, "food security2", None, ['119'], i_cal=None, i_type='percentage', description="Was the food intake yesterday typical of your daily food intake?", period='endline', target = None)
    food_s2.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State','7':'Residency status', 'Disability':'Disability'})
    food_s2.add_var_order(['No, we normally have less to eat than yesterday', "No, we normally have more to eat than yesterday", "Yes, this was a typical amount of daily food intake"])
    indicators.append(food_s2)
    
    food_s1_n = bd.Indicator(df, "food security1n", None, ['120'], i_cal=None, i_type='percentage', description="Looking at your neighbour or friend who did not take part in the project, how would you describe your neighbour’s food intake yesterday? ", period='endline', target = None)
    food_s1_n.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State','7':'Residency status', 'Disability':'Disability'})
    food_s1_n.add_var_order(['Household did not eat yesterday', "Household was able to eat, but did not eat a full meal", "Household was able to eat 1 full meal","Household was able to eat 2-3 full meals"])
    indicators.append(food_s1_n)
    
    food_s2_n = bd.Indicator(df, "food security2n", None, ['121'], i_cal=None, i_type='percentage', description="Would you say that your neighbour’s food intake yesterday, mentioned above, is typical of their daily food intake? ", period='endline', target = None)
    food_s2_n.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State','7':'Residency status', 'Disability':'Disability'})
    food_s2_n.add_var_order(['No, they normally have less to eat than yesterday', "No, they normally have more to eat than yesterday", "Yes, this was a typical amount of daily food intake"])
    indicators.append(food_s2_n)
    
    food_s5 = bd.Indicator(df, "food security5", None, ['137'], i_cal=None, i_type='percentage', description="To what extent is your food security different from that of your neighbour who did not participate in the ASRD project?", period='endline', target = None)
    food_s5.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State','7':'Residency status', 'Disability':'Disability'})
    food_s5.add_var_order(['Worse', "Slightly worse", "About the same","Slightly better","Better"])
    indicators.append(food_s5)
    
    food_s6 = bd.Indicator(df, "food security6", None, ['136'], i_cal=None, i_type='percentage', description="Do you think food security has improved due to the ASRD project?", period='endline', target = None)
    food_s6.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State','7':'Residency status', 'Disability':'Disability'})
    food_s6.add_var_order(['Yes', "No", "Unsure"])
    indicators.append(food_s6)
    
    food_s7 = bd.Indicator(df, "food security7", None, ['138'], i_cal=None, i_type='percentage', description="To what extent has food security to meet basic needs improved?", period='endline', target = None)
    food_s7.add_breakdown({'3':'Gender', '2':'Age group', '4':'Country', 'state':'State','7':'Residency status', 'Disability':'Disability'})
    food_s7.add_var_order(['Very low', "Low", "Moderate","High","Very high"])
    indicators.append(food_s7)
    return indicators

# Extract the SRI scores by each category
def sri_extraction(df, cols, output_file='data/sri_output.xlsx'):
    with pd.ExcelWriter(output_file, engine='openpyxl', mode='w') as writer:
        for col in cols:
            grouped_df = df.groupby(col)['sri'].mean().reset_index()
            grouped_df.to_excel(writer, sheet_name=col, index=False)       
    return grouped_df
    

df_wash = df[df['0'] == 'No']
df_livelihood = df[df['0'] == 'Yes']
# Create the PMF class ('Project Title', 'Evaluation')
# Add the indicators to the PMF class
pongamia_wash = pmf.PerformanceManagementFramework('WASH', 'Evaluation')
indicators_wash = create_indicators_wash(df_wash)
pongamia_wash.add_indicators(indicators_wash)

file_path1 = 'data/24-NEF-GLO-1 - WASH Statistics.xlsx' # File path to save the statistics (including breakdown data)
folder = 'visuals/wash/' # File path for saving visuals
pongamia_wash.PMF_generation(file_path1, folder) # Run the PMF

sri_extraction(df_livelihood, ['3', '2', '4', 'state', '7', 'Disability'])
pongamia_livelihood = pmf.PerformanceManagementFramework('Livelihood', 'Evaluation')
indicators_livelihood = create_indicators_livelihood(df_livelihood)
pongamia_livelihood.add_indicators(indicators_livelihood)

file_path1 = 'data/24-NEF-GLO-1 - Livelihood Statistics.xlsx'
folder = 'visuals/livelihoods/'
pongamia_livelihood.PMF_generation(file_path1, folder)

pongamia = pmf.PerformanceManagementFramework('Overall', 'Evaluation')
indicators = create_indicators(df)
pongamia.add_indicators(indicators)

file_path1 = 'data/24-NEF-GLO-1 - Statistics.xlsx'
folder = 'visuals/'
pongamia.PMF_generation(file_path1, folder)
