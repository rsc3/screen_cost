
# coding: utf-8

# In[ ]:

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


# In[ ]:


# Creating Output Files to store data

# Creates empty data frames with column names for each task, and then write them to a unique csv file
# BE CAREFUL WITH THIS - if their are csv files in your working directory with the same name, this will rewrite them
# index = range(0,0)
# plate_filling = pd.DataFrame(data=None,columns=['ts','name','target','target_volume','target_concerntration','plates','media','tips','fill_time'],index=index)
# colony_picking = pd.DataFrame(data=None,columns=['ts','name','dish_id','plates','lids','stickers','toothpicks','pick_time'],index=index)
# plate_spreading = pd.DataFrame(data=None,columns=['ts','name','dishes','media','spread_time'],index=index)
# plate_replication = pd.DataFrame(data=None,columns=['ts','name','tips', 'incubation_volume', 'replicator','plates','lids','stickers','rep_time'],index=index)
# screening = pd.DataFrame(data=None,columns=['ts','name','target','control_plates','treatment_plates','library_type','construct_id','incubation_time','setup_time'],index=index)
# plate_reading = pd.DataFrame(data=None,columns=['ts','name','read_time','plates_read','read1','read2','read3','fluorescence_type1','fluorescence_type2'],index=index)

# plate_filling.to_csv('plate_filling.csv')
# colony_picking.to_csv('colony_picking.csv')
# plate_spreading.to_csv('plate_spreading.csv')
# plate_replication.to_csv('plate_replication.csv')
# screening.to_csv('screening.csv')
# plate_reading.to_csv('plate_reading.csv')


# In[ ]:

# Defining Global Variables

# Creates dictionaries of variables to be called by list number (key) in functions

antibiotics = OrderedDict([("1", "Spectinomycin"), ('2', 'Chloramphenicol'), ('3', 'Kanamycin'), ('4','Tetracycline')])
plate_types = OrderedDict([('1', 'Clear'), ('2', 'Black')])
screening_targets = OrderedDict([('1', 'Lignin'), ('2', 'Lavender Oil'), ('3', 'Caffeine'), ('4', 'Isoprene'), ('5', 'Isoprenol'), 
                                 ('6', 'Limonene'), ('7', 'Vanilin'), ('8', 'P-coumaric Acid'), ('9', 'Vanilic Acid'), ('10', 'Camphor'), 
                                 ('11', 'Menthol'), ('12', 'Dipentene'),('13','Bisabolol'),('14','Pimelic Acid'),
                                 ('15','Nona-2,6-diene-ol'),('16','4-hydroxydecanote'),('17','7-aminoheptanoic acid'),('18','Water'),('19','Ethanol')])
staff = OrderedDict([('1',"Aneesha"),('2','Cameron'),('3','Giles'),('4','Nina'),('5','Will'),('6','Cindy')])
binary_dict =OrderedDict([("1", "Yes"), ("2", "No")])
read_units = OrderedDict([('1', 'Fluorescence'),('2', 'OD'),('3','Luminescence')])
fluorecence_reads = OrderedDict([('1','Gemini'),('2', 'MUG'),('3','mCherry')])
library_type = OrderedDict([('1', 'e.coli'),('2', 'fosmid')])
construct_id = OrderedDict([('1','gemini/specR'),('2','mCherry/KanR')])


# In[ ]:

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


# In[ ]:

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


# In[ ]:

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


# In[ ]:

# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# import pandas as pd
# import csv

# Creating Output Files to store data
# index = range(0,0)
# plate_filling = pd.DataFrame(data=None,columns=['ts','name','plates','media','tips','antibiotic','antibio_vol','antibio_conc','fill_time'],index=index)
# colony_picking = pd.DataFrame(data=None,columns=['ts','name','plates','lids','stickers','toothpicks','dishes','pick_time'],index=index)
# spread_plating = pd.DataFrame(data=None,columns=['ts','name','dishes','media','antibiotic','antibio_vol','antibio_conc','arabinose_vol','arabinose_conc','chloram_vol','chloram_conc','spread_time'],index=index)
# plate_replication = pd.DataFrame(data=None,columns=['ts','name','tips','replicator','plates','lids','stickers','rep_time'],index=index)
# screening = pd.DataFrame(data=None,columns=['ts','name','target','target_vol','target_conc','control_plates','treatment_plates', 'setup_time','read_time'],index=index)

# plate_filling.to_csv('plate_filling.csv')
# colony_picking.to_csv('colony_picking.csv')
# spread_plating.to_csv('plate_spreading.csv')
# plate_replication.to_csv('plate_replication.csv')
# screening.to_csv('screening.csv')


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


# In[ ]:

# pf_file1 = pd.read_csv('plate_filling.csv',index_col=0)
# pf_file1.head()
# ps_results = pd.DataFrame([[1.4,"Giles",13,13,17,14,15,14,15,15,15,4]],columns=['ts','name','dishes','media','antibiotic','antibio_vol','antibio_conc','arabinose_vol','arabinose_conc','chloram_vol','chloram_conc','spread_time'])
# new_frame_3 = new_frame_2.append(ps_results,ignore_index=True)



# In[ ]:

# new_frame_3


# In[ ]:

# TASK: PLATE FILLING

def plate_filling():
    """This function takes nothing and returns a list of variables related to the task in the title. It's main function is to append that list of user inputted varaibles to 
    the appropriate csv file.  It calls upon the inp function."""
    plates = inp("PLATES! Please enter the number of PLATES you used: ")
    media = inp("MEDIA! Please enter the total ml of MEDIA you poured: ")
    tips = inp("TIPS! How many tips did you use?: ")
#      will says we don't need these, so hashed out for now. if used in future need to add values back into output
#     antibiotic = dict_select(antibiotics,"Which ANTIBIOTIC did you use? Please select the NUMBER associated with your ANTIBIOTIC above: ","Bad input. Please enter the LIST NUMBER associated with the ANTIOBIOTIC you used")
#     antibio_vol = inp("ANTIBIOTICS! Please enter the VOLUME of ANTIBIOTICS used: ")
#     antibio_conc = inp("ANTIBIOTICS! Please enter the CONCETNRATION of ANTIBIOTICS used: ")
    target = dict_select(screening_targets,"SCREENING TARGET! Which TYPE of CHEMICAL did you use? Please select the NUMBER associated with list above: ",
                         "Bad input. Please enter the LIST NUMBER associated with the CHEMICAL you used")
    target_vol = inp("TARGET CHEMICAL! Please enter the VOLUME of CHEMICAL used in ml: ")
    target_conc = inp("TARGET CHEMICAL! Please enter the CONCETNRATION of CHEMICAL used in mM: ")
    fill_time = inp("TIME! How long in MINUTES did it take you to FILL PLATES: ")
    ts = datetime.datetime.utcnow()
    
    pf_results = pd.DataFrame([[ts,name,target,target_vol,target_conc,plates,media,tips,fill_time]],columns=['ts','name','target','target_volume','target_concerntration','plates','media','tips','fill_time'])
    pf_doc = pd.read_csv('plate_filling.csv', index_col=0)
    new_results = pf_doc.append(pf_results,ignore_index=True)
    new_results.to_csv('plate_filling.csv')

    
    return()


# In[ ]:

# TASK: COLONY PICKING

def colony_picking():
    """This function takes nothing and returns a list of variables related to the task in the title. It's main function is to append that list of user inputted varaibles to 
    the appropriate csv file.  It calls upon the inp function."""
    dummy = False
    
    while dummy == False:
        dishes = inp_str("DISH! Please enter the UNIQUE ID of the dish you picked out of: ")
        plates = inp("PLATES! Please enter the number of PLATES W/ MEDIA you used for ONLY the DISH you just entered: ")
        lids = plates
        stickers = plates
        toothpicks = (plates*98*1.25)
        
        pick_time = inp("TIME! How long in MINUTES did it take you to PICK COLONIES for ONLY the DISH you just entered: ")
        ts = datetime.datetime.utcnow()
    
        cp_results = pd.DataFrame([[ts,name,dishes,plates,lids,stickers,toothpicks,pick_time]],columns=['ts','name','dish_id','plates','lids','stickers','toothpicks','pick_time'])
        cp_doc = pd.read_csv('colony_picking.csv', index_col=0)
        new_results = cp_doc.append(cp_results,ignore_index=True)
        new_results.to_csv('colony_picking.csv')
        
        more_plates = dict_select(binary_dict, 'Did you pick colonies out of additional dishes? Enter 1 for Yes, or 2 for No', "Bad Input, please enter the NUMBER associated with your answer")
        if more_plates == 'Yes':
            dummy = False
        elif more_plates == 'No':
            dummy = True
    
    return()


# In[ ]:

# TASK: PLATE SPREADING

def plate_spreading():
    """This function takes nothing and returns a list of variables related to the task in the title. It's main function is to append that list of user inputted varaibles to 
    the appropriate csv file.  It calls upon the inp and dict_select functions."""
    dishes = inp("PETRI DISHES! Please enter the number of PETRI DISHES you used: ")
    media = inp("AGAR! Please enter the total ml of AGAR MEDIA you poured: ")
    dummy = False
    while dummy == False:
        electro_q = dict_select(binary_dict,"Did you Electroporate? Enter 1 for Yes, or 2 for No","Bad Input, please enter the NUMBER associated with your answer")
        if electro_q == "Yes":
            electro = inp("How many times did you electroporate?")
            dummy = True
        elif electro_q == "No":
            electro = None
            dummy = True
#      will says we don't need these, so hashed out for now. if used in future need to add values back into output    
#     antibiotic = dict_select(antibiotics,"Which ANTIBIOTIC did you use? Please select the NUMBER associated with your ANTIBIOTIC above: ","Bad input. Please enter the LIST NUMBER associated with the ANTIOBIOTIC you used")
#     antibio_vol = inp("ANTIBIOTICS! Please enter the VOLUME of ANTIBIOTICS used: ")
#     antibio_conc = inp("ANTIBIOTICS! Please enter the CONCETNRATION of ANTIBIOTICS used: ")
#     arabinose_vol = inp("ARABINOSE! Please enter the VOLUME of ARABINOSE used: ")
#     arabinose_conc = inp("ARABINOSE! Please enter the CONCETNRATION of ARABINOSE used: ")
#     chloram_vol = inp("CHLORAM! Please enter the VOLUME of CHLORAM used: ")
#     chloram_conc = inp("CHLORAM! Please enter the CONCETNRATION of CHLORAM used: ")
    spread_time = inp("TIME! How long in MINUTES did it take you to PLATE SPREAD: ")
    ts = datetime.datetime.utcnow()
    
    ps_results = pd.DataFrame([[ts,name,dishes,media,electro,spread_time]],columns=['ts','name','dishes','media','electroporate', 'spread_time'])
    ps_doc = pd.read_csv('plate_spreading.csv', index_col=0)
    new_results = ps_doc.append(ps_results,ignore_index=True)
    new_results.to_csv('plate_spreading.csv')
    
    
    
    return()


# In[ ]:

# TASK: PLATE REPLICATION
def plate_replication():
    """This function takes nothing and returns a list of variables related to the task in the title. It's main function is to append that list of user inputted varaibles to 
    the appropriate csv file.  It calls upon the inp and dict_select functions."""
    dummy = False
    replicator = 0
    tips = 0
    incubation_vol = 0
    while dummy == False:
        tip_q = dict_select(binary_dict, 'Did you use tips? Please select the NUMBER associated with your answer', "Bad input. Please enter the LIST NUMBER associated with your answer")
        if tip_q == "Yes":
            tips = inp("TIPS! How many tips did you use: ")
            dummy = True
        elif tip_q == "No":
            tips = None
            replicator = dict_select(binary_dict, 'Did you use replicators? Please select the NUMBER associated with your answer', "Bad input. Please enter the LIST NUMBER associated with your answer")
            dummy = True
    if tips != 0:
        incubation_vol = inp('INCUBATION VOLUME! What was the INCUBATION VOLUME in uL: ')
    plates = inp("PLATES! Please enter the number of PLATES W/ MEDIA you used: ")
    lids = plates 
    stickers = plates
#     plate_type = dict_select(plate_types, "PLATE TYPES! Which TYPE of PLATE did you use? Please select the NUMBER associated with list above: ", "Bad input. Please enter the LIST NUMBER associated with the PLATE TYPE you used")
    rep_time = inp("TIME! How long in MINUTES did it take you to REPLICATE PLATES: ")
    ts = datetime.datetime.utcnow()
    
    pr_results = pd.DataFrame([[ts,name,tips,incubation_vol,replicator,plates,lids,stickers,rep_time]],columns=['ts','name','tips','incubation_volume', 'replicator','plates','lids','stickers','rep_time'])
    pr_doc = pd.read_csv('plate_replication.csv', index_col=0)
    new_results = pr_doc.append(pr_results,ignore_index=True)
    new_results.to_csv('plate_replication.csv')
    
    return()


# In[ ]:

# TASK: SCREENING
def screening():
    """This function takes nothing and returns a list of variables related to the task in the title. It's main function is to append that list of user inputted varaibles to 
    the appropriate csv file.  It calls upon the inp and dict_select functions."""
    target = dict_select(screening_targets,"SCREENING TARGET! Which TYPE of CHEMICAL did you use? Please select the NUMBER associated with list above: ",
                         "Bad input. Please enter the LIST NUMBER associated with the CHEMICAL you used")
#     Moved the two below to plate filling
#     target_vol = inp("TARGET CHEMICAL! Please enter the VOLUME of CHEMICAL used in ml: ")
#     target_conc = inp("TARGET CHEMICAL! Please enter the CONCETNRATION of CHEMICAL used in mM: ")
    control_plates = inp("CONTROL PLATES! Please enter the number of CONTROL PLATES you screened: ")
    incubation_time = inp("INCUBATION TIME! How long did you INCUBATE in hours: ")
    treatment_plates = inp("TREATMENT PLATES! Please enter the number of TREATMENT PLATES you screened: ")
    lib_type = dict_select(library_type,"LIBRARY TYPE! Please enter the NUMBER associated with LIBRARY TYPE you used: ",
                           "Bad input. Please enter the LIST NUMBER associated with the LIBRARY TYPE you used")
    construct = None
    if lib_type == "fosmid":
        construct = dict_select(construct_id,"CONSTRUCT ID! Please enter the NUMBER associated with the CONSTRCUT ID used: ","Bad input. Please enter the LIST NUMBER associated with the CONSTRUCT ID you used" )
    setup_time = inp("How much TIME in MINUTES did you spend on screen SETUP: ")
    ts = datetime.datetime.utcnow()
    
    sc_results = pd.DataFrame([[ts,name,target,control_plates, treatment_plates,lib_type,construct,incubation_time,setup_time]],columns=['ts','name','target','control_plates','treatment_plates','library_type','construct_id','incubation_time','setup_time'])
    sc_doc = pd.read_csv('screening.csv', index_col=0)
    new_results = sc_doc.append(sc_results,ignore_index=True)
    new_results.to_csv('screening.csv')
    
    return()


# In[ ]:

# TASK: PLATE READING
def reading():
    read_time = inp("How much TIME in MINUTES did you spend on screen READ: ") 
    plates = inp("How many PLATES did you read?")
    dummy = False
    counter = 0
    read1 = None
    read2 = None
    read3 = None
    sub_fluor1 = None
    sub_fluor2 = None
    while dummy == False:
        read = dict_select(read_units,"What UNITS did you read? Please select the NUMBER associated with your UNIT from the list: ", "Bad input. Please enter the LIST NUMBER associated with your answer" )
        if read == "Fluorescence":
            sub_fluor1 = dict_select(fluorecence_reads, "Which Fluorescent MARKER did you use? Please select the NUMBER associated with your answer from the list: ", "Bad input. Please enter the LIST NUMBER associated with your answer")
            more_sub_fluor = dict_select(binary_dict, "Did you measure another Flurescent Marker? Please enter 1 for YES, or 2 for NO: ", "Bad input. Please enter the LIST NUMBER associated with your answer")
            if more_sub_fluor == "Yes":
                sub_fluor2 = dict_select(fluorecence_reads, "Which Fluorescent MARKER did you use? Please select the NUMBER associated with your answer from the list: ", "Bad input. Please enter the LIST NUMBER associated with your answer")
            elif more_sub_fluor == "No":
                sub_fluor2 = None
        if counter == 0:
            read1 = read
        elif counter == 1:
            read2 = read
        elif counter == 2:
            read3 = read
        more_reads = dict_select(binary_dict, "Did you read OTHER types of OUTPUT UNITS? Please enter 1 for YES, or 2 for NO: ","Bad input. Please enter the LIST NUMBER associated with your answer")
        if more_reads == "Yes":
            counter += 1
            dummy = False
        elif more_reads == "No":
            dummy = True
        
    ts = datetime.datetime.utcnow()
    
    re_results = pd.DataFrame([[ts,name,read_time,plates,read1,read2,read3,sub_fluor1,sub_fluor2]],columns=['ts','name','read_time','plates_read','read1','read2','read3','fluorescence_type1','fluorescence_type2'])
    re_doc = pd.read_csv('plate_reading.csv', index_col=0)
    new_results = re_doc.append(re_results,ignore_index=True)
    new_results.to_csv('plate_reading.csv')
    
    return()
            


# In[ ]:

# FUNCTION DICTIONARY

# Creating an ordered dict of the main task functions, with numeric keys and list values. The lists contain the title of a 
# and the function itself

functions = OrderedDict([('1', ("Plate Filling", plate_filling)), ('2', ("Colony Picking", colony_picking)), 
                         ('3',("Spread Plating", plate_spreading)), ('4', ("Plate Replication",plate_replication)),
                         ('5',("Screening", screening)), ('6',('Plate Reading', reading))])


# In[ ]:

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


# In[ ]:

# MAIN FUNCTION




dummy = False

while dummy == False:
    name = dict_select(staff, "Hello! Who are you? Select the NUMBER associated with your name on the list above!",
                       "Bad input, Please enter the LIST NUMBER associated with your NAME: ")
    more = 0
    dict_select_func(functions, 
                     "What TASK would you like to enter information for? Please selest the NUMBER assosciated with the list above: ", 
                     "Bad input, Please enter the LIST NUMBER associated with the TASK you performed: ")
    more = dict_select(binary_dict, "Are there more tasks you would like to enter data for? Enter 1 for YES - or - 2 for NO: ", "Bad Input. You really should have figured out how this works now.")
    if more == "Yes":
        dummy = False
        print('')
    elif more == 'No':
        dummy = True
        print('')
    else:
        dummy = False
        print('')

