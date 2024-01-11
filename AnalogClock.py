import tkinter as tk
import math
import time

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Analog Clock")
        self.canvas = tk.Canvas(root, width=800, height=800, bg="white")
        self.canvas.pack(expand=True, fill=tk.BOTH)
        self.radius = 380
        self.center_x = 400
        self.center_y = 400
        self.draw_face()
        self.update_clock()

    def draw_face(self):
        for i in range(60):
            angle = math.radians(i * 6)
            x1 = self.center_x + self.radius * math.cos(angle)
            y1 = self.center_y - self.radius * math.sin(angle)
            if i % 5 == 0:
                x2 = x1 - 15 * math.cos(angle)
                y2 = y1 + 15 * math.sin(angle)
                self.canvas.create_line(x1, y1, x2, y2, width=3)
            else:
                x2 = x1 - 5 * math.cos(angle)
                y2 = y1 + 5 * math.sin(angle)
                self.canvas.create_line(x1, y1, x2, y2)
        self.draw_numbers()

    def draw_hand(self, angle, length, width, color='black', tag='hand'):
        angle = math.radians(90 - angle)
        x = self.center_x + length * math.cos(angle)
        y = self.center_y - length * math.sin(angle)
        return self.canvas.create_line(self.center_x, self.center_y, x, y, width=width, fill=color, tags=tag)

    def update_clock(self):
        self.canvas.delete("hand")  # Delete existing hands
        now = time.localtime()
        hours = now.tm_hour
        minutes = now.tm_min
        seconds = now.tm_sec
        h_angle = (hours % 12 + minutes / 60) * 30
        m_angle = minutes * 6
        s_angle = seconds * 6
        self.draw_hand(h_angle, self.radius * 0.6, 16, '#2274A5', 'hand')  # Hour hand
        self.draw_hand(m_angle, self.radius * 0.8, 8, '#F75C03', 'hand') # Minute hand
        self.draw_hand(s_angle, self.radius * 0.95, 4, '#F1C40F', 'hand')   # Second hand
        self.root.after(1000, self.update_clock)

    def draw_numbers(self):
        font_size = 42
        font = ('Arial', font_size, 'bold')
        for number in range(1, 13):
            angle = math.radians(-number * 30 + 90)
            x = self.center_x + (self.radius - 30) * math.cos(angle)
            y = self.center_y - (self.radius - 30) * math.sin(angle)
            self.canvas.create_text(x, y, text=str(number), font=font, fill='black')

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()
