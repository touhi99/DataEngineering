import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("test.csv", sep=";", header=None)
df.columns = ['x','y']
#print(df)

df_x = df.sort_values(['x','y'], ascending=[False, False])
df_y = df.sort_values(['y','x'], ascending=[False, False]) 
df_x = df_x.reset_index()
df_y = df_y.reset_index()

x_list = []
y_list = []

df_x_prev = (-5555,-5555)
df_y_prev = (-5555,-5555)
for i,j in zip(range(len(df_x.index)), range(len(df_y.index))):
	'''FOR X-AXIS'''
	''' While Same X-axis has multiple same value, keep skipping'''
	while df_x.x[i] == df_x_prev[0]:
		i+=1
		continue
	''' For first point case, where X-axis value is higher'''
	if df_x.x[i] > df_x_prev[0]:

		df_x_prev = list(df_x_prev)
		df_x_prev[0] = df_x.x[i]
		df_x_prev[1] = df_x.y[i]
		df_x_prev = tuple(df_x_prev)

		x_list.append((df_x.x[i], df_x.y[i]))

	''' While next X-axis point has higher Y-value than current '''
	elif df_x.y[i] > df_x_prev[1]:
		
		df_x_prev = list(df_x_prev)
		df_x_prev[0] = df_x.x[i]
		df_x_prev[1] = df_x.y[i]
		df_x_prev = tuple(df_x_prev)

		x_list.append((df_x.x[i], df_x.y[i]))
	
	'''FOR Y-AXIS'''
	while df_y.y[j] == df_y_prev[1]:
		j+=1
		continue

	if df_y.y[j] > df_y_prev[1]:
		df_y_prev = list(df_y_prev)
		df_y_prev[0] = df_y.x[j]
		df_y_prev[1] = df_y.y[j]
		df_y_prev = tuple(df_y_prev)

		y_list.append((df_y.x[j], df_y.y[j]))

	elif df_y.x[j] > df_y_prev[0]:
		df_y_prev = list(df_y_prev)
		df_y_prev[0] = df_y.x[j]
		df_y_prev[1] = df_y.y[j]
		df_y_prev = tuple(df_y_prev)

		y_list.append((df_y.x[j], df_y.y[j]))

#print(x_list)
#print(y_list)

c_list = list(set(x_list).intersection(y_list))
print(c_list)
'''
fig = plt.figure()
plt.scatter(df.x,df.y)
plt.grid()
plt.show()
'''