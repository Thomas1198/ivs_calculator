##
# @file app.py
# @brief Main file for app
# @author xchova20
# @date 22.4. 2019

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.clock import Clock


from main.modules.math import *
from main.modules.parser import solve_expr

kivy.require("1.10.1")
#Builder.load_file('main/views/layout.kv')
with open('main/views/layout.kv', encoding='utf8') as f:
     Builder.load_string(f.read())


class CalculatorGridLayout(GridLayout):
    ## 
     # main function that calls parser module
     # @param float input from app
     # @return float result
    def calculate(self, expr):
        if expr:
            try:
                self.display.text = str(solve_expr(self.display.text))
            except Exception:
                self.display.text = "err"

class Tooltip(Label):
    pass

tooltips = {
    "x!": "Factorial of x.",
    "x^y": "Raise x to the power of y.",
    "√x": "Square root of x.",
    "y√x": "Y-th root of x.",
    "+": "Addition.",
    "-": "Subtraction.",
    "*": "Multiplication.",
    "/": "Division.",
    "=": "Solve expression.",
    ".": "Decimal point.",
}
class CustomButton(Button):
    tooltip = Tooltip()

    def __init__(self, **kwargs):
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(Button, self).__init__(**kwargs)
          
    # @brief function for showing help
    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        self.tooltip.pos = pos
        Clock.unschedule(self.display_tooltip)
        self.close_tooltip()
        if self.collide_point(*self.to_widget(*pos)):
            tooltip_text = tooltips.get(self.text)
            self.tooltip.text = tooltip_text or self.text
            Clock.schedule_once(self.display_tooltip, 1)

    def close_tooltip(self, *args):
        Window.remove_widget(self.tooltip)

    def display_tooltip(self, *args):
        Window.add_widget(self.tooltip)

 
class CalculatorApp(App):
    def build(self):
        return CalculatorGridLayout()
 
app = CalculatorApp()
app.run()
 
