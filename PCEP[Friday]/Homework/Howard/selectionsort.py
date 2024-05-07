import time
import random
import tkinter as tk

# Function to preform Selection sort
def selection_sort(myList,canvas,delay):

    # get the size of the list
    nElements = len(myList)

    #traverse through all elements
    for i in range(nElements):
        min_index = i
        for j in range(i+1,nElements):
            if myList[j] < myList[min_index]:
                min_index = j

        #swap the found the found minimum element in the unsorted part of the array
        myList[i],myList[min_index] = myList[min_index], myList[i]

        #update the canvas with the current stat of the array
        draw_array(myList,canvas,min_index)
        canvas.update()

        time.sleep(delay)

def start_sorting():
    #generate a random array
    myList = [random.randint(5,300) for i in range(100)]
              
    #start our selection sort
    selection_sort(myList,canvas,delay_slider.get() / 1000)
    
#create function to draw the bars
def draw_array(myList,canvas,m):
    canvas.delete("all")
    bar_width = 10
    canvas_height = 300
    canvas_width = len(myList) * bar_width
    for i, val in enumerate(myList):
        x0 = i * bar_width
        y0 = canvas_height
        x1 = (i+1) * bar_width
        y1 = canvas_height - val
        canvas.create_rectangle(x0,y0,x1,y1, fill="blue")
    x0 = i * bar_width
    y0 = canvas_height
    x1 = (i+1) * bar_width
    y1 = canvas_height - val
    canvas.create_rectangle(x0,y0,x1,y1, fill="red")
    x0 = m * bar_width
    y0 = canvas_height
    x1 = (m+1) * bar_width
    y1 = canvas_height - val
    canvas.create_rectangle(x0,y0,x1,y1, fill="green")

#create the main tkinter window
root = tk.Tk()
root.title("Selection Sort Visualization")

#create the canvas to draw out our list
canvas = tk.Canvas(root,width=1000,height=300,bg="white")
canvas.pack()

#create a button to create the sorting process
start_button = tk.Button(root,text="Start Sorting", command=start_sorting)
start_button.pack()

#create a slider
delay_slider = tk.Scale(root, from_=0,to=500, orient = "horizontal", label="Delay")
delay_slider.set(100)
delay_slider.pack()

root.mainloop()
