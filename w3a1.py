import math

#set the length for the fence with user input. tSide is the side
#length for an equilateral triangle.
length = float(input("\nPlease enter the length of your fence.\n"))
print("\nLength is", length)
tSide = length / 3

#calculate the area via the math sqrt module.
#it rounds the output to two decimal places as to not
#clutter the terminal.
tArea = round(math.sqrt(3) / 4 * tSide * tSide, 2)
print("Area for triangle fence with given length is: ", tArea)

#makes the width of the rectangle 10% of the length,
#and makes the length of the rectangle 40% of the fence length.
rLength = .4 * length
rWidth = .1 * length

#calculates area of the rectangle and prints to the terminal.
rArea = rLength * rWidth
print("Area for rectangle fence with given length is: ", rArea)

#sets the side length variable for the square, calculates the area,
#and displays it to the terminal.
sLength = length / 4
sArea = sLength * sLength
print("Area for square fence with given length is: ", sArea)

#calculates the radius of the circle from the fence length/circumfrence (uses math.pi for pi)
#calculates the area from the radius
radius = length / math.pi / 2
cArea = round(radius * radius * math.pi, 2)

#prints the output rounded to two decimal places for clutter
print("Area for circle fence with given length is: ", cArea, "\n")

#makes a list with all the areas.
#finds the largest number in the list.
#sets a variable to the name of the largest area shape.
largestList = [tArea, rArea, sArea, cArea]
largestNum = max(largestList)
if largestNum == cArea:
    largest = "circle"
elif largestNum == tArea:
    largest = "triangle"
elif largestNum == rArea:
    largest = "rectangle"
elif largestNum == sArea:
    largest = "square"

#prints the shape with the largest area.
print("The best fence shape with the most area is the", largest, "\n")