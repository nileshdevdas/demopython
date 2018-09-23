import pandas as pd;
import matplotlib.pyplot as plt;
import mplcursors;



# load the data
dataframe = pd.read_csv("C:/input/Customers.csv");
# find the info of the data
print(dataframe)
print(dataframe.info());
mplcursors.cursor(hover=True)
nationality= dataframe.groupby("Nationality")

for eachnation in nationality:
    print(eachnation);
# try slicing and dicing the data filtering or indexing
ages = dataframe['Age']
print(ages)
print(dataframe.head());
print(dataframe.tail());

print(dataframe.columns);

countries = dataframe['Nationality'].unique();
print(countries);
# now try applying different aggregations or combintations to the data

an  = dataframe[['Age', 'Nationality']]

print(dataframe.describe())
print(an);

print(dataframe['Age'].mean())
print(dataframe['Age'].max())
print(dataframe['Age'].min())
print(dataframe.transpose())

print(dataframe['Age'].rolling(1).sum())

print(dataframe.groupby('Age').agg(['count','mean']));

# start plotting different

print(dataframe);
x=dataframe['customerName'];
y=dataframe['Age']

############################ SELECT ONLY SPECIF COLS ###################
print(">>>>>>>>>>>>>>>>>>>>>>>>> SELCTED COLS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

an  = dataframe[['Age', 'Nationality']]
print(an)
print(">>>>>>>>>>>>>>>>>>>>>>>>> SELCTED COLS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
############################ SELECT ONLY SPECIF COLS ###################

############################ Group By Count ###################
print(">>>>>>>>>>>>>>>>>>>>>>>>> Group By Count <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print(dataframe.groupby('Age').agg(['count','mean']));
print(">>>>>>>>>>>>>>>>>>>>>>>>> Group By Count <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
############################ Group By Count ###################

#############################short preview of my whole data ###################
print("###############description of data #######################")
print(dataframe.describe())
print("###############description of data #######################")
###############################################################################
################################ drop na values row ###########################
print(dataframe.dropna())
################################ drop na values row ###########################
############################ PIVOT CODING ######################
print(dataframe.pivot(index='customerName', columns='Nationality', values='Age'));
############################ PIVOT CODING ######################\

##### pip install numpy , pandas, matplotlib,
######################## CODE FOR HOVERED VALUES #######################
#####import matplotlib.pyplot as plt;
x=dataframe['customerName']; # this x axis
y=dataframe['Age']  # this y axis
fig, ax = plt.subplots()  # create the canvas ---> on which -plot
ax.plot(x,y)
ax.set_title("Mouse over a point")
# mplcursors desinged ---> Find any object of plt is enabled
mplcursors.cursor(hover=True)
plt.show()
######################## CODE FOR HOVERED VALUES #######################
print("XXXXXXXXXXxx")
print(dataframe.filter(items=['Age']))

is_nilesh  = dataframe['customerName']=='Nilesh';

for v in is_nilesh:
    print(v == True)

dataframe.filter(items = [1]);
