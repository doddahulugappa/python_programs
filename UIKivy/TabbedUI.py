from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button


Builder.load_string("""

<Test>:
    size_hint: 1, 1
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    TabbedPanelItem:
        text: 'first tab'
        Label:
            text: 'Anode Params'

    TabbedPanelItem:
        id: tab2
        text: 'tab2'

        BoxLayout:
            id: box1
            orientation: 'vertical'

            Label:
                id: label1
                text: 'Second tab content area'
            Button:
                id: button1
                text: 'Button that does nothing'

            BoxLayout:
                id: box2
                orientation: 'vertical'

                Label:
                    id: label2
                    text: 'Label 2'

                BoxLayout:
                    id: box3
                    orientation: 'vertical'

                    Button:
                        id: button2
                        text: 'Button 2'
                    Label:
                        id: label3
                        text: 'Label 3'

    TabbedPanelItem:
        text: 'tab3'
        RstDocument:
            text:
                '\\n'.join(("Hello world", "-----------",
                "You are in the third tab."))

""")


class Test(TabbedPanel):

    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
        print(f"\nself.ids.items():")
        for key, val in self.ids.items():
            if isinstance(val, Label) or isinstance(val, Button):
                print(f"\tkey={key}, val={val}, val.text={val.text}")
            else:
                print(f"\n\tkey={key}, val={val}")

        print(f"\nself.ids.label3.text={self.ids.label3.text}")


class TabbedPanelApp(App):
    def build(self):
        return Test()


if __name__ == '__main__':
    TabbedPanelApp().run()