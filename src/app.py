from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


Builder.load_string('''
<RootWidget>
   Button:
      on_press: root.printer()  
      text: "First button"  

''')


class RootWidget(BoxLayout):
    def printer(self):
        print("Hello world")

class Calculator(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    Calculator().run()