import os
import re
import pandas

excel_data_df = pandas.read_excel('Book1.xlsx', sheet_name='Sheet1', usecols=['Heading','Text1','Text2','Text3'])

# print('Excel Sheet to Dict:', excel_data_df.to_dict(orient='record'))

Content  = excel_data_df.to_dict(orient='record')
print("Choose a Argument to update -")
for i in Content:
    print(i['Heading'])


Heading  = input('Enter a heading to update:')

for i in Content:
    if(i['Heading']==Heading):
        Text1 = (i['Text1'])
        Text2 = (i['Text2'])
        Text3 = (i['Text3'])


folder = "C:\\Users\\HP\\Desktop\\NLG Variations"

for filename in os.listdir(folder):
    
    infilename = os.path.join(folder,filename)
    base,ext = os.path.splitext(filename)
    newfilename = os.path.join(folder,base)
    
    if(base == 'Dialogs' and ext == '.bxb'):
        os.rename(infilename,newfilename + '.txt')
        print(newfilename + '.txt')



print("\tText in the file before update-")

with open("Dialogs.txt",'r+') as file:
    text = file.read()

print(text)

pattern = re.compile(r'''template-macro-def \('''+Heading+'''\){
	content{
		choose \(Random\){
			template \("(.*)"\)
			template \("(.*)"\)
			template \("(.*)"\)
		}
	}
}''',re.M)

matches = pattern.finditer(text)

for match in matches:
    print(match)
    
k = match.group()
# print(k)
p = match.groups()

pattern1 = re.compile(p[0])
pattern2 = re.compile(p[1])
pattern3 = re.compile(p[2])

k = pattern1.sub(Text1,k)
k = pattern2.sub(Text2,k)
k = pattern3.sub(Text3,k)

text = pattern.sub(k,text)

print("\tText after update")
print(text)

for filename in os.listdir(folder):
    
    infilename = os.path.join(folder,filename)
    base,ext = os.path.splitext(filename)
    newfilename = os.path.join(folder,base)
    
    if(base == 'Dialogs' and ext == '.txt'):
        os.rename(infilename,newfilename + '.bxb')
        print(newfilename + '.bxb')