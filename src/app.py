import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

from main.modules.math import *

kivy.require("1.10.1")
#Builder.load_file('main/views/layout.kv')
with open('main/views/layout.kv', encoding='utf8') as f:
     Builder.load_string(f.read())


class CalculatorGridLayout(GridLayout):
    def calculate(self, expr):
        if expr:
            try:
                #Cond. to find if we want power func.
                if '^' in self.display.text:
                    power_func = []
                    power_func = self.display.text.split('^')
                    self.display.text = str(power(power_func[0], power_func[1]))
                #self.display.text = calculate(expr))
                
            except Exception:
                self.display.text = "err"
 
class CalculatorApp(App):
    def build(self):
        return CalculatorGridLayout()
 
app = CalculatorApp()
app.run()
 
