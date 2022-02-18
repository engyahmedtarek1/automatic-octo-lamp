#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np
    
CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }
global city
def load_city():
    global city
    while True:        
        city= input("")
        city=city.title()
        if city in CITY_DATA:
            print("Thank you for choosing {}".format(city))
            break
        else:
            print("please choose one of the following city:\n Chicago, New York City, Washington ?  ")
            continue
    return city
def load_df():
    city=load_city()
    df = pd.read_csv(CITY_DATA[city])
    df= df.dropna(axis=0)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Hours']= df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.strftime('%b')
    df['day_of_week'] = df['Start Time'].dt.strftime('%a')
    return  df

def load_month(df): 
    global month
    """ Take Data Fram returned the same data frame filtered by month """
    print("Which month do you like to explore first 6 month only (January, February, ... , June) ?")
    while True:
        month= input(" ")
        month=month.title()
        month_to_check= month[0:3]
        if month_to_check in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'] :
            month = month_to_check
            break
        else: 
            print('Only first 6 months are avaliable enter correct month(January, February, ...  , June)')
            continue
    df = df[df['month']== month]
    return df

def load_day(df):
    global day
    """ Take Data Fram returned the same data frame filtered by day """
    print("Which day do you like to explore (Monday, Tuesday, ... Sunday)?")
    while True:
        day= input(" ")
        day=day.title()
        day_to_check= day[0:3]
        if day_to_check in ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri'] :
            day = day_to_check
            break
        else: 
            print("Please enter correct day name(Monday, Tuesday, ... Sunday)?")
            continue
    
    df = df[df['day_of_week']== day]
    return df

def station_stats(df):
    """Take Data Frame and Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    s_station = df['Start Station'].mode()[0]
    s_station_v = df['Start Station'].value_counts().max()
    print('Most commonly used start station is {} with {} trip.'.format(s_station,s_station_v ))

    #display most commonly used end station
    e_station= df['End Station'].mode()[0]
    e_station_v = df['End Station'].value_counts().max()
    print('Most commonly used end station is {} with {} trip.'.format(e_station,e_station_v ))

    #  display most frequent combination of start station and end station trip
    combin_station =df.groupby('Start Station')['End Station'].value_counts().max()
    print("The most frequent combination of start station and end station trip is {} trip.".format(combin_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def time_stats(df):
    
    """Take Data Frame and Displays statistics on the most frequent times(month, day, hour) of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month 
    com_month= df['month'].mode()[0]
    print("Most Common Month is {}".format(com_month))

    # display the most common day of week
    com_day =df['day_of_week'].mode()[0]
    print("Most Common Day Of The Week is {}".format(com_day))
    
    # display the most common start hour
    com_hour= df['Hours'].mode()[0]
    print("Most Common Start Hour is {}".format( com_hour)) 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Take Data Frame and Displays statistics on the total and average trip duration in seconds."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    hour_sum= df['Trip Duration'].sum()
    print("Total Travel Time: {} seconds".format(hour_sum))

    hour_mean= df['Trip Duration'].mean()
    print("Mean :  {} seconds".format(hour_mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Statsistics ......\n')
    start_time = time.time()

    #  Display counts of user types
    user_type=df['User Type'].value_counts()
    print('User type \n', user_type)
   
    # validate if required columns is available in dataFrame and Display counts of gender 
    while True:
        if city in ['Chicago', 'New York City']:
            gender =df['Gender'].value_counts()
            print("Gender Count\n",gender)
            # TO DO: Display earliest, most recent, and most common year of birth
            df['Birth Year'] = df['Birth Year'].astype(int)
            early_year=df['Birth Year'].min()
            recent_year=df['Birth Year'].max()
            common_year=df['Birth Year'].mode()[0]
            print(" 1) Earliest birth year is :{} ".format(early_year))
            print(" 2) Most recent birth year is {} ".format(recent_year))
            print(" 3) Common birth year is {} ".format(common_year))
            break
        else:
            break
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    print("How do you like to see(filter) your data?\n Please choose one letter (n, b, m,d):")
    print(" N for no filtration(all months and days),\n b to filter by month and day ,\n m to filter by month only,\n d to filter by day only")
    
    choioce_list=["n","b", "m","d"]

    while True:
        user_choice=input(" ")
        user_choice=user_choice.lower()
        if user_choice not in choioce_list:
            print("Please type one of the following letters:")
            print(" N for no filtration,\n b to filter by month and day ,\n m to filter by month only,\n d to filter by day only")
            continue
        else:
            break
           
    print("Which city do you like to explore  statistics \n Chicago, New York City, Washington ?")
    df=load_df()
    if user_choice == "b":
        
        df = load_month(df)  
        df = load_day(df)
        com_hour= df['Hours'].value_counts().index[0]
        print("Most Common Start Hour is: ", com_hour)
          
    elif user_choice == "m":
        df = load_month(df)
        com_day =df['day_of_week'].value_counts().index[0]
        print("Most Common Day Of The Week is:  ",com_day)
        com_hour= df['Hours'].value_counts().index[0]
        print("Most Common Start Hour is : ", com_hour) 
            
    elif user_choice == "d":
        df = load_day(df)
        com_hour= df['Hours'].value_counts().index[0]
        print("Most Common Start Hour is: ", com_hour) 
        
            
    else:
        time_stats(df)
          
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    df_size=df.size
    x=np.arange(1, df_size, 5)
    for i in x:
        print(df[i:i+5])
        print(" Do you like to display more rows?\n Please type (yes or no)?")
        
        while True:
            user_ans=input("")
            user_ans = user_ans.lower()
            if user_ans not in ["no", "yes"]:
                print("Please type yes or no ")
                continue
            else:
                break
        if user_ans == "yes":
            print("Thank you, let's continue our statistics ")
            continue
        else:
            break
    return df
def main():
    
    get_filters()
    while True:
        print("Do you like to restart your research?")
        user_ans=input("")  
        user_ans = user_ans.lower()
        if user_ans not in ["no", "yes"]:
            print("Do you want to explore more?")
            print("Please type yes or  no ")
            continue
        if user_ans == "yes":
            get_filters()
            continue
        else:
            break
    print("Thank You, Good Bye") 
if __name__ == "__main__":
	main()


# In[ ]:




