import pandas as p
import matplotlib.pyplot as m
import seaborn as s
data=p.read_csv("C:\\Users\\PRK\\Desktop\\mtcars.csv")
# HISTOGRAM
mpg=data['mpg']
m.hist(mpg,bins='auto',color='r',edgecolor='k')
m.xlabel('Miles per gallon (mpg)');
m.ylabel('Frequency')
m.title('Frequency Distribution of mpg')
m.show()
# SCATTER
wt=data['wt']
iv=range(len(data))
m.scatter(iv,mpg,color='g',label='mpg')
m.scatter(iv,wt,color='k',label='wt')
m.title("Relationship b/w Weigth and MPG")
m.legend()
m.show()
# BAR PLOT
c=data['am'].value_counts()
co=['k','g']
m.bar(c.index,c.values,color=co,width=0.2)
m.xticks([0,1],['0-Automatic','1-Manual'])
m.xlabel("Tranmisson Type");m.ylabel("No of Cars")
m.title("Frequency distribution of transmission type of cars")
m.show()
# BOX PLOT
s.boxplot(mpg,color='c')
m.xlabel("MPG");m.ylabel("Values")
m.title("BOX plot of MPG Vlues")
