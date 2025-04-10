# Home Run Simulator (English Version)

This Python application simulates whether a batted ball would result in a home run based on its velocity, angle, batter's handedness, target zone, and ballpark environment.

---

## 🎯 Features

- Full MLB stadium data (LF/LC/CF/RC/RF distances for 30 teams)
- Batter-direction correction factors (e.g., pull-side power)
- Ballpark-specific correction factors (e.g., Coors Field altitude)
- Automatic search for optimal launch angle (10° to 59°)
- Real-time trajectory visualization using matplotlib
- Tkinter-based GUI (English)

---

## 🔧 Known Issues & Improvement Suggestions

- [ ] The graph currently plots the uncorrected trajectory; could be updated to reflect the corrected distance.
- [ ] Visual fence lines or thresholds could help indicate home run cutoffs.
- [ ] Could integrate real-world variables like altitude, temperature, wind, and humidity.
- [ ] Adding wall height per zone would increase realism.
- [ ] Future version: Link with real player Statcast data for personalized simulations.

---

## 🧪 How to Use

1. Run the script and enter the following:
   - MLB team (e.g., New York Yankees)
   - Target zone (e.g., Left Field, Center)
   - Batter's handedness (Right / Left)
   - Exit velocity (e.g., 160 m/s)
2. Click “Calculate” to view:
   - Optimal launch angle and corrected flight distance
   - Home run status (yes/no)
   - Trajectory graph (currently uncorrected)

---

## 🧰 Requirements

- Python 3.7+
- matplotlib
- tkinter (bundled with Python)

---

## 📁 File Structure

- `ballpark_home_run_calculator_english.py`: English version of the GUI simulator
- Includes: Distance data and correction factors for all 30 MLB ballparks

---

## 👤 Author

Seiya Genda
