import tkinter as tk
from tkinter import ttk, messagebox
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Ballpark data (Team Name: Distance to various zones in meters)
stadiums = {
    "Baltimore Orioles": {
        "name": "Oriole Park at Camden Yards",
        "left": 101.5, "left_center": 111, "center": 125, "right_center": 113.7, "right": 96.9
    },
    "Boston Red Sox": {
        "name": "Fenway Park",
        "left": 94.5, "left_center": 111.3, "center": 118.9, "right_center": 116.1, "right": 92.0
    },
    "New York Yankees": {
        "name": "Yankee Stadium",
        "left": 96.9, "left_center": 121.6, "center": 124.4, "right_center": 117.3, "right": 95.7
    },
    "Tampa Bay Rays": {
        "name": "Tropicana Field",
        "left": 100.6, "left_center": 116.1, "center": 121.9, "right_center": 116.1, "right": 100.6
    },
    "Toronto Blue Jays": {
        "name": "Rogers Centre",
        "left": 100.0, "left_center": 114.3, "center": 121.9, "right_center": 114.3, "right": 100.0
    },
    "Chicago White Sox": {
        "name": "Guaranteed Rate Field",
        "left": 100.6, "left_center": 114.3, "center": 121.9, "right_center": 114.3, "right": 102.1
    },
    "Cleveland Guardians": {
        "name": "Progressive Field",
        "left": 99.1, "left_center": 112.8, "center": 125, "right_center": 114.3, "right": 99.1
    },
    "Detroit Tigers": {
        "name": "Comerica Park",
        "left": 103.6, "left_center": 115.8, "center": 124.7, "right_center": 115.8, "right": 103.6
    },
    "Kansas City Royals": {
        "name": "Kauffman Stadium",
        "left": 100.6, "left_center": 118.0, "center": 125.0, "right_center": 118.0, "right": 100.6
    },
    "Minnesota Twins": {
        "name": "Target Field",
        "left": 103.3, "left_center": 115.0, "center": 123.1, "right_center": 111.9, "right": 99.7
    },
    "Houston Astros": {
        "name": "Minute Maid Park",
        "left": 96.0, "left_center": 110.3, "center": 124.7, "right_center": 113.4, "right": 99.4
    },
    "Los Angeles Angels": {
        "name": "Angel Stadium",
        "left": 100.6, "left_center": 116.4, "center": 121.9, "right_center": 111.3, "right": 100.6
    },
    "Oakland Athletics": {
        "name": "Oakland Coliseum",
        "left": 101.2, "left_center": 121.9, "center": 121.9, "right_center": 121.9, "right": 101.2
    },
    "Seattle Mariners": {
        "name": "T-Mobile Park",
        "left": 100.6, "left_center": 114.3, "center": 123.4, "right_center": 111.3, "right": 99.4
    },
    "Texas Rangers": {
        "name": "Globe Life Field",
        "left": 100.6, "left_center": 117.3, "center": 121.9, "right_center": 114.3, "right": 99.1
    },
    "Atlanta Braves": {
        "name": "Truist Park",
        "left": 102.1, "left_center": 117.3, "center": 121.9, "right_center": 114.3, "right": 99.1
    },
    "Miami Marlins": {
        "name": "LoanDepot Park",
        "left": 100.6, "left_center": 115.8, "center": 124.4, "right_center": 115.8, "right": 100.6
    },
    "New York Mets": {
        "name": "Citi Field",
        "left": 102.1, "left_center": 115.5, "center": 124.4, "right_center": 116.7, "right": 100.6
    },
    "Philadelphia Phillies": {
        "name": "Citizens Bank Park",
        "left": 100.3, "left_center": 108.2, "center": 122.2, "right_center": 108.8, "right": 100.6
    },
    "Washington Nationals": {
        "name": "Nationals Park",
        "left": 102.4, "left_center": 115.0, "center": 122.5, "right_center": 112.8, "right": 102.1
    },
    "Chicago Cubs": {
        "name": "Wrigley Field",
        "left": 108.2, "left_center": 112.2, "center": 121.9, "right_center": 112.2, "right": 107.6
    },
    "Cincinnati Reds": {
        "name": "Great American Ball Park",
        "left": 100.6, "left_center": 114.3, "center": 121.9, "right_center": 114.3, "right": 100.6
    },
    "Milwaukee Brewers": {
        "name": "American Family Field",
        "left": 104.9, "left_center": 112.8, "center": 121.9, "right_center": 114.0, "right": 102.7
    },
    "Pittsburgh Pirates": {
        "name": "PNC Park",
        "left": 99.1, "left_center": 118.6, "center": 121.6, "right_center": 111.0, "right": 97.5
    },
    "St. Louis Cardinals": {
        "name": "Busch Stadium",
        "left": 102.1, "left_center": 114.3, "center": 121.9, "right_center": 114.3, "right": 102.1
    },
    "Arizona Diamondbacks": {
        "name": "Chase Field",
        "left": 100.6, "left_center": 113.0, "center": 125.9, "right_center": 113.0, "right": 100.6
    },
    "Colorado Rockies": {
        "name": "Coors Field",
        "left": 105.8, "left_center": 118.9, "center": 126.5, "right_center": 114.3, "right": 106.7
    },
    "Los Angeles Dodgers": {
        "name": "Dodger Stadium",
        "left": 100.6, "left_center": 117.3, "center": 120.4, "right_center": 117.3, "right": 100.6
    },
    "San Diego Padres": {
        "name": "Petco Park",
        "left": 102.1, "left_center": 118.9, "center": 120.7, "right_center": 119.2, "right": 98.1
    },
    "San Francisco Giants": {
        "name": "Oracle Park",
        "left": 103.3, "left_center": 121.9, "center": 123.1, "right_center": 121.9, "right": 94.5,
    }
}

stadium_corrections = {
    "Arizona Diamondbacks": 1.02,
    "Atlanta Braves": 1.01,
    "Baltimore Orioles": 1.00,
    "Boston Red Sox": 1.00,
    "Chicago White Sox": 1.01,
    "Chicago Cubs": 1.01,
    "Cincinnati Reds": 1.01,
    "Cleveland Guardians": 1.00,
    "Colorado Rockies": 1.07,
    "Detroit Tigers": 0.99,
    "Houston Astros": 1.02,
    "Kansas City Royals": 1.00,
    "Los Angeles Angels": 1.01,
    "Los Angeles Dodgers": 0.99,
    "Miami Marlins": 0.98,
    "Milwaukee Brewers": 1.01,
    "Minnesota Twins": 1.00,
    "New York Yankees": 1.02,
    "New York Mets": 1.00,
    "Oakland Athletics": 0.99,
    "Philadelphia Phillies": 1.01,
    "Pittsburgh Pirates": 1.00,
    "San Diego Padres": 0.98,
    "San Francisco Giants": 0.98,
    "Seattle Mariners": 0.99,
    "St. Louis Cardinals": 1.01,
    "Tampa Bay Rays": 1.00,
    "Texas Rangers": 1.02,
    "Toronto Blue Jays": 1.00,
    "Washington Nationals": 1.00,
}

available_zones = {
    "左翼": "left",
    "左中間": "left_center",
    "中堅": "center",
    "右中間": "right_center",
    "右翼": "right",
}

def simulate_flight(v0, angle_deg, correction=1.0):
    g = 9.81
    dt = 0.01
    m = 0.145
    rho = 1.2
    Cd = 0.3
    A = 0.0042
    x, y = 0, 1
    angle_rad = math.radians(angle_deg)
    vx = v0 * math.cos(angle_rad)
    vy = v0 * math.sin(angle_rad)

    while y >= 0:
        v = math.sqrt(vx ** 2 + vy ** 2)
        Fd = 0.5 * Cd * rho * A * v ** 2
        ax = -Fd * (vx / v) / m
        ay = -g - (Fd * (vy / v) / m)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
    return x * correction

def find_optimal_angle(v0, correction=1.0):
    best_angle = 0
    max_distance = 0
    for angle in range(10, 60):
        d = simulate_flight(v0, angle, correction)
        if d > max_distance:
            max_distance = d
            best_angle = angle
    return best_angle, round(max_distance, 2)

def get_target_distance_by_zone(team, zone_en):
    key = available_zones.get(zone_en, "center")
    return stadiums[team][key]

def get_correction_factor(direction, handedness):
    if direction in ["Center", "Left Center", "Right Center"]:
        return 1.0
    if handedness == "Right":
        return 1.03 if direction == "Left Field" else 0.97 if direction == "Right Field" else 1.0
    else:
        return 1.03 if direction == "Right Field" else 0.97 if direction == "Left Field" else 1.0

def get_total_correction(team, direction, handedness):
    base = get_correction_factor(direction, handedness)
    stadium_corr = stadium_corrections.get(team, 1.00)
    return base * stadium_corr

def plot_trajectory(v0, angle_deg, canvas_frame):
    g = 9.81
    dt = 0.01
    m = 0.145
    rho = 1.2
    Cd = 0.3
    A = 0.0042
    x, y = 0, 1
    angle_rad = math.radians(angle_deg)
    vx = v0 * math.cos(angle_rad)
    vy = v0 * math.sin(angle_rad)

    x_vals = [x]
    y_vals = [y]

    while y >= 0:
        v = math.sqrt(vx ** 2 + vy ** 2)
        Fd = 0.5 * Cd * rho * A * v ** 2
        ax = -Fd * (vx / v) / m
        ay = -g - (Fd * (vy / v) / m)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        if y < 0: break
        x_vals.append(x)
        y_vals.append(y)

    for widget in canvas_frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(x_vals, y_vals)
    ax.set_title("Hit Trajectory")
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Height (m)")
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def on_calculate():
    team = team_var.get()
    zone = direction_var.get()
    handedness = handedness_var.get()
    try:
        v = float(speed_entry.get())
    except:
        messagebox.showerror("Input Error", "Ball speed must be a number")
        return

    if team not in stadiums:
        messagebox.showerror("Error", "Invalid team name")
        return

    d = get_target_distance_by_zone(team, zone)
    correction = get_total_correction(team, zone, handedness)
    optimal_angle, max_d = find_optimal_angle(v, correction)

    result = f"Stadium: {team} ({stadiums[team]['name']})\n"
    result += f"Target Zone: {zone} ({d} m)\n"
    result += f"Batter: {handedness}\n"
    result += f"Optimal Angle: {optimal_angle} degrees\nDistance (Corrected): {max_d} m\n"

    if max_d >= d:
        result += "\u2192 Home Run!"
    else:
        result += "\u2192 Not far enough."

    result_label.config(text=result)
    plot_trajectory(v, optimal_angle, graph_frame)

# GUI Layout
root = tk.Tk()
root.title("Home Run Simulator (with Graph)")

tk.Label(root, text="Team:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
team_var = tk.StringVar()
team_combo = ttk.Combobox(root, textvariable=team_var, values=list(stadiums.keys()), width=30)
team_combo.grid(row=0, column=1, padx=5, pady=5)
team_combo.set("New York Yankees")

tk.Label(root, text="Target Zone:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
direction_var = tk.StringVar(value="Center")
direction_menu = ttk.Combobox(root, textvariable=direction_var, values=list(available_zones.keys()), width=15)
direction_menu.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Batter Side:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
handedness_var = tk.StringVar(value="Right")
handedness_menu = ttk.Combobox(root, textvariable=handedness_var, values=["Right", "Left"], width=10)
handedness_menu.grid(row=1, column=3, padx=5, pady=5)

tk.Label(root, text="Initial Speed (m/s):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
speed_entry = tk.Entry(root)
speed_entry.grid(row=2, column=1, padx=5, pady=5)

calc_btn = tk.Button(root, text="Calculate", command=on_calculate)
calc_btn.grid(row=3, column=0, columnspan=4, pady=10)

result_label = tk.Label(root, text="Results will appear here", justify="left")
result_label.grid(row=4, column=0, columnspan=4, pady=10)

# Graph Area
graph_frame = tk.Frame(root)
graph_frame.grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()
