from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import bluetooth

class BluetoothApp(MDApp):

    def build(self):
        # Desain UI dengan KivyMD
        self.app_kv = '''
MDScreen:
    MDBoxLayout:
        orientation: "vertical"
        MDLabel:
            id: bluetooth_status
            text: "Memeriksa status Bluetooth..."
            halign: "center"
            theme_text_color: "Primary"
    '''
        self.screen = Builder.load_string(self.app_kv)
        # Jadwalkan pembaruan status Bluetooth secara berkala
        Clock.schedule_interval(self.check_bluetooth_status, 1)  # Memeriksa setiap 1 detik
        return self.screen

    def check_bluetooth_status(self, dt):
        # Periksa status Bluetooth
        if bluetooth.is_enabled():
            self.screen.ids.bluetooth_status.text = "Bluetooth ON"
        else:
            self.screen.ids.bluetooth_status.text = "Bluetooth OFF"

BluetoothApp().run()
