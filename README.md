# Solar System Visualizer (Pygame)

A clean, educational, and extensible **2D Solar System Visualizer** built with **Python** and **Pygame**. It simulates planet orbits around the Sun using Keplerian parameters (semi‑major axis & orbital period) scaled to screen units, with smooth rendering, zoom/pan, and a minimal in‑game HUD.

---

## ✨ Features
- Real‑time orbit simulation with configurable **time scale** (speed up/slow down).
- **Zoom** (mouse wheel) and **pan** (right‑drag) across the scene.
- Toggle **trails** and **labels**.
- Minimal **HUD** (frames per second, sim time factor, controls).
- Modular architecture (`src/` layout, tests, CI, MIT license).


## 🧰 Tech Stack
- Python 3.10+
- Pygame ≥ 2.3


## 📦 Installation
```bash
# clone
git clone https://github.com/mobinyousefi-cs/solar-system-visualizer.git
cd solar-system-visualizer

# (optional) create a venv
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# install
pip install -e .
```

Alternatively, with `pip` directly from the folder:
```bash
pip install -r requirements.txt
```


## ▶️ Run
```bash
python -m solar_system_visualizer
```
Or:
```bash
python src/solar_system_visualizer/main.py
```


## 🎮 Controls
- **Mouse Wheel**: Zoom in/out
- **Right Mouse Drag**: Pan
- **Space**: Pause / Resume
- **+ / -**: Increase / Decrease time scale
- **T**: Toggle trails
- **L**: Toggle labels
- **R**: Reset camera
- **Esc**: Quit


## 🧪 Tests
Only pure functions are unit‑tested to keep CI headless.
```bash
pytest -q
```


## 📁 Project Structure
```
solar-system-visualizer/
├─ .github/workflows/ci.yml
├─ src/
│  └─ solar_system_visualizer/
│     ├─ __init__.py
│     ├─ main.py
│     ├─ config.py
│     ├─ physics.py
│     ├─ entities.py
│     ├─ render.py
│     ├─ hud.py
│     └─ colors.py
├─ tests/
│  └─ test_physics.py
├─ .editorconfig
├─ .gitignore
├─ LICENSE
├─ pyproject.toml
└─ requirements.txt
```


## 🧪 Physics Model (Simplified)
- Each planet is approximated with a **circular/elliptical** orbit defined by:
  - semi‑major axis `a` (in astronomical units),
  - orbital period `P` (in Earth years),
  - optional eccentricity `e` and initial phase `φ0`.
- We map simulation time to **mean anomaly** and approximate position on the ellipse.
- Distances are scaled to pixels; time factor is adjustable at runtime.

This is intended for **visualization & education**, not astrophysical precision.


## 🧭 Configuration
Most knobs live in `config.py`:
- `WINDOW_SIZE`, `BACKGROUND_COLOR`, `MAX_FPS`
- `INITIAL_TIME_SCALE`, `MIN_TIME_SCALE`, `MAX_TIME_SCALE`
- Planet style defaults (colors, radii, label toggles)


## 🪲 Troubleshooting
- If the window is blank, ensure your GPU or VM supports an SDL surface.
- On Wayland/Linux, you may need `SDL_VIDEODRIVER=x11`.
- If fonts look odd, Pygame will fall back to default system fonts.


## 📜 License
MIT © 2025 Mobin Yousefi — see [LICENSE](LICENSE).


## 🙌 Credits
- Planet orbital periods & semi‑major axes inspired by canonical NASA/JPL datasets (normalized and simplified for teaching).
- Built with ❤️ for students and enthusiasts.

