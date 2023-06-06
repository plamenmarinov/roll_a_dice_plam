import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random


class DiceRoller(App):
    def build(self):
        # Create the layout
        layout = BoxLayout(orientation='vertical')

        # Create the label to display the dice result
        self.result_label = Label(text='Roll the dice!', font_size=100)
        layout.add_widget(self.result_label)

        # Create the roll button
        roll_button = Button(text='Roll the dice', font_size=50)
        roll_button.bind(on_press=self.roll_dice)
        layout.add_widget(roll_button)

        return layout

    def roll_dice(self, instance):
        # Generate a random number between 1 and 6
        dice_result = random.randint(1, 12)

        # Update the label with the dice result
        self.result_label.text = f'You rolled a {dice_result}'


if __name__ == '__main__':
    DiceRoller().run()
