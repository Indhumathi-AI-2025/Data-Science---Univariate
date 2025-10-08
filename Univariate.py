import pandas as pd
import numpy as np
class univariate:
    def QuanQual(dataset):
        qual = []
        quan = []
        for ColumnName in dataset.columns:
            if (dataset[ColumnName].dtype == 'O'):
                qual.append(ColumnName)
            else:
                quan.append(ColumnName)
        return quan, qual
    def Centre_Percentile_IQR(quan,dataset):
            descriptive = pd.DataFrame(index = ["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5 Rule","Lesser","Greater","Min","Max"],columns = quan)
            #Mean
            for ColumnName in quan:
                descriptive[ColumnName]["Mean"] = dataset[ColumnName].mean()
            #Median
                descriptive[ColumnName]["Median"] = dataset[ColumnName].median()
            #Mode
                descriptive[ColumnName]["Mode"] = dataset[ColumnName].mode()[0]
            #Percentile
                descriptive[ColumnName]["Q1:25%"] = dataset.describe()[ColumnName]["25%"]
                descriptive[ColumnName]["Q2:50%"] = dataset.describe()[ColumnName]["50%"]
                descriptive[ColumnName]["Q3:75%"] = dataset.describe()[ColumnName]["75%"]
                descriptive[ColumnName]["99%"] = np.percentile(dataset[ColumnName],99)
                descriptive[ColumnName]["Q4:100%"] = dataset.describe()[ColumnName]["max"]
            #IQR
                descriptive[ColumnName]["IQR"] = descriptive[ColumnName]["Q3:75%"] - descriptive[ColumnName]["Q1:25%"]
                descriptive[ColumnName]["1.5 Rule"] = 1.5 * descriptive[ColumnName]["IQR"]
                descriptive[ColumnName]["Lesser"] = descriptive[ColumnName]["Q1:25%"] -  descriptive[ColumnName]["1.5 Rule"]
                descriptive[ColumnName]["Greater"] = descriptive[ColumnName]["Q3:75%"] +  descriptive[ColumnName]["1.5 Rule"]
                descriptive[ColumnName]["Min"] = dataset[ColumnName].min()
                descriptive[ColumnName]["Max"] = dataset[ColumnName].max()
            return descriptive
    #Function for Lesser and Greater Outliers
    def less_great_outlier(quan,descriptive):
        lesser = []
        greater = []
    
        for ColumnName in quan:
            if(descriptive[ColumnName]["Min"]< descriptive[ColumnName]["Lesser"]):
                lesser.append(ColumnName)
            if(descriptive[ColumnName]["Max"]> descriptive[ColumnName]["Greater"]):
                greater.append(ColumnName)
        return lesser, greater
    #Replacing Outliers
    def Replace_Outlier(dataset, lesser, greater, descriptive):
        for ColumnName in lesser: 
            dataset[ColumnName][dataset[ColumnName]< descriptive[ColumnName]["Lesser"]] = descriptive[ColumnName]["Lesser"]
        for ColumnName in greater: 
            dataset[ColumnName][dataset[ColumnName]> descriptive[ColumnName]["Greater"]] = descriptive[ColumnName]["Greater"] 
        return dataset
    #Frequency
    def FreqTable(dataset):
        freq_tables = {}  # dictionary to store frequency tables for each column
        for ColumnName in dataset.columns:
            freq_df = pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Frequency","Cumsum"])
            freq_df["Unique_Values"] = dataset[ColumnName].value_counts().index
            freq_df["Frequency"] = dataset[ColumnName].value_counts().values
            freq_df["Relative_Frequency"] = freq_df["Frequency"] / 103
            freq_df["Cumsum"] = freq_df["Relative_Frequency"].cumsum()
            freq_tables[ColumnName] = freq_df  # store the table for this column
        return freq_tables
    
