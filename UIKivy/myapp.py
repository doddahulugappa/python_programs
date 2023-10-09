import random

from kivy.app import App
from kivy.clock import Clock
from matplotlib import pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import time


class MyApp(App):
    def build(self):
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([0], [0])
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        # time.sleep(0)
        return FigureCanvasKivyAgg(self.fig)

    def update(self, dt):
        y = random.random()
        self.line.set_ydata([y])
        self.line.set_xdata([random.random()])
        self.ax.relim()
        self.ax.autoscale_view(True,True,True)
        self.fig.canvas.draw_idle()

if __name__ == '__main__':
    MyApp().run()