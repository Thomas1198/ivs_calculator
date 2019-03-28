import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

from main.modules.math import calculate

kivy.require("1.10.1")
Builder.load_file('main/views/layout.kv')


class CalculatorGridLayout(GridLayout):
    def calculate(self, expr):
        if expr:
            try:
                self.display.text = calculate(expr)
            except Exception:
                self.display.text = "err"
 
class CalculatorApp(App):
    def build(self):
        return CalculatorGridLayout()
 
app = CalculatorApp()
app.run()
 