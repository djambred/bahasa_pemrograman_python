import array as arr 

#original array
numbers = arr.array('i',[10,20,30])

#change the first element
#change it from having a value of 10 to having a value of 40
numbers[0] = 40

print(numbers)



#add
import array as arr 

#original array
numbers = arr.array('i',[10,20,30])

#add the integer 40 to the end of numbers
numbers.append(40)

print(numbers)

#float
import array as arr 

#original array
numbers = arr.array('f',[10,20,30])

#add the integer 40 to the end of numbers
numbers.append(40.0)

print(numbers)


#extend
import array as arr 

#original array
numbers = arr.array('i',[10,20,30])

#add the integers 40,50,60 to the end of numbers
#The numbers need to be enclosed in square brackets

numbers.extend([40,50,60])

print(numbers)


#insert
import array as arr 

#original array
numbers = arr.array('i',[10,20,30])

#add the integer 40 in the first position
#remember indexing starts at 0

numbers.insert(0,40)

print(numbers)


#remove
import array as arr 

#original array
numbers = arr.array('i',[10,20,30])

numbers.remove(10)

print(numbers)

#pop
import array as arr 

#original array
numbers = arr.array('i',[10,20,30,10,20])

#remove the first instance of 10
numbers.pop(0)

print(numbers)