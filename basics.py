# import os
# os.environ['MPLCONFIGDIR'] = r'C:\Users\sushm\OneDrive\Desktop\Matplotlib'
# import matplotlib.pyplot as plt
# # from matplotlib import pyplot as plt
# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
# # plt.plot(x,y)
# # plt.show()
# c=["b","m","r","c","y"]
# plt.bar(x,y,color=c)
# plt.show()


# Bar plot
import os
os.environ['MPLCONFIGDIR'] = r'C:\Users\sushm\OneDrive\Desktop\Matplotlib'
import matplotlib.pyplot as plt
x=["Python","C","C++","Javascript"]
y=[99,45,56,85]
z=[98,67,86,56]
plt.xlabel("language")
plt.ylabel("Number")
plt.title("Sushmita")
width=0.2
# c=["y","b","m","g"]
plt.bar(x,y,width=0.5,color="b",edgecolor="b",label="Sushmita")
plt.bar(x,z,width=0.5,color="y",edgecolor="b",label="Sushmita1")
plt.legend()
plt.show()

