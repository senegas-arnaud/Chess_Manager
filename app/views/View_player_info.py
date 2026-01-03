from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich import box
import os

console = Console()


class View_player_info:

    def player_info(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 5)

        title = Panel(
            "[bold magenta]📋  PLAYER REGISTRATION  📋[/bold magenta]",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )
        console.print(Align.center(title))
        console.print()

        console.print(Align.center("[blue]" + "─" * 60 + "[/blue]"))
        console.print()

        terminal_width = console.width
        form_width = 50
        padding_left = (terminal_width - form_width) // 2

        console.print(" " * padding_left, end="")
        name = console.input("[bold yellow]📝 Enter player's name ➤[/bold yellow] ")
        console.print()

        console.print(" " * padding_left, end="")
        surname = console.input("[bold yellow]📝 Enter player's surname ➤[/bold yellow] ")
        console.print()

        console.print(" " * padding_left, end="")
        birthday = console.input("[bold yellow]📅 Enter date of birth (YYYY-MM-DD) ➤[/bold yellow] ")
        console.print()

        console.print(" " * padding_left, end="")
        national_id = console.input("[bold yellow]🆔 Enter national ID ➤[/bold yellow] ")
        console.print()

        console.print(Align.center("[blue]" + "─" * 60 + "[/blue]"))

        return name, surname, birthday, national_id

    def display_error(self, text):
        console.print(Align.center(f"\n [bold red]{text}[/bold red] \n"))

    def display_success(self, text):
        console.print(Align.center(f"[bold green]{text}[/bold green] \n"))

    def display_info(self, text):
        console.print(Align.center(f"[bold blue]{text}[/bold blue] \n"))
