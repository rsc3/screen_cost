
# coding: utf-8

# In[1]:

# Imports
import pprint
from collections import OrderedDict
import datetime
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import csv
import os


# In[2]:


# # Creating Output Files to store data

# Creates empty data frames with column names for each task, and then write them to a unique csv file

# plate_filling = pd.DataFrame(data=None,columns=['ts','name','plates','media','tips','antibiotic','antibio_vol','antibio_conc','fill_time'])
# colony_picking = pd.DataFrame(data=None,columns=['ts','name','plates','lids','stickers','toothpicks','dishes','pick_time'])
# spread_plating = pd.DataFrame(data=None,columns=['ts','name','dishes','media','antibiotic','antibio_vol','antibio_conc','arabinose_vol','arabinose_conc','chloram_vol','chloram_conc','spread_time'])
# plate_replication = pd.DataFrame(data=None,columns=['ts','name','tips','plates','lids','stickers','plate_type','rep_time'])
# screening = pd.DataFrame(data=None,columns=['ts','name','target','target_vol','target_conc','plates','setup_time','read_time'])

# plate_filling.to_csv('plate_filling.csv')
# colony_picking.to_csv('colony_picking.csv')
# spread_plating.to_csv('spread_plating.csv')
# plate_replication.to_csv('plate_replication.csv')
# screening.to_csv('screeing.csv')


# In[3]:

# Defining Global Variables

# Creates dictionaries of variables to be called by list number (key) in functions

antibiotics = OrderedDict([("1", "Spectinomycin"), ('2', 'Chloramphenicol'), ('3', 'Kanamycin'), ('4','Tetracycline')])
plate_types = OrderedDict([('1', 'Clear'), ('2', 'Black')])
screening_targets = OrderedDict([('1', 'Lignin'), ('2', 'Lavender Oil'), ('3', 'Caffeine'), ('4', 'Isoprene'), ('5', 'Isoprenol'), 
                                 ('6', 'Limonene'), ('7', 'Vanilin'), ('8', 'P-coumaric Acid'), ('9', 'Vanilic Acid'), ('10', 'Camphor'), 
                                 ('11', 'Menthol'), ('12', 'Dipentene')])
staff = OrderedDict([('1',"Aneesha"),('2','Cameron'),('3','Giles'),('4','Nina'),('5','Will')])


# In[4]:

# TAKING USER INPUTS FOR FLOATS AND INTS
def inp(question):
    """This function takes a string question, prompts a user input in numeric format (float or int) and returns 
    the input in the form of a float"""
    dummy = False
    while dummy == False:
        try:
            user_input = float(input(question))
            dummy = True
        except: 
            print("You entered a bad input. Let's try again.")
    print('')
    return(user_input)


# In[5]:

# TAKING USER INPUTS FOR STRINGS
def inp_str(question):
    """This function takes a string question, prompts a user input  and returns 
    the input in the form of a string"""
    dummy = False
    while dummy == False:
        try:
            user_input = str(input(question))
            dummy = True
        except: 
            print("You entered a bad input. Let's try again.")
    print('')
    return(user_input)  


# In[6]:

def dict_select(dict,question,scold):
    """This function takes a dictionary, a question in the form of a string, and a message in the form of a string 
    to allert users of a bad input.  It returns a single value out of the dictionary."""
    for vals in dict:
        print(vals,dict[vals])
    dummy = False 
    while dummy == False:
        dict_key = inp_str(question)
        try:
            val = dict[dict_key]
            dummy = True
        except:
            print(scold)
            dummy = False
    print('')
    return(val)


# In[7]:

# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# import pandas as pd
# import csv

# # Creating Output Files to store data
# index = range(0,0)
# plate_filling = pd.DataFrame(data=None,columns=['ts','name','plates','media','tips','antibiotic','antibio_vol','antibio_conc','fill_time'],index=index)
# colony_picking = pd.DataFrame(data=None,columns=['ts','name','plates','lids','stickers','toothpicks','dishes','pick_time'],index=index)
# spread_plating = pd.DataFrame(data=None,columns=['ts','name','dishes','media','antibiotic','antibio_vol','antibio_conc','arabinose_vol','arabinose_conc','chloram_vol','chloram_conc','spread_time'],index=index)
# plate_replication = pd.DataFrame(data=None,columns=['ts','name','tips','plates','lids','stickers','plate_type','rep_time'],index=index)
# screening = pd.DataFrame(data=None,columns=['ts','name','target','target_vol','target_conc','plates','setup_time','read_time'],index=index)

# plate_filling.to_csv('plate_filling1.csv')
# colony_picking.to_csv('colony_picking1.csv')
# spread_plating.to_csv('spread_plating1.csv')
# plate_replication.to_csv('plate_replication1.csv')
# screening.to_csv('screeing1.csv')


# pf_file = pd.read_csv('spread_plating1.csv')

# pf_file.head()

# # frames = [results,ps_results_2]
# # results = pd.concat(frames)    
# ps_results = pd.DataFrame([[1.4,"Giles",3,3,7,4,5,4,5,5,5,4]],columns=['ts','name','dishes','media','antibiotic','antibio_vol','antibio_conc','arabinose_vol','arabinose_conc','chloram_vol','chloram_conc','spread_time'],index=[0,1])
# spread_plating.append(ps_results,ignore_index=True)
# spread_plating.head()
# ps_results_2 = pd.DataFrame([[1.4,"Giles",3,3,7,4,5,4,5,5,5,4]],columns=['ts','name','dishes','media','antibiotic','antibio_vol','antibio_conc','arabinose_vol','arabinose_conc','chloram_vol','chloram_conc','spread_time'],index=[0,1])


# new_reults_2 = pf_file.append(ps_results_2,ignore_index=True)

# new_reults_2.to_csv('spread_plating1.csv')

# spread_plating1.csv

# # writer = pd.ExcelWriter('output.xlsx')
# # data_frame.to_excel(writer,'Sheet1')
# # writer.save()


# In[8]:

# pf_file1 = pd.read_csv('plate_filling.csv',index_col=0)
# pf_file1.head()
# ps_results = pd.DataFrame([[1.4,"Giles",13,13,17,14,15,14,15,15,15,4]],columns=['ts','name','dishes','media','antibiotic','antibio_vol','antibio_conc','arabinose_vol','arabinose_conc','chloram_vol','chloram_conc','spread_time'])
# new_frame_3 = new_frame_2.append(ps_results,ignore_index=True)



# In[9]:

# new_frame_3


# In[10]:

# TASK: PLATE FILLING

def plate_filling():
    """This function takes nothing and returns a list of variables related to the task in the title. It's main function is to append that list of user inputted varaibles to 
    the appropriate csv file.  It calls upon the inp function."""
    plates = inp("PLATES! Please enter the number of PLATES you used: ")
    media = inp("MEDIA! Please enter the total ml of MEDIA you poured: ")
    tips = inp("TIPS! Please enter the number of BOXES of TIPS you used - fractions are OK: ")
    antibiotic = dict_select(antibiotics,"Which ANTIBIOTIC did you use? Please select the NUMBER associated with your ANTIBIOTIC above: ","Bad input. Please enter the LIST NUMBER associated with the ANTIOBIOTIC you used")
    antibio_vol = inp("ANTIBIOTICS! Please enter the VOLUME of ANTIBIOTICS used: ")
    antibio_conc = inp("ANTIBIOTICS! Please enter the CONCETNRATION of ANTIBIOTICS used: ")
    fill_time = inp("TIME! How long in MINUTES did it take you to FILL PLATES: ")
    ts = datetime.datetime.utcnow()
    
    pf_results = pd.DataFrame([[ts,name,plates,media,tips,antibiotic,antibio_vol,antibio_conc,fill_time]],columns=['ts','name','plates','media','tips','antibiotic','antibio_vol','antibio_conc','fill_time'])
    pf_doc = pd.read_csv('plate_filling.csv', index_col=0)
    new_results = pf_doc.append(pf_results,ignore_index=True)
    new_results.to_csv('plate_filling.csv')

    
    return([ts,name,plates,media,tips,antibiotic,antibio_vol,antibio_conc,fill_time])


# In[11]:

# TASK: COLONY PICKING

def colony_picking():
    """This function takes nothing and returns a list of variables related to the task in the title. It's main function is to append that list of user inputted varaibles to 
    the appropriate csv file.  It calls upon the inp function."""
    plates = inp("PLATES! Please enter the number of PLATES W/ MEDIA you used: ")
    lids = plates
    stickers = plates
    toothpicks = (plates*98*1.25)
    dishes = inp("DISHES! How many UNIQUE DISHES did you pick colonies out of: ")
    pick_time = inp("TIME! How long in MINUTES did it take you to PICK COLONIES: ")
    ts = datetime.datetime.utcnow()
    
    cp_results = pd.DataFrame([[ts,name,plates,lids,stickers,toothpicks,dishes,pick_time]],columns=['ts','name','plates','lids','stickers','toothpicks','dishes','pick_time'])
    cp_doc = pd.read_csv('colony_picking.csv', index_col=0)
    new_results = cp_doc.append(cp_results,ignore_index=True)
    new_results.to_csv('colony_picking.csv')
    
    return([ts,name,plates,lids,stickers,toothpicks,dishes,pick_time])


# In[12]:

# TASK: PLATE SPREADING

def plate_spreading():
    """This function takes nothing and returns a list of variables related to the task in the title. It's main function is to append that list of user inputted varaibles to 
    the appropriate csv file.  It calls upon the inp and dict_select functions."""
    dishes = inp("PETRI DISHES! Please enter the number of PETRI DISHES you used: ")
    media = inp("AGAR! Please enter the total ml of AGAR MEDIA you poured: ")
    antibiotic = dict_select(antibiotics,"Which ANTIBIOTIC did you use? Please select the NUMBER associated with your ANTIBIOTIC above: ","Bad input. Please enter the LIST NUMBER associated with the ANTIOBIOTIC you used")
    antibio_vol = inp("ANTIBIOTICS! Please enter the VOLUME of ANTIBIOTICS used: ")
    antibio_conc = inp("ANTIBIOTICS! Please enter the CONCETNRATION of ANTIBIOTICS used: ")
    arabinose_vol = inp("ARABINOSE! Please enter the VOLUME of ARABINOSE used: ")
    arabinose_conc = inp("ARABINOSE! Please enter the CONCETNRATION of ARABINOSE used: ")
    chloram_vol = inp("CHLORAM! Please enter the VOLUME of CHLORAM used: ")
    chloram_conc = inp("CHLORAM! Please enter the CONCETNRATION of CHLORAM used: ")
    spread_time = inp("TIME! How long in MINUTES did it take you to PLATE SPREAD: ")
    ts = datetime.datetime.utcnow()
    
    ps_results = pd.DataFrame([[ts,name,dishes,media,antibiotic,antibio_vol,antibio_conc,arabinose_vol,arabinose_conc,chloram_vol,chloram_conc,spread_time]],columns=['ts','name','dishes','media','antibiotic','antibio_vol','antibio_conc','arabinose_vol','arabinose_conc','chloram_vol','chloram_conc','spread_time'])
    ps_doc = pd.read_csv('plate_spreading.csv', index_col=0)
    new_results = ps_doc.append(ps_results,ignore_index=True)
    new_results.to_csv('plate_spreading.csv')
    
    
    
    return([ts,name,dishes,media,antibiotic,antibio_vol,antibio_conc,arabinose_vol,arabinose_conc,chloram_vol,chloram_conc,spread_time])


# In[13]:

# TASK: PLATE REPLICATION
def plate_replication():
    """This function takes nothing and returns a list of variables related to the task in the title. It's main function is to append that list of user inputted varaibles to 
    the appropriate csv file.  It calls upon the inp and dict_select functions."""
    tips = inp("TIPS! Please enter the number of BOXES of TIPS you used - fractions are OK: ")
    plates = inp("PLATES! Please enter the number of PLATES W/ MEDIA you used: ")
    lids = plates 
    stickers = plates
    plate_type = dict_select(plate_types, "PLATE TYPES! Which TYPE of PLATE did you use? Please select the NUMBER associated with list above: ", "Bad input. Please enter the LIST NUMBER associated with the PLATE TYPE you used")
    rep_time = inp("TIME! How long in MINUTES did it take you to REPLICATE PLATES: ")
    ts = datetime.datetime.utcnow()
    
    pr_results = pd.DataFrame([[ts,name,tips,plates,lids,stickers,plate_type,rep_time]],columns=['ts','name','tips','plates','lids','stickers','plate_type','rep_time'])
    pr_doc = pd.read_csv('plate_replication.csv', index_col=0)
    new_results = pr_doc.append(pr_results,ignore_index=True)
    new_results.to_csv('plate_replication.csv')
    
    return()


# In[14]:

# TASK: SCREENING
def screening():
    """This function takes nothing and returns a list of variables related to the task in the title. It's main function is to append that list of user inputted varaibles to 
    the appropriate csv file.  It calls upon the inp and dict_select functions."""
    target = dict_select(screening_targets,"SCREENING TARGET! Which TYPE of CHEMICAL did you use? Please select the NUMBER associated with list above: ",
                         "Bad input. Please enter the LIST NUMBER associated with the CHEMICAL you used")
    target_vol = inp("TARGET CHEMICAL! Please enter the VOLUME of CHEMICAL used: ")
    target_conc = inp("TARGET CHEMICAL! Please enter the CONCETNRATION of CHEMICAL used: ")
    plates = inp("PLATES! Please enter the number of PLATES you screened: ")
    setup_time = inp("How much TIME in MINUTES did you spend on screen SETUP: ")
    read_time = inp("How much TIME in MINUTES did you spend on screen READ: ")
    ts = datetime.datetime.utcnow()
    
    sc_results = pd.DataFrame([[ts,name,target,target_vol,target_conc,plates,setup_time,read_time]],columns=['ts','name','target','target_vol','target_conc','plates','setup_time','read_time'])
    sc_doc = pd.read_csv('screening.csv', index_col=0)
    new_results = sc_doc.append(sc_results,ignore_index=True)
    new_results.to_csv('screening.csv')
    
    return([ts,name,target,target_vol,target_conc,plates,setup_time,read_time])


# In[15]:

# FUNCTION DICTIONARY

# Creating an ordered dict of the main task functions, with numeric keys and list values. The lists contain the title of a 
# and the function itself

functions = OrderedDict([('1', ("Plate Filling", plate_filling)), ('2', ("Colony Picking", colony_picking)), 
                         ('3',("Spread Plating", plate_spreading)), ('4', ("Plate Replication",plate_replication)), ('5',("Screening", screening))])


# In[16]:

# Selecting items from a dictionary of functions

def dict_select_func(dict,question,scold):
    """This function takes a dictionary, a question in the form of a string, and a message in the form of a string 
    to allert users of a bad input.  It returns a function out of the dictionary to be executed."""
    for vals in dict:
        print(vals,dict[vals][0])
    dummy = False 
    while dummy == False:
        dict_key = inp_str(question)
        try:
            val = dict[dict_key][1]
            dummy = True
        except:
            print(scold)
            dummy = False
    print('')
    return(val())


# In[17]:

# MAIN FUNCTION




dummy = False

while dummy == False:
    name = dict_select(staff, "Hello! Who are you? Select the NUMBER associated with your name on the list above!",
                       "Bad input, Please enter the LIST NUMBER associated with your NAME: ")
    more = 0
    dict_select_func(functions, 
                     "What TASK would you like to enter information for? Please selest the NUMBER assosciated with the list above: ", 
                     "Bad input, Please enter the LIST NUMBER associated with the TASK you performed: ")
    more = inp("Are there more tasks you would like to enter data for? Enter 1 for YES - or - 2 for NO: ")
    if more == 1:
        dummy = False
        print('')
    elif more == 2:
        dummy = True
        print('')
    else:
        dummy = False
        print('')

