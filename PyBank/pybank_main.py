# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#import the needed libraries
import os, csv

#tell computer how to get to the file you want
csvpath = os.path.join('Resources', 'budget_data.csv')

#Okay now that im here what do you want me to do with it? - open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

#skip first row & consider then as header    
    header = next(csvreader)

#initialize lists
    date = []
    pandl = []
    
#loop thru rows in csvreader to make lists of each column
    for row in csvreader:
        date.append(row[0])
        pandl.append(int(row[1]))

#use the date list to find the total number of months included in the dataset
    monthcount = len(date)
    
#sum the total list of pandl to get net total amount of "Profit/Losses" over the entire period
    nettotal = sum(pandl)
    
#loop thru 'pandl' list values to get values of total monthly change
    #Jan has no previous value to subtract from so start at feb-10 
    chg = []
    for x in range(1, len(pandl)): #range(<startvalue>, <endvalue>)
        chg.append(int(pandl[x]-pandl[x-1])) #'x' is the current row minus 'x-1 = the previous row

#take the sum of chg values before cacluating average
    totalchg = float(sum(chg))
    #find the average of those changes
    avgchg = float(round(totalchg/(len(pandl)-1),2)) #minus 1 becuse we skipped jan value
#find max value in chg list
    maxchg = round(float(max(chg)),2)
    minchg = round(float(min(chg)),3)
    
    print(f'${totalchg}')


# %%
#In addition, your final script should both print the analysis to the terminal
#export a text file with the results

#tell computer where to create the new file
txtpath_out = os.path.join('analysis', 'budget_analysis.txt')

#what type the new file should be and at teh same time make the file object
with open(txtpath_out, 'w', newline='') as txtfile:
    
#we need to tell it what to write on the file
    txtfile.write(f'Financial Analysis\n --------------------------------------------- \nTotal Months: {monthcount}\nNet Total: ${nettotal}\nAverage Change: ${avgchg}\nGreatest Profit Increase: ${maxchg}\nGreatest Profit Decrease: ${minchg}')


# %%



# %%



