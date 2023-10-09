import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.clock import Clock
import matplotlib.pyplot as plt
import numpy as np
import random

kivy.require("2.0.0")


class ContinuousPlotApp(App):
    def build(self):
        # Create the main layout as a vertical BoxLayout
        main_layout = BoxLayout(orientation="vertical")

        # Create a figure and axis for Matplotlib
        self.figure, self.ax = plt.subplots()

        # Create a Matplotlib canvas widget
        self.canvas = FigureCanvasKivyAgg(self.figure)
        main_layout.add_widget(self.canvas)

        # Create a button to start the plot
        self.start_button = Button(text="Start Plotting", size_hint=(1.0, 0.1))
        self.start_button.bind(on_press=self.start_plot)
        main_layout.add_widget(self.start_button)

        # Initialize the x and y data
        self.x_data = np.linspace(1, 10, 100)
        self.y_data = np.zeros_like(self.x_data)

        # Create a Clock event to update the plot
        self.plot_event = None

        return main_layout

    def start_plot(self, instance):
        # Start or restart the plot
        if self.plot_event:
            self.plot_event.cancel()
        self.plot_event = Clock.schedule_interval(self.update_plot, 0.001)

    def update_plot(self, dt):
        # Generate 10 random y-values
        random_values = [random.randint(0, 100) for _ in range(1)]
        print(random_values)
        # Update the y_data with the new random values
        self.y_data = np.roll(self.y_data, -1)
        self.y_data[-1:] = random_values

        # Clear the existing plot
        self.ax.clear()

        # Update the plot with new data
        self.ax.plot(self.x_data, self.y_data, color="b")
        self.ax.set_title("Continuous Plot")
        self.ax.set_xlabel("X-axis")
        self.ax.set_ylabel("Y-axis")

        # Redraw the canvas
        self.canvas.draw()


if __name__ == "__main__":
    ContinuousPlotApp().run()
