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

kivy.require("1.10.1")
#Builder.load_file('main/views/layout.kv')
with open('main/views/layout.kv', encoding='utf8') as f:
     Builder.load_string(f.read())


class CalculatorGridLayout(GridLayout):
    def calculate(self, expr):
        if expr:
            try:
                def organ_operations(text):
                    """Organize operations in list.
                    @param text input string text.
                    @return list of operations result.
                    """
                    op = ['*','/','+','-','!','^','√']
                    oper_input = []
                    for i in range(len(text)):
                        if text[i] in op:
                            oper_input.append(text[i])
                    return oper_input

                def organ_number(text):
                    """Organize numbers in list.
                    @param text input string text.
                    @return list of numbers result.
                    """
                    op = ['*','/','+','-','!','^','√']
                    number_input = []
                    number = ''
                    for i in range(len(text)):
                        if (text[i] in op)!=1:
                            number += text[i]
                        else:
                            number_input.append(number)
                            number = ''
                    number_input.append(number)
                    return number_input

                operations = []
                operations = organ_operations(self.display.text)
                numbers = []
                numbers = organ_number(self.display.text)
                
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
 
