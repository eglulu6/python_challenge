# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#import libraries
import os, csv

#define path to file
csvpath = os.path.join('Resources', 'election_data_sample.csv')
#use path variable to open csv file
csvfile = open(csvpath)
#initiate csvreader
electdata = csv.reader(csvfile,delimiter=',')
header = next(electdata)
print(header) #['ï»¿Voter ID', 'County', 'Candidate']


# %%
#initialize vote counter
fullcandlst = []
#initialize candidate set to create a list of non duplicate candidates
cand_set = set(())
candlst = list(cand_set)


# %%
#loop thru csv rows to add to vote count AND create the candidate set
for row in electdata:
    cand_set.add(row[2])
    fullcandlst.append(row[2])


# %%
votecount= []
for name in fullcandlst:
    x = fullcandlst.count(name)
    votecount.append(x)
print(votecount)


# %%
#sets are restrictive so convert to list type
candlst = list(cand_set)
#use list to create a dictionary
#loop thru candlst and for every cand use cand as key : value = votecount 
cand_dict= {cand :2 for cand in candlst }
cand_dict


# %%
for row in electdata:
    print(row[2])


# %%



# %%
#get ea candidates total votes
#percentage e/a candidate won
#percentage = sum(candqty)/votecount


