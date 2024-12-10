#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 9 16:22:04 2024

@author: Bodhi Global Analysis
"""

import pandas as pd
import matplotlib.pyplot as plt

bodhi_blue = (0.0745, 0.220, 0.396)
bodhi_grey = (0.247, 0.29, 0.322)
bodhi_primary_1 = (0.239, 0.38, 0.553)
bodhi_secondary = (0.133, 0.098, 0.42)
bodhi_tertiary = (0.047, 0.396, 0.298)
bodhi_complement = (0.604, 0.396, 0.071)
color_palette = [bodhi_primary_1, bodhi_complement, bodhi_tertiary, bodhi_blue, bodhi_grey, bodhi_secondary]

def bar_chart(data, title, fontsize, output_file, type_v = None):
    df = pd.DataFrame(data)
    plt.figure(figsize=(24, 10))
    ax = df.set_index('State').plot(kind='bar', stacked=False, color=color_palette, width=0.65)

    for container in ax.containers:
        for bar in container:
            height = bar.get_height()
            if type_v == 'percent':
                ax.text(bar.get_x() + bar.get_width() / 2.0, bar.get_y() + height, 
                    f'{(height*100):.1f}%', ha='center', va='bottom', fontsize=fontsize-3, color='black')
            elif type_v == 'number':
                ax.text(bar.get_x() + bar.get_width() / 2.0, bar.get_y() + height, 
                    f'{height:.2f}', ha='center', va='bottom', fontsize=fontsize-2.3, color='black')                


    ax.set_xticks(range(len(df)))
    ax.set_xticklabels(df['State'], rotation=0, ha='center', fontsize=fontsize-1)
    ax.tick_params(axis='y', labelsize=7)
    if type_v == 'percent': 
        ax.set_ylim(0, 1.1)
    else: ax.set_ylim(0, 4)
    plt.title(title, fontsize=fontsize)
    plt.xlabel(' ')
    plt.ylabel(' ', fontsize=fontsize -2)
    plt.legend(prop={'size': fontsize-3})
    plt.savefig(output_file, bbox_inches='tight', dpi=600)
    
def bar_chart2(data, title, fontsize, output_file, type_v = None):
    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df['item'], df['Value'], color=color_palette, width=0.7)
    for bar in bars:
        height = bar.get_height()
        if height > 0:  # Only label non-zero bars
            if type_v == 'percent':
                plt.text(
                    bar.get_x() + bar.get_width() / 2.0,
                    bar.get_y() + height,
                    f'{(height * 100):.1f}%',
                    ha='center',
                    va='bottom',
                    fontsize=fontsize - 3,
                    color='black'
                )
            elif type_v == 'number':
                plt.text(
                    bar.get_x() + bar.get_width() / 2.0,
                    bar.get_y() + height,
                    f'{height:.2f}',
                    ha='center',
                    va='bottom',
                    fontsize=fontsize - 2.3,
                    color='black'
                )

    # Set x-tick labels
    plt.xticks(range(len(df)), df['item'], rotation=0, ha='center', fontsize=fontsize - 1)
    plt.yticks(fontsize=7)

    # Adjust y-axis limits
    if type_v == 'percent':
        plt.ylim(0, 1.1)
    else:
        plt.ylim(0, 4)

    # Add chart title and labels
    plt.title(title, fontsize=fontsize)
    plt.xlabel(' ')
    plt.ylabel(' ', fontsize=fontsize - 2)

    # Save the chart to a file
    plt.savefig(output_file, bbox_inches='tight', dpi=600)

# Visualisation
data = {
    "State": ["Female","Male", "Host\nCommunity", "Long-term\nIDPs", "Short-term\nIDPs", "Refugees", 'Returnees', 'Disability'],
    "Baseline" : [0.998, 0.996, 0.998, 0.994, 0.995, 0.998, 1.00, 1.00], # Please adjust these valuses manually
    "Endline" : [0.548, 0.524, 0.474, 0.625, 0.963, 0.455, 0.684, 0.815]}  # Please adjust these valuses manually

bar_chart(data, title = 'Impact 1.1: % of the displacement-affected persons living below the national poverty line', fontsize = 7, output_file = 'visuals/IM1-1.png', type_v = 'percent')

data2 = {
    "State": ["Female","Male", "Host\nCommunity", "Long-term\nIDPs", "Short-term\nIDPs", "Refugees", 'Returnees', 'Disability'],
    "Baseline" : [3.36, 3.41, 3.40, 3.49, 3.44, 3.12, 3.47, 2.86], # Please adjust these valuses manually
    "Endline" : [2.28, 2.24, 2.32, 2.12, 2.18, 2.36, 2.10, 1.91]}  # Please adjust these valuses manually

bar_chart(data2, title = 'Impact 1.2: % of beneficiaries with improved self-reliance', fontsize = 7, output_file = 'visuals/IM1-2.png', type_v = 'number')

data3 = {
    "State": ["Output 1.2.1","Output 1.2.2"],
    "Baseline" : [0.208, 0.083], # Please adjust these valuses manually
    "Endline" : [0.125, 0.174]}  # Please adjust these valuses manually

bar_chart(data3, title = 'Output 1.2: Displacement-affected beneficiaries have improved WASH practices and\naccess to upgraded WASH facilities and light infrastructure', fontsize = 7, output_file = 'visuals/output1.2.png', type_v = 'percent')

data4 = {
    "item": ["After defecation/\nusing toilet","Before eating", "After\nchanging diapers", "Before\npreparing food", "Before\nfeeding an infant"],
    "Value" : [0.620, 0.844, 0.504, 0.761, 0.435]}  # Please adjust these valuses manually

bar_chart2(data4, title = 'Critical times to wash their hands', fontsize = 12, output_file = 'visuals/wash_critical.png', type_v = 'percent')