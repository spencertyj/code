import tkinter as tk
import random
game_over = False
after_id = None
root = tk.Tk()
root.title("Snake - 1")
SIZE = 15
W = 1300
H = 600
canvas= tk.Canvas(root, width=W, height=H, bg="white")
canvas.pack()
snake = [(10, 10)]
dx = 1
dy = 0
max_x = W // SIZE
max_y = H // SIZE
status_label = tk.Label(root, text="")
food = (random.randint(0, W//SIZE - 1),
random.randint(0, H//SIZE - 1))
score = 0
score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack()
def draw():
    canvas.delete("all")
    fx, fy = food
    canvas.create_rectangle(fx*SIZE, fy*SIZE,
                            fx*SIZE+SIZE, fy*SIZE+SIZE,
                            fill="red")
    
    for (x, y) in snake:
        canvas.create_rectangle(x*SIZE, y*SIZE,
                                x*SIZE+SIZE, y*SIZE+SIZE,
                                fill="green")
def game_loop():
    global snake, food, game_over, after_id,score
    if game_over == True:
        return
    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)
    if new_head[0] < 0 or new_head[0] >=  max_x or \
        new_head[1] < 0 or new_head[1] >= max_y:
        print("game over")
        game_over =True
        return
    if new_head in snake:
        game_over = True
        return
    snake.insert(0, new_head)
    if new_head == food:
        food = (random.randint(0, W//SIZE - 1),
            random.randint(0, H//SIZE - 1))
        score+= 1
        score_label.config(text=f"Score: {score}")
    else:
        snake.pop()
    draw()
    if after_id:
        root.after_cancel(after_id)
    after_id = root.after(65, game_loop)
def restart():
    global snake, dx, dy, food, game_over, after_id, score
    snake = [(10,10)]
    dx, dy = 1, 0
    food = (random.randint(0, max_x - 1),
            random.randint(0, max_y - 1))
    game_over = False
    score = 0 
    status_label.config(text=f"Score: {score}")
    draw()
    if after_id:
        root.after_cancel(after_id)
        print("cancel in restart")
    after_id = root.after(10, game_loop)
restart_btn = tk.Button(root, text="Restart", command=restart)
restart_btn.pack(pady=5)
status_label.pack()
def up(event):
    global dx, dy
    dx, dy = 0, -1
def down(event):
    global dx, dy
    dx, dy = 0, 1
def left(event):
    global dx, dy
    dx, dy = -1, 0
def right(event):
    global dx, dy
    dx, dy = 1, 0
root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Left>", left)
root.bind("<Right>", right)
draw()
if after_id:
    root.after_cancel(after_id)
    print("cancel in end")
after_id = root.after(150, game_loop)
root.mainloop()
