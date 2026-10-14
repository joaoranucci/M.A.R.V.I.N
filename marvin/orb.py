"""Projected 3D wire sphere, drawn locally without an OpenGL dependency."""
import math
import tkinter as tk
import time


class Orb(tk.Canvas):
    COLORS = {'Pronto': '#48d8cf', 'Ouvindo': '#62efac', 'Pensando': '#a998ff',
              'Falando': '#56c8ff', 'Privacidade': '#738297'}

    def __init__(self, parent, state):
        super().__init__(parent, width=250, height=230, bg='#0b1524', highlightthickness=0)
        self.state = state
        self.started = time.monotonic()
        self.animate()

    def animate(self):
        if not self.winfo_exists():
            return
        self.delete('all')
        t = time.monotonic() - self.started
        mode = self.state()
        color = self.COLORS.get(mode, self.COLORS['Pronto'])
        w, h = max(250, self.winfo_width()), max(230, self.winfo_height())
        cx, cy = w / 2, h / 2 - 15
        r = min(w, h) * .33 * (1 + .035 * math.sin(t * (5 if mode == 'Falando' else 2)))
        self.create_oval(cx-r*1.2, cy+r*.78, cx+r*1.2, cy+r*1.05, fill='#102337', outline='')
        def project(lat, lon):
            x, y, z = math.cos(lat)*math.cos(lon), math.sin(lat), math.cos(lat)*math.sin(lon)
            a = t*.32
            x, z = x*math.cos(a)+z*math.sin(a), z*math.cos(a)-x*math.sin(a)
            y, z = y*.94-z*.34, z*.94+y*.34
            scale = 3 / (3-z)
            return cx+x*r*scale, cy+y*r*scale, z
        lines = []
        for lat in range(-60, 61, 20):
            pts = [project(math.radians(lat), math.radians(lon)) for lon in range(0, 361, 8)]
            for p, q in zip(pts, pts[1:]):
                lines.append(((p[2]+q[2])/2, p, q))
        for lon in range(0, 360, 30):
            pts = [project(math.radians(lat), math.radians(lon)) for lat in range(-90, 91, 8)]
            for p, q in zip(pts, pts[1:]):
                lines.append(((p[2]+q[2])/2, p, q))
        for z, p, q in sorted(lines, key=lambda line: line[0]):
            self.create_line(p[0], p[1], q[0], q[1], fill=color if z > 0 else '#20374b', width=1.5 if z>.5 else 1)
        self.create_text(cx, h-25, text=mode.upper(), fill=color, font=('Segoe UI Semibold', 11))
        self.winfo_toplevel().after(50, self.animate)
