import tkinter as tk
from PIL import Image, ImageTk

TILE = 48

level1 = [
    "##########",
    "#P....#..#",
    "#..##.#K.#",
    "#.##..#..#",
    "#..##..#.#",
    "##....#.D#",
    "##########"
]
level2 = [
    "##########",
    "#P....#..#",
    "#..##K#..#",
    "#.##..#..#",
    "#......#D#",
    "##########",
]
levels = [level1, level2]
current_level = 0

root = tk.Tk()
root.title("Grid Adventure")

# Create a canvas (dimensions will be configured dynamically in load_level)
canvas = tk.Canvas(root)
canvas.pack()

# 1. Define the paths for your assets
image_paths = {
    'floor': "tiles/floor.png",
    'wall': "tiles/wall.png",
    'player': "tiles/player.png",
    'key': "tiles/key.png",
    'door_locked': "tiles/door_locked.png",
    'door_open': "tiles/door_open.png"
}

# 2. Load, resize, and store them in the 'images' dictionary
images = {}
for key, path in image_paths.items():
    try:
        img = Image.open(path)
        img = img.resize((TILE, TILE), Image.Resampling.LANCZOS)
        images[key] = ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Warning: Could not load {path} - {e}")

# Global state variables
game_map = []
player_r = 0
player_c = 0
has_key = False
ROWS = 0
COLS = 0

def load_level(index):
    global game_map, player_r, player_c, has_key, ROWS, COLS
    
    if index >= len(levels):
        print("Congratulations, you finished all levels!")
        root.quit()
        return

    has_key = False
    game_map = []

    for row_text in levels[index]:
        game_map.append(list(row_text))
        
    ROWS = len(game_map)
    COLS = len(game_map[0])
    
    # Adjust canvas size automatically for the current level
    canvas.config(width=COLS*TILE, height=ROWS*TILE)

    for r in range(ROWS):
        for c in range(COLS):
            if game_map[r][c] == "P":
                player_r, player_c = r, c
                game_map[r][c] = "."

def load_map(maps):
    """Utility to load a map from a file (Fixed indentation & added valid chars)"""
    with open(maps, 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    if len(lines) == 0:
        raise ValueError('Map is empty')

    width = len(lines[0])
    for line in lines:
        if len(line) != width:
            raise ValueError('Map is not rectangular')
    
    allowed = set('#.PKD') # Added Keys and Doors to allowed sets
    p_count = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            ch = lines[r][c]
            # Fixed indentation error block
            if ch not in allowed:
                raise ValueError(f"Invalid character '{ch}' at ({r}, {c})")
            if ch == 'P':
                p_count += 1
                
    if p_count != 1:
        raise ValueError('Map must contain exactly one player')
    return lines

def draw_tile(r, c, key):
    # Ensure this key exists in 'images' before creating to avoid crashing if images are missing
    if key in images:
        x = c * TILE
        y = r * TILE
        canvas.create_image(x, y, image=images[key], anchor="nw")

def draw_world():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            ch = game_map[r][c]
            
            # Draw base layers (walls and floors)
            if ch == '#':
                draw_tile(r, c, 'wall')
            else:
                draw_tile(r, c, 'floor')
                
            # Draw overlays
            if ch == 'K':
                draw_tile(r, c, 'key')
            elif ch == 'D':
                if has_key:
                    draw_tile(r, c, 'door_open')
                else:
                    draw_tile(r, c, 'door_locked')
                    
    draw_tile(player_r, player_c, 'player')

def try_move(dr, dc):
    global player_r, player_c, has_key, current_level
    nr = player_r + dr
    nc = player_c + dc

    # Bounds safety
    if not (0 <= nr < ROWS and 0 <= nc < COLS):
        return
    
    target_tile = game_map[nr][nc]
    
    # Check Wall Collision
    if target_tile == "#":
        return
        
    # Check Door Logic
    if target_tile == "D":
        if not has_key:
            return # Blocked by locked door
        else:
            current_level += 1
            load_level(current_level)
            if current_level < len(levels):
                draw_world()
            return

    # Check Key Logic
    if target_tile == "K":
        has_key = True
        game_map[nr][nc] = "." # Remove key from map
    
    # Update Player position
    player_r = nr
    player_c = nc
    draw_world()

def on_key(event):
    if event.keysym == "Up":
        try_move(-1, 0)
    elif event.keysym == "Down":
        try_move(1, 0)
    elif event.keysym == "Left":
        try_move(0, -1)
    elif event.keysym == "Right":
        try_move(0, 1)

# Initialize and draw the game
load_level(current_level)
draw_world()

root.bind("<Key>", on_key)
root.mainloop()
