import ReadingFile
import clustering
import Model

# enter the type of file is need to be read
file_path = input ("enter file path  ")
# data_type =input ("please enter the type of file  ") 
object_Read = ReadingFile.READ_FILE (file_path)

prep = ReadingFile.Preparation(object_Read.df)
df=prep.df
#get the value of target
y = df.Rent
#remove target column from dataset
# df=ReadingFile.Preparation(df).dropColumns(df,'Rent')
#remove date column
df=ReadingFile.Preparation(df).dropColumns(df , 'Posted On')

#cluster dataset by choosing the model of clustering basesd on variables type
categorical_idx = [2,  3 , 4 , 5 , 6 , 7 ,9]  
model = input("enter the model of clustering ")
object_cluster = clustering.Cluster(df , categorical_idx ,'Rent' ,y)
#remove categorical columns
df = object_cluster.df

df=ReadingFile.Preparation(df).dropColumns(df , 'Floor')
df=ReadingFile.Preparation(df).dropColumns(df , 'Area Type')
df=ReadingFile.Preparation(df).dropColumns(df , 'Area Locality')
df=ReadingFile.Preparation(df).dropColumns(df , 'City')
df=ReadingFile.Preparation(df).dropColumns(df , 'Furnishing Status')
df=ReadingFile.Preparation(df).dropColumns(df , 'Tenant Preferred')
df=ReadingFile.Preparation(df).dropColumns(df , 'Point of Contact')

print(df[df['cluster']==0].head(5))

print(df[df['cluster']==1].head(5))

print(df[df['cluster']==2].head(5))



Feature_Names=['BHK', 'Size', 'Bathroom', 'PostedOn', 'SuperArea',
        'CarpetArea', 'BuiltArea', 'Month', 'Day' ,'cluster','cluster_0' ,'cluster_1' ,'cluster_2','Rent']

object_Model =Model.Models(df , Feature_Names)






