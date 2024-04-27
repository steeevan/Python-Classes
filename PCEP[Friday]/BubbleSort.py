import tkinter as tk
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                update_bars(arr)
                root.update()
                time.sleep(.1)



def update_bars(arr):
    canvas.delete("all")
    bar_width = canvas_width / len(arr)
    for i, height in enumerate(arr):
        x0 = i * bar_width
        y0 = canvas_height - height * canvas_height / max(arr)
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        
        canvas.create_rectangle(x0,y0,x1,y1,fill="blue")


def start_sorting():
    global arr
    random.shuffle(arr)
    bubble_sort(arr)


    
# generate our random list
'''
arr = []
for i in range(20):
    arr.append(random.randint(1,15))
'''

n = 20
arr = [i+1 for i in range(n)]
random.shuffle(arr)


root = tk.Tk()
root.title("Bubble Sort Visualization")

canvas_width = 800
canvas_height = 400

canvas = tk.Canvas(root,width=canvas_width,height = canvas_height)
canvas.pack()

sort_button = tk.Button(root, text="Start Sorting", command= start_sorting)
sort_button.pack()

root.mainloop()









