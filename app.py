import flet as ft
from osinfo import Info
from diskComponent import DiskComponent

def show(page: ft.page):
    info: Info = Info()
    
    page.add(
        ft.Text(f"hostname: {info.host}"),
        ft.Text(f"ip: {info.ip}")
    )
    
    disks: dict = info.disks()

    for device, disk_info in disks.items():
        disk = DiskComponent(disk_info)
        #disk.show()
        page.add(disk)


def main(page: ft.Page):
    page.title = "my domain"
    page.vertical_alignment = 'center'
    page.horizontal_alignement = 'center'

    
    show(page)
      
ft.app(target=main)
