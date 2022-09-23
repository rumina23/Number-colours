# Empty List
numbers = []

#Read from the text file
with open('./numbers.txt', 'r') as read_file:
  for line in read_file:
    numbers.append(int(line))


#print(numbers)
numbers.sort() #Sorting the Array.
#print(numbers)

#Dictionary to hold the count of the numbers.
number_count = {}

for number in numbers:
  if number in number_count:  #Check if number exists in dictionary
    number_count[number] += 1 #Number already exists.
  else:
    number_count[number] = 1

#print(number_count)   #Printing the dictionary.

#Check which number exists the most.
max_count = 0
max_number = 0

#Check
for number, count in number_count.items():
  if count > max_count:
    max_count = count
    max_number = number

print(f'The number {max_number} exists {max_count} times!')
#Numbers Code Done


# Colors Code.
#Reading colours.txt using with open()
#Read colours.txt using Python
#Create an empty list
colors = []
samecolorLines = 0
diffColorLines = 0

with open('./colours.txt', 'r') as read_file:
    #Check which color exists most and which does not exists    
    for line in read_file:
        #Count which color appears most in the file
        # colors.append(line.strip())
        line = line.strip()
        #Append all three colors in a line seperated by a comma
        newArr = line.split(',')
        #Count how many newArr have all different values
        if (newArr[0] == newArr[1]) and (newArr[1] == newArr[2]):
          samecolorLines += 1

        if ((newArr[0] != newArr[1]) and (newArr[1] != newArr[2])):
            diffColorLines += 1
      
        for color in newArr:
            colors.append(color.strip())
      

# print(colors)
#Sort Colors
colors.sort()
#print(colors)


#Check in colors list which color exists most
#Create a dictionary to store the color and its count
color_count = {}

for color in colors:
    if color in color_count:
        color_count[color] += 1
    else:
        color_count[color] = 1

#print(color_count)
#Check which color exists most
max_count = 0
max_color = ''

#Checks which color exists most
for color, count in color_count.items():
    if count > max_count:
        max_count = count
        max_color = color

#print(color_count)
print(f'The color {max_color} exists {max_count} times')
print(f'Same colors occured {samecolorLines} times')
print(f'Different colors occured {diffColorLines} times')