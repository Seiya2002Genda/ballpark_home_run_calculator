import tkinter as tk
from tkinter import ttk, messagebox
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

stadiums = {
    "ボルチモア・オリオールズ": {
        "name": "オリオール・パーク・アット・カムデンヤーズ",
        "left": 101.5, "left_center": 111, "center": 125, "right_center": 113.7, "right": 96.9
    },
    "ボストン・レッドソックス": {
        "name": "フェンウェイ・パーク",
        "left": 94.5, "left_center": 111.3, "center": 118.9, "right_center": 116.1, "right": 92.0
    },
    "ニューヨーク・ヤンキース": {
        "name": "ヤンキー・スタジアム",
        "left": 96.9, "left_center": 121.6, "center": 124.4, "right_center": 117.3, "right": 95.7
    },
    "タンパベイ・レイズ": {
        "name": "トロピカーナ・フィールド",
        "left": 100.6, "left_center": 116.1, "center": 121.9, "right_center": 116.1, "right": 100.6
    },
    "トロント・ブルージェイズ": {
        "name": "ロジャーズ・センター",
        "left": 100.0, "left_center": 114.3, "center": 121.9, "right_center": 114.3, "right": 100.0
    },
    "シカゴ・ホワイトソックス": {
        "name": "ギャランティード・レート・フィールド",
        "left": 100.6, "left_center": 114.3, "center": 121.9, "right_center": 114.3, "right": 102.1
    },
    "クリーブランド・ガーディアンズ": {
        "name": "プログレッシブ・フィールド",
        "left": 99.1, "left_center": 112.8, "center": 125, "right_center": 114.3, "right": 99.1
    },
    "デトロイト・タイガース": {
        "name": "コメリカ・パーク",
        "left": 103.6, "left_center": 115.8, "center": 124.7, "right_center": 115.8, "right": 103.6
    },
    "カンザスシティ・ロイヤルズ": {
        "name": "カウフマン・スタジアム",
        "left": 100.6, "left_center": 118.0, "center": 125.0, "right_center": 118.0, "right": 100.6
    },
    "ミネソタ・ツインズ": {
        "name": "ターゲット・フィールド",
        "left": 103.3, "left_center": 115.0, "center": 123.1, "right_center": 111.9, "right": 99.7
    },
    "ヒューストン・アストロズ": {
        "name": "ミニッツメイド・パーク",
        "left": 96.0, "left_center": 110.3, "center": 124.7, "right_center": 113.4, "right": 99.4
    },
    "ロサンゼルス・エンゼルス": {
        "name": "エンゼル・スタジアム",
        "left": 100.6, "left_center": 116.4, "center": 121.9, "right_center": 111.3, "right": 100.6
    },
    "オークランド・アスレチックス": {
        "name": "オークランド・コロシアム",
        "left": 101.2, "left_center": 121.9, "center": 121.9, "right_center": 121.9, "right": 101.2
    },
    "シアトル・マリナーズ": {
        "name": "T-モバイル・パーク",
        "left": 100.6, "left_center": 114.3, "center": 123.4, "right_center": 111.3, "right": 99.4
    },
    "テキサス・レンジャーズ": {
        "name": "グローブライフ・フィールド",
        "left": 100.6, "left_center": 117.3, "center": 121.9, "right_center": 114.3, "right": 99.1
    },
    "アトランタ・ブレーブス": {
        "name": "トゥルーイスト・パーク",
        "left": 102.1, "left_center": 117.3, "center": 121.9, "right_center": 114.3, "right": 99.1
    },
    "マイアミ・マーリンズ": {
        "name": "ローンデポ・パーク",
        "left": 100.6, "left_center": 115.8, "center": 124.4, "right_center": 115.8, "right": 100.6
    },
    "ニューヨーク・メッツ": {
        "name": "シティ・フィールド",
        "left": 102.1, "left_center": 115.5, "center": 124.4, "right_center": 116.7, "right": 100.6
    },
    "フィラデルフィア・フィリーズ": {
        "name": "シチズンズ・バンク・パーク",
        "left": 100.3, "left_center": 108.2, "center": 122.2, "right_center": 108.8, "right": 100.6
    },
    "ワシントン・ナショナルズ": {
        "name": "ナショナルズ・パーク",
        "left": 102.4, "left_center": 115.0, "center": 122.5, "right_center": 112.8, "right": 102.1
    },
    "シカゴ・カブス": {
        "name": "リグレー・フィールド",
        "left": 108.2, "left_center": 112.2, "center": 121.9, "right_center": 112.2, "right": 107.6
    },
    "シンシナティ・レッズ": {
        "name": "グレート・アメリカン・ボール・パーク",
        "left": 100.6, "left_center": 114.3, "center": 121.9, "right_center": 114.3, "right": 100.6
    },
    "ミルウォーキー・ブルワーズ": {
        "name": "アメリカン・ファミリー・フィールド",
        "left": 104.9, "left_center": 112.8, "center": 121.9, "right_center": 114.0, "right": 102.7
    },
    "ピッツバーグ・パイレーツ": {
        "name": "PNCパーク",
        "left": 99.1, "left_center": 118.6, "center": 121.6, "right_center": 111.0, "right": 97.5
    },
    "セントルイス・カージナルス": {
        "name": "ブッシュ・スタジアム",
        "left": 102.1, "left_center": 114.3, "center": 121.9, "right_center": 114.3, "right": 102.1
    },
    "アリゾナ・ダイヤモンドバックス": {
        "name": "チェイス・フィールド",
        "left": 100.6, "left_center": 113.0, "center": 125.9, "right_center": 113.0, "right": 100.6
    },
    "コロラド・ロッキーズ": {
        "name": "クアーズ・フィールド",
        "left": 105.8, "left_center": 118.9, "center": 126.5, "right_center": 114.3, "right": 106.7
    },
    "ロサンゼルス・ドジャース": {
        "name": "ドジャー・スタジアム",
        "left": 100.6, "left_center": 117.3, "center": 120.4, "right_center": 117.3, "right": 100.6
    },
    "サンディエゴ・パドレス": {
        "name": "ペトコ・パーク",
        "left": 102.1, "left_center": 118.9, "center": 120.7, "right_center": 119.2, "right": 98.1
    },
    "サンフランシスコ・ジャイアンツ": {
        "name": "オラクル・パーク",
        "left": 103.3, "left_center": 121.9, "center": 123.1, "right_center": 121.9, "right": 94.5,
    }
}

stadium_corrections = {
    "アリゾナ・ダイヤモンドバックス": 1.02,
    "アトランタ・ブレーブス": 1.01,
    "ボルチモア・オリオールズ": 1.00,
    "ボストン・レッドソックス": 1.00,
    "シカゴ・ホワイトソックス": 1.01,
    "シカゴ・カブス": 1.01,
    "シンシナティ・レッズ": 1.01,
    "クリーブランド・ガーディアンズ": 1.00,
    "コロラド・ロッキーズ": 1.07,
    "デトロイト・タイガース": 0.99,
    "ヒューストン・アストロズ": 1.02,
    "カンザスシティ・ロイヤルズ": 1.00,
    "ロサンゼルス・エンゼルス": 1.01,
    "ロサンゼルス・ドジャース": 0.99,
    "マイアミ・マーリンズ": 0.98,
    "ミルウォーキー・ブルワーズ": 1.01,
    "ミネソタ・ツインズ": 1.00,
    "ニューヨーク・ヤンキース": 1.02,
    "ニューヨーク・メッツ": 1.00,
    "オークランド・アスレチックス": 0.99,
    "フィラデルフィア・フィリーズ": 1.01,
    "ピッツバーグ・パイレーツ": 1.00,
    "サンディエゴ・パドレス": 0.98,
    "サンフランシスコ・ジャイアンツ": 0.98,
    "シアトル・マリナーズ": 0.99,
    "セントルイス・カージナルス": 1.01,
    "タンパベイ・レイズ": 1.00,
    "テキサス・レンジャーズ": 1.02,
    "トロント・ブルージェイズ": 1.00,
    "ワシントン・ナショナルズ": 1.00,
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


def get_target_distance_by_zone(team, zone_jp):
    key = available_zones.get(zone_jp, "center")
    return stadiums[team][key]

def get_correction_factor(direction, handedness):
    if direction in ["中堅", "左中間", "右中間"]:
        return 1.0
    if handedness == "右打者":
        return 1.03 if direction == "左翼" else 0.97 if direction == "右翼" else 1.0
    else:  # 左打者
        return 1.03 if direction == "右翼" else 0.97 if direction == "左翼" else 1.0

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
    ax.set_title("打球軌道")
    ax.set_xlabel("飛距離 (m)")
    ax.set_ylabel("高さ (m)")
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
        messagebox.showerror("入力エラー", "球速は数値で入力してください")
        return

    if team not in stadiums:
        messagebox.showerror("エラー", "球団名が無効です")
        return

    d = get_target_distance_by_zone(team, zone)

    # 🔧 修正ここ！
    correction = get_total_correction(team, zone, handedness)

    optimal_angle, max_d = find_optimal_angle(v, correction)

    result = f"球場: {team}（{stadiums[team]['name']}）\n"
    result += f"狙う位置: {zone}（{d} m）\n"
    result += f"打者: {handedness}\n"
    result += f"最適角度: {optimal_angle} 度\n飛距離（補正後）: {max_d} m\n"

    if max_d >= d:
        result += "→ ホームラン可能！"
    else:
        result += "→ 届かず…"

    result_label.config(text=result)
    plot_trajectory(v, optimal_angle, graph_frame)

# GUIレイアウト
root = tk.Tk()
root.title("Home Run Simulator(with Graph)")

tk.Label(root, text="球団名:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
team_var = tk.StringVar()
team_combo = ttk.Combobox(root, textvariable=team_var, values=list(stadiums.keys()), width=30)
team_combo.grid(row=0, column=1, padx=5, pady=5)
team_combo.set("ニューヨーク・ヤンキース")

tk.Label(root, text="狙う位置:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
direction_var = tk.StringVar(value="中堅")
direction_menu = ttk.Combobox(root, textvariable=direction_var, values=list(available_zones.keys()), width=10)
direction_menu.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="打者の利き手:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
handedness_var = tk.StringVar(value="右打者")
handedness_menu = ttk.Combobox(root, textvariable=handedness_var, values=["右打者", "左打者"], width=10)
handedness_menu.grid(row=1, column=3, padx=5, pady=5)

tk.Label(root, text="打球初速度 (m/s):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
speed_entry = tk.Entry(root)
speed_entry.grid(row=2, column=1, padx=5, pady=5)

calc_btn = tk.Button(root, text="計算する", command=on_calculate)
calc_btn.grid(row=3, column=0, columnspan=4, pady=10)

result_label = tk.Label(root, text="ここに結果が表示されます", justify="left")
result_label.grid(row=4, column=0, columnspan=4, pady=10)

# グラフ表示エリア
graph_frame = tk.Frame(root)
graph_frame.grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()
