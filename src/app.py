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
                #function that return dict. of all functions used in raw input
                def organ_operations(text):
                    op = ['*','/','+','-','!','^','√']
                    oper_input = []
                    for i in range(len(text)):
                        if text[i] in op:
                            oper_input.append(text[i])
                    return oper_input

                #function that return dict. of all numbers used in raw input
                def organ_number(text):
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
 
class CalculatorApp(App):
    def build(self):
        return CalculatorGridLayout()
 
app = CalculatorApp()
app.run()
 
