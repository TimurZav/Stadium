# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

# Глобальные настройки
Window.clearcolor = (0, 1, 0, 1)
Window.title = "Stadium"


class MyApp(App):

    # Создание всех виджетов (объектов)
    def __init__(self):
        super().__init__()
        self.stadium = Label(text='Stadium', font_size=20)
        self.date = Label(text='Opening date', font_size=20)
        self.country = Label(text='Country', font_size=20)
        self.city = Label(text='City', font_size=20)
        self.capacity = Label(text='Capacity', font_size=20)
        self.input_data = TextInput(multiline=False, size_hint=(.36, None), pos_hint={"center_x": 0.5, "top": 1},
                                    height=45,
                                    hint_text='Stadium', font_size=23)
        self.input_data2 = TextInput(multiline=False, size_hint=(.36, None), pos_hint={"center_x": 0.5, "top": 1},
                                     height=45, input_filter="float",
                                     hint_text='Opening date', font_size=23)
        self.input_data3 = TextInput(multiline=False, size_hint=(.36, None), pos_hint={"center_x": 0.5, "top": 1},
                                     height=45,
                                     hint_text='Country', font_size=23)
        self.input_data4 = TextInput(multiline=False, size_hint=(.36, None), pos_hint={"center_x": 0.5, "top": 1},
                                     height=45,
                                     hint_text='City', font_size=23)
        self.input_data5 = TextInput(multiline=False, size_hint=(.36, None), pos_hint={"center_x": 0.5, "top": 1},
                                     height=45, input_filter="float",
                                     hint_text='Capacity', font_size=23)
        self.input_data.bind(text=self.on_text)
        self.input_data2.bind(text=self.on_text)
        self.input_data3.bind(text=self.on_text)
        self.input_data4.bind(text=self.on_text)
        self.input_data5.bind(text=self.on_text)

    # Получаем данные и производим их конвертацию
    def on_text(self, *args):
        data = self.input_data.text
        data2 = self.input_data2.text
        data3 = self.input_data3.text
        data4 = self.input_data4.text
        data5 = self.input_data5.text

        self.stadium.text = "Stadium: " + str(data)
        if data2.isnumeric():
            self.date.text = "Opening date: " + str(data2)
        else:
            self.date.text = "Opening date: " + ""
        self.country.text = "Country: " + str(data3)
        self.city.text = "City: " + str(data4)
        self.capacity.text = "Capacity: " + str(data5)
        if data5.isnumeric():
            self.capacity.text = "Capacity: " + str(data5)
        else:
            self.capacity.text = "Capacity: " + ""

    # Основной метод для построения программы
    def build(self):
        # Все объекты будем помещать в один общий слой
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.input_data)
        box.add_widget(self.input_data2)
        box.add_widget(self.input_data3)
        box.add_widget(self.input_data4)
        box.add_widget(self.input_data5)
        box.add_widget(self.stadium)
        box.add_widget(self.date)
        box.add_widget(self.country)
        box.add_widget(self.city)
        box.add_widget(self.capacity)

        return box


# Запуск проекта
if __name__ == "__main__":
    MyApp().run()
