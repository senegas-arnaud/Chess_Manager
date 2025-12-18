from app.views.View_menu import View_menu
from rich.console import Console

class Controller_menu:

    def __init__(self):
        self.view = View_menu()
        self.console = Console()
    def main_menu(self):
        self.console.clear()
        while True:
            choice = self.view.display_main_menu()
            if choice == "0":
                break
            elif choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass