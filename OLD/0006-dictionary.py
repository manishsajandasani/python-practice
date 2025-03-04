# The key should be unique and immutable. We can string and number both for keys.
# We can create dictionary out of two different lists using dict(zip(keyList, valueList))
# We can have nested dictionaries
# Dictionary can have anyting nested in it

data = {
    1 : 'Manish',
    2 : 'Kiran',
    10 : 'Somesh',
    'Money' : 10
}
print(data)
print(data[10])
print(data['Money'])

# print(data[3])   # Error

print(data.get(2))
print(data.get(3))
print(data.get(3, 'There is nothing'))

keys = ['A', 'B', 'C', 'D']
values = ['English', 'Hindi', 'Science', 'Maths']
data_2 = dict(zip(keys, values))
print(data_2)
print(data_2['D'])

data_2['E'] = 'EVS'
print(data_2)

del data_2["C"]
print(data_2)

progLang = {
    'JS' : {'id' : 1, 'full-form' : 'JavaScript', 'IDE' : 'Atom'},
    'C#' : {'id' : 2, 'full-form' : 'C-Sharp', 'IDE' : 'Visual Studio'},
    'PHP' : {'id' : 3, 'full-form' : 'Hypertext Preprocessor', 'IDE' : ['PHP Storm', 'VS Code']}
}
print(progLang)
print('\n')
print(progLang['JS'])
print(progLang['JS']['IDE'])
print(progLang['PHP']['IDE'])
print(progLang['PHP']['IDE'][0])