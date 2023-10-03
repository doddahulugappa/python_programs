from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty


class MainApp(App):
    sw_started = BooleanProperty(False)

    def on_sw_started(self, *args):
        # This will call meth. update_time whenever attr. sw_started changes.
        self.update_time(args)

    def build(self):
        self.frequency = 1.0
        #        self.bind(sw_started = self.update_time)
        self.sw_seconds = 0
        # self.tmp_sw_seconds = 0 #this way doesnt work either
        Clock.schedule_interval(self.update_time, self.frequency)

        self.lbl = Label(text="0")
        return self.lbl

    def on_start(self):
        self.sw_started = True

    #        self.start_timer()

    def update_time(self, *args):
        if self.sw_started:
            #        if self.sw_started==True:
            self.sw_seconds += self.frequency
            print(int(self.sw_seconds))
            self.lbl.text = str(int(self.sw_seconds))

    def reset_timer(self):
        self.sw_started = False
        self.sw_seconds = 0

    #    def start_timer(self):
    #        self.sw_started = True

    #    def stop_timer(self):
    #        self.sw_started=False

    def on_pause(self):
        self.sw_started = False
        #        self.stop_timer()
        # self.tmp_sw_seconds = self.sw_seconds #this way doesnt work either
        print("timer paused")
        return True

    def on_resume(self):
        # self.sw_seconds = self.tmp_sw_seconds #this way doesnt work either
        #        self.start_timer()
        print("timer resumed")
        self.sw_started = True


#        pass
MainApp().run()