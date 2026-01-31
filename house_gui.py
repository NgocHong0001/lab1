import tkinter as tk
import json

HOUSE_FILE = "house.json"

def load_house_state():
    with open(HOUSE_FILE, 'r') as f:
        data = json.load(f)
    return data

#return a color for each obj. based on state.
def get_colors(state:dict):
    #light
    if state.get("light") == "on":
        light_color = "yellow"
    else:
        light_color= "gray"

    #door
    if state.get("door") == "open":
        door_color = "green"
    else:
        door_color = "red"

    #window
    if state.get("window") == "open":
        window_color = "lightblue"
    else:
        window_color = "darkblue"
    return light_color, door_color, window_color

def draw_house(canvas, state):
    canvas.delete("all") #clear prev. drawings

    light_color, door_color, window_color = get_colors(state)

    # circle - light
    canvas.create_oval(50, 50, 150, 150, fill=light_color, outline="black")
    canvas.create_text(100, 160, text=f"Light: {state.get('light')}", font=("Arial", 10))

    #triangle - door
    canvas.create_polygon(
        250, 150, #top point
        200, 250, #bottom left
        300, 250, #bottom right
        fill=door_color, outline="black"
    )
    canvas.create_text(250, 260, text=f"Door: {state.get('door')}", font=("Arial", 10))

    # square - window
    canvas.create_rectangle(400, 100, 500, 200, fill=window_color, outline="black")
    canvas.create_text(450, 210, text=f"Window: {state.get('window')}", font=("Arial", 10))

def main():
  state = load_house_state()

  root = tk.Tk()
  root.title("House State (Server Side)")

  canvas = tk.Canvas(root, width=600, height=300, bg="white")
  canvas.pack(padx=10, pady=10)

#loop to refresh every 0.5 seconds to reflect any changes
  def refresh():
      state = load_house_state()
      draw_house(canvas, state)
      root.after(500, refresh)
      
  refresh()
  
  root.mainloop()


if __name__ == "__main__":
  main()