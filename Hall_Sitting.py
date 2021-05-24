import pandas as pd 
import os
import numpy as np 
data = pd.read_csv('E:\\Courses\\Python Projects\\Hall Sitting\\input1.csv')
data = data.replace(np.nan,0)
def pre(col):
	return [i for i in col if i!=0]
all_data = []
for i in data.columns:
	all_data.append(pre(data[i]))
index_ = [len(i) for i in all_data]
pre_processed_data = [0 for i in range(sum(index_)*2)]
main_data = []
for i in range(len(index_)):
	main_data.append(all_data[index_.index(max(index_))])
	index_[index_.index(max(index_))]=0
for i in range(len(main_data)):
	if pre_processed_data.index(0)%2==0:
		for j,l in zip([k for k in range(pre_processed_data.index(0),(len(main_data[i])*2)+pre_processed_data.index(0)) if k%2==0],main_data[i]):
			pre_processed_data[j]=l
	else:
		for m,n in zip([o for o in range(pre_processed_data.index(0),(len(main_data[i])*2)+pre_processed_data.index(0)) if o%2!=0],main_data[i]):
			pre_processed_data[m]=n
pre_processed_data = [str(int(i)) for i in pre_processed_data if i!=0]
class_room = []
csv_dict = {'SNO':[],'HALL NO':[],'DEGREE':[],'SUBJECT OF THE EXAM':[],'REG NO OF THE CANDIDATE':[],'NO OF STUDENT':[],'TOTAL':[],'Name of the Hall Superintendent':[]}
def to_return_degree_name(setarr):
	deg = []
	for i in setarr:
		if i=='101':
			deg.append('BE-CIVIL')
		elif i=='102':
			deg.append('BE-CSE')
		elif i=='103':
			deg.append('BE-AGRI')
		elif i=='104':
			deg.append('BE-ECE')
		elif i=='105':
			deg.append('BE-EEE')
		elif i=='106':
			deg.append('BE-MECH')
		elif i=='107':
			deg.append('BE-IT')
	return " , ".join(deg)
def get_number_of_students(arr):
	tot = []
	#print(set(arr))
	for i in set(arr):
		c = 0
		for j in arr:
			if str(i)==str(j):
				c+=1
		tot.append(str(c))
	return " , ".join(tot)
def candidate(l1,l2):
	re = []
	ok_pa = []
	for i in set(l2):
		ok_pa.append([])
		for j in range(len(l2)):
			if str(l2[j])==str(i):
				ok_pa[len(ok_pa)-1].append(int(l1[j]))
	#print(set(l2))
	#print(ok_pa)
	for i in ok_pa:
		f = min(i)
		t = max(i)
		re.append(str(f)+' - '+str(t))
	return " , ".join(re)
for i in range(len(pre_processed_data)//25):
    c1 = pre_processed_data[:7]
    c2 = pre_processed_data[7:13]
    c2 = c2[::-1]
    c2.insert(0,' ')
    c3 = pre_processed_data[13:19]
    c3.insert(0,' ')
    c4 = pre_processed_data[19:25]
    c4.append(' ')
    c4 = c4[::-1]
    df = pd.DataFrame.from_dict({'C1':c1,'C2':c2,'C3':c3,'C4':c4})
    df['C1'] = df['C1'].astype(str)
    df['C2'] = df['C2'].astype(str)
    df['C3'] = df['C3'].astype(str)
    df['C4'] = df['C4'].astype(str)
    class_room.append(df)
    del pre_processed_data[:25]
    csv_dict['SNO'].append(i+1)
    csv_dict['HALL NO'].append(' ')
    all_reg = []
    full_reg = []
    for i in c1:
    	all_reg.append(i[6:9])
    	full_reg.append(i)
    for i in c2:
    	all_reg.append(i[6:9])
    	full_reg.append(i)
    for i in c3:
    	all_reg.append(i[6:9])
    	full_reg.append(i)
    for i in c4:
    	all_reg.append(i[6:9])
    	full_reg.append(i)
    all_reg = [i for i in all_reg if i!='']
    full_reg = [i for i in full_reg if i!='']
    all_reg = [i for i in all_reg if i!=' ']
    full_reg = [i for i in full_reg if i!=' ']
    csv_dict['DEGREE'].append(to_return_degree_name(set(all_reg)))
    csv_dict['SUBJECT OF THE EXAM'].append(' ')
    csv_dict['NO OF STUDENT'].append(get_number_of_students(all_reg))
    csv_dict['TOTAL'].append(len(all_reg))
    csv_dict['Name of the Hall Superintendent'].append(' ')
    csv_dict['REG NO OF THE CANDIDATE'].append(candidate(full_reg,all_reg))
c1 = pre_processed_data[:7]
del pre_processed_data[:7]
if len(c1)!=7:
	while len(c1)!=7:
		c1.append('NA')
c2 = pre_processed_data[:6]
del pre_processed_data[:6]
if len(c2)!=6:
	while len(c2)!=6:
		c2.append('NA')
c3 = pre_processed_data[:6]
del pre_processed_data[:6]
if len(c3)!=6:
	while len(c3)!=6:
		c3.append('NA')
c4 = pre_processed_data[:6]
del pre_processed_data[:6]
if len(c4)!=6:
	while len(c4)!=6:
		c4.append('NA')
c2 = c2[::-1]
c4 = c4[::-1]
c2.insert(0,' ')
c3.insert(0,' ')
c4.insert(0,' ')
csv_dict['SNO'].append(len(csv_dict['SNO'])+1)
csv_dict['HALL NO'].append(' ')
all_reg = []
full_reg = []
for i in c1:
   	all_reg.append(i[6:9])
   	full_reg.append(i)
for i in c2:
   	all_reg.append(i[6:9])
   	full_reg.append(i)
for i in c3:
   	all_reg.append(i[6:9])
   	full_reg.append(i)
for i in c4:
   	all_reg.append(i[6:9])
   	full_reg.append(i)
all_reg = [i for i in all_reg if i!='NA']
all_reg = [i for i in all_reg if i!='']
full_reg = [i for i in full_reg if i!='NA']
full_reg = [i for i in full_reg if i!='']
csv_dict['DEGREE'].append(to_return_degree_name(set(all_reg)))
csv_dict['SUBJECT OF THE EXAM'].append(' ')
csv_dict['NO OF STUDENT'].append(get_number_of_students(all_reg))
csv_dict['TOTAL'].append(len(all_reg))
csv_dict['Name of the Hall Superintendent'].append(' ')
#print(full_reg)
#print(all_reg)
csv_dict['REG NO OF THE CANDIDATE'].append(candidate(full_reg,all_reg))
class_room.append(pd.DataFrame.from_dict({'C1':c1,'C2':c2,'C3':c3,'C4':c4}))
pd.DataFrame.from_dict(csv_dict).to_csv('Hall.csv',index=False)
os.popen('Hall.csv')
for i in range(len(class_room)):
	class_room[i].to_csv("Hall "+str(i)+".csv")
print('\n')
print('\n')
print('*'*len("Output file stored in "+os.getcwd()))
print('\n')
print("Output file stored in "+os.getcwd()+"\\Hall.csv")
print('\n')
print('*'*len("Output file stored in "+os.getcwd()))
print('\n')
print('\n')