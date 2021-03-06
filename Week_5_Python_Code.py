import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
import os

'''
   Name:    MSDS600_X70_Python
   Author:  Robert Apple
   Date:    22-jul-2021 
   
   Purpose: Written in partial fulfillment of the Week 5 required material for the Regis class.
   
   Discussion:  This code loads up the Churn data from Week 2 (TRAINING_DATA_URL), and the new_churn_data
                (NEW_CHURN_DATA) from Week 5. It then loads the GBC machine learning model and trains
                 it up using the Week 2 data.  Finally, it outputs predictions on the new churn data.
'''

#--GLOBAL Variables
#------------------
TRAINING_DATA_URL = 'https://raw.githubusercontent.com/Rob4Hope/MSDS600_X70/main/week_5_data.csv'
NEW_CHURN_DATA =  'https://raw.githubusercontent.com/Rob4Hope/MSDS600_X70/main/new_churn_data.csv'

#--normal variables
#------------------
df = pd.DataFrame()
new_churn_data = pd.DataFrame()

def load_up_dataframes():
   #--Lets get that
   global df
   df = pd.read_csv(TRAINING_DATA_URL, index_col='customerID')


def get_the_model_ready(in_x_train, in_y_train):
    gbc = GradientBoostingClassifier()
    gbc.fit(in_x_train, in_y_train)
    return gbc

if __name__ == '__main__':
   load_up_dataframes()

   #--Allow for the entering of a DataFrame manually
   #------------------------------------------------
   try:
     os.system('cls')
     user_choice = input('Do you want to enter the new_churn_data.csv URL manually, or use what is stored in GitHub. (y/n) ')
     if (user_choice == 'Y' or user_choice == 'y'):
         url_name = input('Please enter the URL string of that file now.  ')
         new_churn_data = pd.read_csv(url_name, index_col='customerID')
   except:
      print("Something didn't work.  Going to use the one we have in GitHub already")
      new_churn_data = pd.read_csv(NEW_CHURN_DATA, index_col='customerID')


   #--I'm gunna run this the old fashioned way.  Load it all up from the beginning
   #------------------------------------------------------------------------------
   DV = "Churn"
   X_train = df.drop(DV, axis=1) #--this removes the "Dependent Variable" (DV) from our domain
   y_train = df[DV]              #--This has our DV in the range

   our_model = get_the_model_ready(X_train, y_train)

   my_output = []
   for i in range(5):
       output = our_model.predict(new_churn_data.iloc[i:i+1])
       my_output.append(output[0])

   print(my_output)















