#Docstring


#Example, delete this
def a_function():
    #inner function
    def an_inner_function():
        #inner funciton code; double indented
        print("This must be called to be executed")
    #singe indented, inner function code call
    an_inner_function()

def measurements(a_list):
    def area(a_list):
        pass
        #does this inner function need a return?
    def perimeter(a_list):
        pass
        #does this inner function need a return?
    pass
    #how do I call area?
    #how do I call perimeter?

    #I can use length to determine if it is a square vs rectangle

    #how do I calculate area of a square? how do I calculate area of a rectangle?
        #note: with a square, height = width; all squares are rectangles but not all rectangles are squares



#DO NOT DO THIS, these are not inner functions/nestest functions
#def area(a_list):
#    pass
#def perimeter(a_list):
#    pass

#Driver Code
if __name__ == '__main__':
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result)
    square = [3.5]
    result = measurements(square)
    print(result)
