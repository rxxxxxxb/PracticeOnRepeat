
# Use for, .split(), and if to create a Statement that will print out words that start with 's'

st = 'Print only the words that start with s in this sentence'


for word in st.split():
    if word[0] == 's':
        print(word)

# even number using range

li = list(range(1,15,2))  
print(li) 

#List comprehension to create a list of number devisible by 3

div3 = [x for x in range(1,50) if x%3 == 0 ]
print(div3)


#using list comprehension for 1st letter in every word
firstLetter = [word[0] for word in st.split()]

print(firstLetter)