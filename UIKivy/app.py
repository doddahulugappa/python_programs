from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import random
import threading
import time
from kivy.clock import Clock

x = [1, 2, 3, 4, 5]
y = [5, 12, 6, 24, 29]
counter = 10


def data():
    data.a = None
    data.fig = None


data()

plt.plot(x, y)
plt.ylabel("Y axis")
plt.xlabel("X axis")


def gen_rand_int(intput):
    return random.randint(20, 50)


data.fig = Figure(figsize=(5, 4), dpi=100)
data.a = data.fig.add_subplot(111)
data.a.plot([1, 2, 3, 4, 5])
run_thread = True


def animate():
    while run_thread:
        data.a.clear()
        n_list = list(map(gen_rand_int, [0] * 5))
        data.a.plot(n_list)
        time.sleep(0.5)
        print("animate")
        global counter
        counter -= 1
        print(counter)
        if counter == 0:
            break


calcThread = threading.Thread(target=animate)
calcThread.start()


class View(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.box = self.ids.box
        canvas = FigureCanvasKivyAgg(data.fig)
        self.box.add_widget(canvas)
        Clock.schedule_interval(self.timer, 1)

    def timer(self, dt):
        canvas = FigureCanvasKivyAgg(data.fig)
        self.box.clear_widgets()
        self.box.add_widget(canvas)
        # print("timer")

    def save_it(self):
        print("button clicked")


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        Builder.load_file('app.kv')
        return View()


try:
    MainApp().run()

except:
    run_thread = False
    print("Keyboard interrupt")
