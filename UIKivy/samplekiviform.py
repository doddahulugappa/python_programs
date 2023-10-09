import random

import kivy
import numpy as np
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from matplotlib import pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.clock import Clock
counter = 1

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 1

        # self.button_grid = GridLayout()
        # self.button_grid.cols = 2

        # self.button_grid.add_widget(Label(text="Enter No hours"))

        figure, self.ax = plt.subplots()
        canvas = FigureCanvasKivyAgg(figure)
        self.inside.add_widget(canvas)

        # Initialize the x and y data
        self.x_data = np.linspace(1, 10, 10)
        self.y_data = np.zeros_like(self.x_data)
        self.y1_data = np.zeros_like(self.x_data)

        # Create a Clock event to update the plot
        self.plot_event = None

        self.add_widget(self.inside)

        self.button_grid = GridLayout()
        self.button_grid.cols = 3
        self.no_hours = TextInput(multiline=False, input_filter = "int")
        self.button_grid.add_widget(self.no_hours)

        self.submit = Button(text="Start", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.button_grid.add_widget(self.submit)

        self.stop = Button(text="Stop", font_size=40)
        self.stop.bind(on_press=self.exit)
        self.button_grid.add_widget(self.stop)

        self.add_widget(self.button_grid)

    def pressed(self, instance):
        # no_seconds = int(self.no_hours.text) * 3600
        # print(no_seconds)
        self.no_hours.text = ""
        self.plot_event = Clock.schedule_interval(self.update_plot, 0.0001)

    def exit(self, instance):
        print(instance)
        pass

    def update_plot(self, dt):
        # Generate 10 random y-values
        volt = [random.randint(0, 100) for _ in range(1)]
        volt_m = [random.randint(0, 100) for _ in range(1)]
        # Update the y_data with the new random values
        global counter
        self.y_data = np.roll(self.y_data, -1)
        self.x_data = np.roll(self.x_data, -1)
        self.x_data[-1:] = counter
        self.y1_data = np.roll(self.y1_data, -1)
        self.y_data[-1:] = volt
        self.y1_data[-1:] = volt_m
        counter += 1

        # Clear the existing plot
        self.ax.clear()

        # Update the plot with new data
        self.ax.plot(self.x_data, self.y_data, color="b")
        self.ax.plot(self.x_data, self.y1_data, color="r")
        self.ax.set_title("Continuous Plot")
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")
        self.ax.set_ylim([3.5, 5])

        # Redraw the canvas
        self.canvas.draw()


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()