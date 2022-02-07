# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:22:27 2020

@author: SELİM
"""
#Import numpy
import numpy as np


#Load data in the file data_1.csv into a numpy array and display.
data = np.loadtxt("data_1.csv",delimiter = ",",skiprows = 1, dtype = "str")
print("Vote data:\n", data)


#Find and display who became the president with how many votes.
candidate_1 = ("1", np.count_nonzero(data[:,5] == "1"))
candidate_0 = ("0", np.count_nonzero(data[:,5] == "0"))
maks = max(candidate_0[1],candidate_1[1])
arry = np.array([candidate_0,candidate_1])
print("President and his/her vote count:",arry[arry[:,1] == str(maks)])
president = arry[arry[:,1] == str(maks)][0][0]


#Find and display the age, education and income information about white and 
#other voters of president in two different arrays.
w_p_voters = data[(data[:,5] == president) & (data[:,1] == '"white"')]
print("The age, education and income information about white voters:\n",w_p_voters[:,2:5])

o_p_voters = data[(data[:,5] == president) & (data[:,1] == '"others"')]
print("The age, education and income information about other voters:\n",o_p_voters[:,2:5])


#Find and display the difference of number of white voters and other voters of the president.
diff = np.count_nonzero(w_p_voters[:,1]) - np.count_nonzero(o_p_voters[:,1])
print("Difference of number of white voters and other voters of the president:",diff)


#Find and display the voters of president with education level greater than 12.
voter_12 = data[:,3]
voter_12 = voter_12.astype(np.float)

voter_boolean = voter_12 > 12
print("The voters of president with education level greater than 12:")
print(data[(voter_boolean[:] == True) & (data[:,5] == president)])


#Find and display the mean of ages of the voters of president.
ages = data[:,2]

ages = ages.astype(np.float)
print("The mean of ages of the voters of president:\n", np.mean(ages))


#Find the mean of education levels of white voters and find the mean of education 
#levels of other voters and display the difference between them.

educ_white = data[data[:,1] == '"white"'][:,3]

educ_white = educ_white.astype(np.float)

educ_other = data[data[:,1] == '"others"'][:,3]

educ_other = educ_other.astype(np.float)

print("The difference betweenthe mean of education levels of white voters and the mean of education levels of other voters:")
print(abs(np.mean(educ_white) - np.mean(educ_other)))


#Find and store in a boolean array, age_35, if voter is older than 35.
age_35 = ages > 35

#Using age_35 array, find the voters who vote for candidate_1
print(data[(data[:,5] == "1") & (age_35[:] == True)][:,0:3:2])


#Find the difference between mean of incomes of voters who voted for president,
#and who voted for the other candidate.
income_vote = data[:,4:]

a = income_vote.astype(np.float)

print("The difference between mean of incomes of voters who voted for president,and who voted for the other candidate:")
print(np.mean(a[a[:,1] == 1][:,0]) - np.mean(a[a[:,1] == 0][:,0]))
















