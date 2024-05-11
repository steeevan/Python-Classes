import tkinter as tk
import random
import math

def start_animation(root, canvas, speed_scale, num_balls_entry):
    speed = speed_scale.get()
    num_balls = int(num_balls_entry.get())
    balls = generate_balls(canvas, speed, num_balls)
    move_balls(root, canvas, balls, speed)

def generate_balls(canvas, speed, num_balls):
    balls = []
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    for _ in range(num_balls):
        x = random.randint(10, canvas_width - 10)
        y = random.randint(10, canvas_height - 10)
        radius = random.randint(5, 20)
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        angle = random.uniform(0, 2 * math.pi)
        velocity_x = speed * math.cos(angle)
        velocity_y = speed * math.sin(angle)

        ball = {'id': canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color),
                'x': x, 'y': y, 'radius': radius, 'color': color,
                'velocity_x': velocity_x, 'velocity_y': velocity_y}
        balls.append(ball)
    return balls

def move_balls(root, canvas, balls, speed):
    for ball in balls:
        move_ball(root, canvas, ball, speed)

def move_ball(root, canvas, ball, speed):
    ball['x'] += ball['velocity_x']
    ball['y'] += ball['velocity_y']
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    if ball['x'] <= 0 or ball['x'] >= canvas_width:
        ball['velocity_x'] *= -1
        # Uncomment the following section to change ball color when hitting edges
        # ball['color'] = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        # canvas.itemconfig(ball['id'], fill=ball['color'])
    if ball['y'] <= 0 or ball['y'] >= canvas_height:
        ball['velocity_y'] *= -1
        # Uncomment the following section to change ball color when hitting edges
        # ball['color'] = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        # canvas.itemconfig(ball['id'], fill=ball['color'])

    canvas.move(ball['id'], ball['velocity_x'], ball['velocity_y'])
    root.after(1000//speed, move_ball, root, canvas, ball, speed)

def main():
    root = tk.Tk()
    root.title("Random Data Visualization")
    root.configure(bg='black')

    canvas = tk.Canvas(root, width=600, height=400, bg='black')
    canvas.pack()

    speed_label = tk.Label(root, text="Speed:", bg='black', fg='white')
    speed_label.pack()
    speed_scale = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, bg='black', fg='white')
    speed_scale.pack()

    num_balls_label = tk.Label(root, text="Number of Balls:", bg='black', fg='white')
    num_balls_label.pack()
    num_balls_entry = tk.Entry(root, bg='black', fg='white')
    num_balls_entry.pack()

    start_button = tk.Button(root, text="Start", command=lambda: start_animation(root, canvas, speed_scale, num_balls_entry), bg='black', fg='white')
    start_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
