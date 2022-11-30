#IMPORTING LIBRARIES

import os
import json
import argparse
import csv
import pandas as pd
from bs4 import BeautifulSoup


#FUNCTION DEFINITIONS

def take_args():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-b', '--branch', help='Branch which you want to create DB', required=True)
        args = parser.parse_args()
    
        return args.branch
    
    except:
        print("Error in taking arguments")
        return None

def fetch_branch_data(branch):
    with open('branchdata.json') as f:
        data = json.load(f)
        StartRoll = data[branch]['range'][0]
        EndRoll = data[branch]['range'][1]
        rollnos_with_error = data[branch]['error']

    return StartRoll, EndRoll, rollnos_with_error

def generate_filenames(range_start, range_end, rollnos_with_error):
    
    try:

        filenames = []
        
        for i in range(range_start, range_end + 1):
            name = str(i)
            filenames.append(name)

        #if some roll numbers have some problem delete them from filenames list below
        for i in rollnos_with_error:    
            filenames.remove(str(i))
        else:
            pass
        return filenames
    
    except Exception as e:
        print("Error in generating filenames: ", e)
        return []

def parse_html(file):
    
    try:

        with open(f'{RESULTS_DIR}\\{file}.html', 'r', encoding = 'utf-8') as f:
            
            soup = BeautifulSoup(f, 'html.parser')
            print("Soup made for: ", file)
            
            #all the data is inside table format even metadata
            tables = soup.find('table', {'class': 'table-responsive'})
            if(len(tables) == 0):
                print(f"No data found for {file}")
            
            return tables
    except:
        print("Error in parsing html")
        return []
    
def extract_data(tables):
    
    try:

        #extracting data from tables and writing in txt file as string
        with open(f'{OUTPUT_DIR}\\{file}' + '.txt' , "w", encoding = "utf-8") as f:
            
            for x in tables.find_all('tr'):
                if len(x.text) > 0:
                    a = x.text.strip()
                    f.write(str(a))
    
    except:

        print("Error in extracting data")

def clean_data(file):
    
    try:
    
        newlines = []
        
        #opening txt files and loading data in list newlines for cleaning for blank lines and stripping extra spaces
        with open(f'{OUTPUT_DIR}\\{file}' + '.txt' , "r", encoding = "utf-8") as f:
            for line in f:
                if line.strip():
                    newlines.append(line)

        #overwriting txt files with cleaned data to use space efficiently
        with open(f'{OUTPUT_DIR}\\{file}' + '.txt', 'w', encoding='utf-8') as o:
            for line in newlines:
                o.write(line)

    except:
        print("Error in cleaning data")

def create_db():

    try:
        if branch != 'CSE':
            fields = [
                    'Name',
                    'RollNo',
                    'Gender',
                    'Branch',
                    'SGPA3',
                    'SGPA4',
                    'Status',
                    'KOE038i',
                    'KOE038e',
                    'KOE038g',
                    'KAS301i',
                    'KAS301e',
                    'KAS301g',
                    'KCS301i',
                    'KCS301e',
                    'KCS301g',
                    'KCS302i',
                    'KCS302e',
                    'KCS302g',
                    'KCS303i',
                    'KCS303e',
                    'KCS303g',
                    'KCS351i',
                    'KCS351e',
                    'KCS351g',
                    'KCS352i',
                    'KCS352e',
                    'KCS352g',
                    'KCS353i',
                    'KCS353e',
                    'KCS353g',
                    'KCS354i',
                    'KNC301i',
                    'KNC301e',
                    'KAS402i',
                    'KAS402e',
                    'KAS402g',
                    'KVE401i',
                    'KVE401e',
                    'KVE401g',
                    'KCS401i',
                    'KCS401e',
                    'KCS401g',
                    'KCS402i',
                    'KCS402e',
                    'KCS402g',
                    'KCS403i',
                    'KCS403e',
                    'KCS403g',
                    'KCS451i',
                    'KCS451e',
                    'KCS451g',
                    'KCS452i',
                    'KCS452e',
                    'KCS452g',
                    'KCS453i',
                    'KCS453e',
                    'KCS453g',
                    'KNC402i',
                    'KNC402e'
                    
                    ]
        else:
            fields = [
                    'Name',
                    'RollNo',
                    'Gender',
                    'Branch',
                    'SGPA3',
                    'SGPA4',
                    'Status',
                    'KAS302i',
                    'KAS302e',
                    'KAS302g',
                    'KVE301i',
                    'KVE301e',
                    'KVE301g',
                    'KCS301i',
                    'KCS301e',
                    'KCS301g',
                    'KCS302i',
                    'KCS302e',
                    'KCS302g',
                    'KCS303i',
                    'KCS303e',
                    'KCS303g',
                    'KCS351i',
                    'KCS351e',
                    'KCS351g',
                    'KCS352i',
                    'KCS352e',
                    'KCS352g',
                    'KCS353i',
                    'KCS353e',
                    'KCS353g',
                    'KCS354i',
                    'KNC302i',
                    'KNC302e',
                    'KOE049i',
                    'KOE049e',
                    'KOE049g',
                    'KAS401i',
                    'KAS401e',
                    'KAS401g',
                    'KCS401i',
                    'KCS401e',
                    'KCS401g',
                    'KCS402i',
                    'KCS402e',
                    'KCS402g',
                    'KCS403i',
                    'KCS403e',
                    'KCS403g',
                    'KCS451i',
                    'KCS451e',
                    'KCS451g',
                    'KCS452i',
                    'KCS452e',
                    'KCS452g',
                    'KCS453i',
                    'KCS453e',
                    'KCS453g',
                    'KNC401i',
                    'KNC401e',
                
                    ]


        with open(f'{DB_DIR}\\{DB_NAME}.csv', 'w', encoding='utf-8') as csvfile:
            csvwrter = csv.writer(csvfile)
            csvwrter.writerow(fields)

    except:
        print("Error in creating database")

def find_indices(item_to_find, where_to_find):
    
    try:
    
        indices = []
        for idx, value in enumerate(where_to_find):
            if value == item_to_find:
                indices.append(idx)
        return indices

    except:
        
        print("Error in finding indices")
        return []

def write_db(file):
    
        with open(f'{OUTPUT_DIR}\\{file}' + '.txt' , "r", encoding = "utf-8") as f:
            
            #cleaning lines for blank lines and stripping extra spaces
            lines = [line.rstrip() for line in f]
            

            #finding indices of 'sgpa' in lines
            sgpas_indices = find_indices('SGPA', lines)
            

            #defining fields for db
            Name = lines[19]
            RollNo = lines[lines.index('RollNo')  + 2]
            Gender = lines[lines.index('Gender')  + 2]
            Branch = lines[lines.index('Branch Code & Name')  + 2]
            SGPA3 = lines[sgpas_indices[-2] + 2][0:4]
            SGPA4 = lines[len(lines) - 1 - lines[::-1].index('SGPA') + 2][0:4]
            Status = lines[len(lines) - 1 - lines[::-1].index('Result Status') + 2]
            
            if branch != 'CSE':
                #extracting 3rd sem subjects
                
                KOE038i = lines[lines.index('KOE038')  + 3][0:2]
                KOE038e = lines[lines.index('KOE038')  + 3][2:4]
                KOE038g = lines[lines.index('KOE038')  + 3][6:]

                KAS301i = lines[lines.index('KAS301')  + 3][0:2]
                KAS301e = lines[lines.index('KAS301')  + 3][2:4]
                KAS301g = lines[lines.index('KAS301')  + 3][6:]

                KCS301i = lines[lines.index('KCS301')  + 3][0:2]
                KCS301e = lines[lines.index('KCS301')  + 3][2:4]
                KCS301g = lines[lines.index('KCS301')  + 3][6:]

                KCS302i = lines[lines.index('KCS302')  + 3][0:2]
                KCS302e = lines[lines.index('KCS302')  + 3][2:4]
                KCS302g = lines[lines.index('KCS302')  + 3][6:]

                KCS303i = lines[lines.index('KCS303')  + 3][0:2]
                KCS303e = lines[lines.index('KCS303')  + 3][2:4]
                KCS303g = lines[lines.index('KCS303')  + 3][6:]

                KCS351i = lines[lines.index('KCS351')  + 3][0:2]
                KCS351e = lines[lines.index('KCS351')  + 3][2:4]
                KCS351g = lines[lines.index('KCS351')  + 3][6:]

                KCS352i = lines[lines.index('KCS352')  + 3][0:2]
                KCS352e = lines[lines.index('KCS352')  + 3][2:4]
                KCS352g = lines[lines.index('KCS352')  + 3][6:]

                KCS353i = lines[lines.index('KCS353')  + 3][0:2]
                KCS353e = lines[lines.index('KCS353')  + 3][2:4]
                KCS353g = lines[lines.index('KCS353')  + 3][6:]

                KCS354i = lines[lines.index('KCS354')  + 3][0:2]

                KNC301i = lines[lines.index('KNC301')  + 3][0:2]
                KNC301e = lines[lines.index('KNC301')  + 3][2:4]


                #extracting 4th sem subjects

                KAS402i = lines[lines.index('KAS402')  + 3][0:2]
                KAS402e = lines[lines.index('KAS402')  + 3][2:4]
                KAS402g = lines[lines.index('KAS402')  + 3][6:]

                KVE401i = lines[lines.index('KVE401')  + 3][0:2]
                KVE401e = lines[lines.index('KVE401')  + 3][2:4]
                KVE401g = lines[lines.index('KVE401')  + 3][6:]                

                KCS401i = lines[lines.index('KCS401')  + 3][0:2]
                KCS401e = lines[lines.index('KCS401')  + 3][2:4]
                KCS401g = lines[lines.index('KCS401')  + 3][6:]

                KCS402i = lines[lines.index('KCS402')  + 3][0:2]
                KCS402e = lines[lines.index('KCS402')  + 3][2:4]
                KCS402g = lines[lines.index('KCS402')  + 3][6:]

                KCS403i = lines[lines.index('KCS403')  + 3][0:2]
                KCS403e = lines[lines.index('KCS403')  + 3][2:4]
                KCS403g = lines[lines.index('KCS403')  + 3][6:]

                KCS451i = lines[lines.index('KCS451')  + 3][0:2]
                KCS451e = lines[lines.index('KCS451')  + 3][2:4]
                KCS451g = lines[lines.index('KCS451')  + 3][6:]

                KCS452i = lines[lines.index('KCS452')  + 3][0:2]
                KCS452e = lines[lines.index('KCS452')  + 3][2:4]
                KCS452g = lines[lines.index('KCS452')  + 3][6:]

                KCS453i = lines[lines.index('KCS453')  + 3][0:2]
                KCS453e = lines[lines.index('KCS453')  + 3][2:4]
                KCS453g = lines[lines.index('KCS453')  + 3][6:]

                KNC402i = lines[lines.index('KNC402')  + 3][0:2]
                KNC402e = lines[lines.index('KNC402')  + 3][2:4]

                

                #inserting into db
                with open(f'{DB_DIR}\\{DB_NAME}.csv', 'a', newline='') as csvfile:
                    csvwrter = csv.writer(csvfile)
                    csvwrter.writerow([
                        
                        Name, RollNo, Gender, Branch, SGPA3, SGPA4, Status,

                        KOE038i,
                        KOE038e,
                        KOE038g,

                        KAS301i,
                        KAS301e,
                        KAS301g,

                        KCS301i,
                        KCS301e,
                        KCS301g,

                        KCS302i,
                        KCS302e,
                        KCS302g,

                        KCS303i,
                        KCS303e,
                        KCS303g,

                        KCS351i,
                        KCS351e,
                        KCS351g,

                        KCS352i,
                        KCS352e,
                        KCS352g,

                        KCS353i,
                        KCS353e,
                        KCS353g,

                        KCS354i,

                        KNC301i,
                        KNC301e,
                        

                        KAS402i,
                        KAS402e,
                        KAS402g,

                        KVE401i,
                        KVE401e,
                        KVE401g,

                        KCS401i,
                        KCS401e,
                        KCS401g,

                        KCS402i,
                        KCS402e,
                        KCS402g,

                        KCS403i,
                        KCS403e,
                        KCS403g,

                        KCS451i,
                        KCS451e,
                        KCS451g,

                        KCS452i,
                        KCS452e,
                        KCS452g,

                        KCS453i,
                        KCS453e,
                        KCS453g,

                        KNC402i,
                        KNC402e
                    ])

                print("Data Inserted")
            
            else:
                KAS302i = lines[lines.index('KAS302')  + 3][0:2]
                KAS302e = lines[lines.index('KAS302')  + 3][2:4]
                KAS302g = lines[lines.index('KAS302')  + 3][6:]

                KVE301i = lines[lines.index('KVE301')  + 3][0:2]
                KVE301e = lines[lines.index('KVE301')  + 3][2:4]
                KVE301g = lines[lines.index('KVE301')  + 3][6:]

                KCS301i = lines[lines.index('KCS301')  + 3][0:2]
                KCS301e = lines[lines.index('KCS301')  + 3][2:4]
                KCS301g = lines[lines.index('KCS301')  + 3][6:]

                KCS302i = lines[lines.index('KCS302')  + 3][0:2]
                KCS302e = lines[lines.index('KCS302')  + 3][2:4]
                KCS302g = lines[lines.index('KCS302')  + 3][6:]

                KCS303i = lines[lines.index('KCS303')  + 3][0:2]
                KCS303e = lines[lines.index('KCS303')  + 3][2:4]
                KCS303g = lines[lines.index('KCS303')  + 3][6:]

                KCS351i = lines[lines.index('KCS351')  + 3][0:2]
                KCS351e = lines[lines.index('KCS351')  + 3][2:4]
                KCS351g = lines[lines.index('KCS351')  + 3][6:]

                KCS352i = lines[lines.index('KCS352')  + 3][0:2]
                KCS352e = lines[lines.index('KCS352')  + 3][2:4]
                KCS352g = lines[lines.index('KCS352')  + 3][6:]

                KCS353i = lines[lines.index('KCS353')  + 3][0:2]
                KCS353e = lines[lines.index('KCS353')  + 3][2:4]
                KCS353g = lines[lines.index('KCS353')  + 3][6:]

                KCS354i = lines[lines.index('KCS354')  + 3][0:2]

                KNC302i = lines[lines.index('KNC302')  + 3][0:2]
                KNC302e = lines[lines.index('KNC302')  + 3][2:4]


                #extracting 4th sem subjects

                KOE049i = lines[lines.index('KOE049')  + 3][0:2]
                KOE049e = lines[lines.index('KOE049')  + 3][2:4]
                KOE049g = lines[lines.index('KOE049')  + 3][6:]

                KAS401i = lines[lines.index('KAS401')  + 3][0:2]
                KAS401e = lines[lines.index('KAS401')  + 3][2:4]
                KAS401g = lines[lines.index('KAS401')  + 3][6:]

                KCS401i = lines[lines.index('KCS401')  + 3][0:2]
                KCS401e = lines[lines.index('KCS401')  + 3][2:4]
                KCS401g = lines[lines.index('KCS401')  + 3][6:]

                KCS402i = lines[lines.index('KCS402')  + 3][0:2]
                KCS402e = lines[lines.index('KCS402')  + 3][2:4]
                KCS402g = lines[lines.index('KCS402')  + 3][6:]

                KCS403i = lines[lines.index('KCS403')  + 3][0:2]
                KCS403e = lines[lines.index('KCS403')  + 3][2:4]
                KCS403g = lines[lines.index('KCS403')  + 3][6:]

                KCS451i = lines[lines.index('KCS451')  + 3][0:2]
                KCS451e = lines[lines.index('KCS451')  + 3][2:4]
                KCS451g = lines[lines.index('KCS451')  + 3][6:]

                KCS452i = lines[lines.index('KCS452')  + 3][0:2]
                KCS452e = lines[lines.index('KCS452')  + 3][2:4]
                KCS452g = lines[lines.index('KCS452')  + 3][6:]

                KCS453i = lines[lines.index('KCS453')  + 3][0:2]
                KCS453e = lines[lines.index('KCS453')  + 3][2:4]
                KCS453g = lines[lines.index('KCS453')  + 3][6:]

                KNC401i = lines[lines.index('KNC401')  + 3][0:2]
                KNC401e = lines[lines.index('KNC401')  + 3][2:4]


                #inserting into db
                with open(f'{DB_DIR}\\{DB_NAME}.csv', 'a', newline='') as csvfile:
                    csvwrter = csv.writer(csvfile)
                    csvwrter.writerow([
                        
                        Name, RollNo, Gender, Branch, SGPA3, SGPA4, Status,

                        KAS302i,
                        KAS302e,
                        KAS302g,

                        KVE301i,
                        KVE301e,
                        KVE301g,

                        KCS301i,
                        KCS301e,
                        KCS301g,

                        KCS302i,
                        KCS302e,
                        KCS302g,

                        KCS303i,
                        KCS303e,
                        KCS303g,

                        KCS351i,
                        KCS351e,
                        KCS351g,

                        KCS352i,
                        KCS352e,
                        KCS352g,

                        KCS353i,
                        KCS353e,
                        KCS353g,

                        KCS354i,
                        
                        KNC302i,
                        KNC302e,

                        KOE049i,
                        KOE049e,
                        KOE049g,

                        KAS401i,
                        KAS401e,
                        KAS401g,

                        KCS401i,
                        KCS401e,
                        KCS401g,

                        KCS402i,
                        KCS402e,
                        KCS402g,

                        KCS403i,
                        KCS403e,
                        KCS403g,

                        KCS451i,
                        KCS451e,
                        KCS451g,

                        KCS452i,
                        KCS452e,
                        KCS452g,

                        KCS453i,
                        KCS453e,
                        KCS453g,

                        KNC401i,
                        KNC401e
                    ])

                print("Data Inserted")
    
def clean_sgpas():
    
    try:
    
        df = pd.read_csv(f'{DB_DIR}\\{DB_NAME}.csv')
        
        sgpa3 = df['SGPA3'].tolist()
        sgpa4 = df['SGPA4'].tolist()

        temp1 = []
        for i in sgpa3:
            x = ''.join(m for m in i if m.isdigit() or m == '.')
            temp1.append(x)
        
        temp2 = []
        for i in sgpa4:
            x = ''.join(m for m in i if m.isdigit() or m == '.')
            temp2.append(x)
        
        #replacing with new cleaned values

        df['SGPA3'] = temp1
        df['SGPA4'] = temp2

        df.to_csv(f'{DB_DIR}\\{DB_NAME}.csv', index=False)
        
    except:
        print("Error in cleaning SGPA")


#MAIN PROGRAM

if __name__ == '__main__':

    branch = take_args()

    cwd = os.path.dirname(__file__)

    #create clean output directory if it doesn't exist
    os.mkdir(os.path.dirname(__file__) + '/clean output')
    
    #USER CONFIGURATION
    #path to directory containing result html files
    RESULTS_DIR = (f'{cwd}\\Raw Results\\{branch}')

    #path to directory containing cleaned txt files
    OUTPUT_DIR = (f'{cwd}\\clean output')

    #path for database
    DB_DIR = (f'{cwd}\\DB')
    DB_NAME = branch

    
    #creating database
    StartRoll , EndRoll , rollnos_with_errors = fetch_branch_data(branch)
    
    filenames = generate_filenames(StartRoll, EndRoll, rollnos_with_errors)

    for file in filenames:
        
        tables = parse_html(file)

        extract_data(tables)

        clean_data(file)

    
    create_db()

    for file in filenames:
        print(f'Processing {file}')
        write_db(file)

    clean_sgpas()

    
    print("All Processes completed successfully")



