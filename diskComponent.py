import flet as ft

class DiskComponent(ft.UserControl):
    def __init__(self, data: dict)->None:
        super().__init__()
        self.device = data["device"]
        self.size = data["size"]
        self.used = data["used"]
        self.available = data["available"]
        self.percent = data["percent"]
        self.mount = data["mountpoint"]

    def build(self):
        return ft.Column(
            [
                ft.Text(f"Device: {str(self.device)}"), 
                ft.Text(f"Size: {self.size}"), 
                ft.Text(f"Used {self.used}"), 
                ft.Text(f"available: {self.available}"), 
                ft.Text(f"percent: {self.percent}"),
                ft.Text(f"mountpoint: {self.mount}")
            ],
            spacing = 0
        )

    def show(self)->None:
        print(f"\ndevice: {self.device}")
        print(f"size: {self.size}")
        print(f"used: {self.used}")
        print(f"available: {self.available}")
        print(f"percent: {self.percent}")
        print(f"mount: {self.mount}\n")

