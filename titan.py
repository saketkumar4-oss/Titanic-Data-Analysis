import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#======================================================================
#                         PROJECT 2.1
#======================================================================
#import pandas as pd

df = pd.read_excel("Titanic-Data.xlsx")

# First 5 rows
#print(df.head())

# Dataset information
#print(df.info())

# Statistical summary
#print(df.describe())


#print(df["Survived"].value_counts())

#print(df.groupby("Pclass")["Survived"].mean())

children = df[df["Age"] < 18]

print(children["Survived"].mean())




#======================================================================
#                       PROJECT 3.1
#======================================================================


df=pd.read_excel("Titanic-Data.xlsx")
#print(df)

# COUNT MISSING VALUES IN EACH COLUMN
#print(df.isnull().sum())

#IMPUTE MISSING AGE WITH MEDIAN AGE

df["Age"] = df["Age"].fillna(df["Age"].median())
#print(df["Age"].isnull().sum())




#IMPUTE MISSING EMBARKED WITH MODE
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
#print(df["Embarked"].isnull().sum())


#MISSING VALUES IN CABIN

df["Cabin"] = df["Cabin"].fillna("Unknown")
#print(df["Cabin"])


#CHECKING DATA TYPE
#print(df.info())

#===========X STRETCH GOAL(impute age using the median age within each passenger class) X=============


df["Age"] = df.groupby("Pclass")["Age"].transform(
    lambda x: x.fillna(x.median())
)


#====================================================
#                 PROJECT 4.1
#====================================================
# CALCULATE MEAN, MEDIAN, MODE AND STANDARD DEVIATION FOR FARE
mean_fare = df["Fare"].mean()
median_fare = df["Fare"].median()
mode_fare = df["Fare"].mode()[0]
std_fare = df["Fare"].std()

# print("Mean:", mean_fare)
# print("Median:", median_fare)
# print("Mode:", mode_fare)
# print("Standard Deviation:", std_fare)


#COMPARE THE MEAN AND MEDIAN OF FARE
mean_fare = df["Fare"].mean()
median_fare = df["Fare"].median()

#print("Mean Fare:", mean_fare)
#print("Median Fare:", median_fare)


#COMPUTE THE CORRELATION BETWEEN AGE AND FARE
correlation = df["Age"].corr(df["Fare"])
#print("Correlation:", correlation)


#PLOT THE HISTOGRAM OF AGE
# plt.hist(df["Age"], bins=20)
# plt.title("Histogram of Age")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
#plt.show()


#================ X STRETCH GOAL (FIRST CLASS PASSENGER PAY MORE) X===============================

avg_fare = df.groupby("Pclass")["Fare"].mean()

#print(avg_fare)



#=======================================================
#                      PROJECT 5.1
#=======================================================

# PLOT A HISTOGRAM OF "AGE" AND BAR CHART OF SURVIVAL COUNT====================================

plt.figure(figsize=(6,4))
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
#plt.show()


survival_counts = df["Survived"].value_counts().sort_index()
#print(survival_counts)

plt.figure(figsize=(5,4))
plt.bar(["Died (0)", "Survived (1)"], survival_counts.values)
plt.title("Survival Counts")
plt.xlabel("Status")
plt.ylabel("Count")
#plt.show()


#DRAW BOX PLOT OF "FARE" SPLIT BY SURVIVAL (SURVIVED VS NOT)===============================

survived = df[df["Survived"] == 1]["Fare"]
not_survived = df[df["Survived"] == 0]["Fare"]


plt.figure(figsize=(8, 5))
plt.boxplot([not_survived, survived],
             labels=["Not Survived", "Survived"])

plt.title("Fare Distribution by Survival Status")
plt.xlabel("Survival Status")
plt.ylabel("Fare")
#plt.show()

#SURVIVAL RATE BY P-CLASS AND BY SEX==================================

survival_by_pclass = df.groupby("Pclass")["Survived"].mean()

plt.figure(figsize=(5,4))
survival_by_pclass.plot(kind="bar")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Pclass")
plt.ylabel("Survival Rate")
#plt.show()


survival_by_sex = df.groupby("Sex")["Survived"].mean()

plt.figure(figsize=(5,4))
survival_by_sex.plot(kind="bar")
plt.title("Survival Rate by Sex")
plt.xlabel("Sex")
plt.ylabel("Survival Rate")
#plt.show()



# CORRELATION HEATMAP OF NUMERIC COLUMN========================================================

numeric_df = df.select_dtypes(include=['number'])
#print(numeric_df)

corr_matrix = numeric_df.corr()

#print(corr_matrix)


# plt.figure(figsize=(10, 8))
# sns.heatmap(
#     corr_matrix,
#     annot=True
# )

# plt.title("Correlation Heatmap of Numeric Columns")
#plt.show()

#================== X CREATING DASHBOARD USING STREAMLIT X===============================================

def age_distribution(df):
    fig, ax = plt.subplots(figsize=(6,4))
    ax.hist(df["Age"], bins=20)
    ax.set_title("Age Distribution")
    ax.set_xlabel("Age")
    ax.set_ylabel("Frequency")
    return fig

def survival_by_class(df):
    fig, ax = plt.subplots(figsize=(6,4))
    survival_rate = df.groupby("Pclass")["Survived"].mean()
    survival_rate.plot(kind="bar", ax=ax)
    ax.set_title("Survival Rate by Passenger Class")
    ax.set_ylabel("Survival Rate")
    return fig

def fare_boxplot(df):
    fig, ax = plt.subplots(figsize=(6,4))
    df.boxplot(column="Fare", by="Survived", ax=ax)
    ax.set_title("Fare Distribution by Survival Status")
    plt.suptitle("")
    return fig

def survival_by_sex(df):
    fig, ax = plt.subplots(figsize=(6,4))
    survival_rate = df.groupby("Sex")["Survived"].mean()
    survival_rate.plot(kind="bar", ax=ax)
    ax.set_title("Survival Rate by Sex")
    ax.set_ylabel("Survival Rate")
    return fig
