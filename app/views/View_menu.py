from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich import box
import os

console = Console()


class View_menu:
    def display_main_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 10)

        title = "[bold magenta]  ♟️    CHESS TOURNAMENT MANAGER    ♟️  [/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()

        table = Table(
            show_header=True,
            header_style="bold magenta",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )

        table.add_column("Option", justify="center", style="cyan", width=30)
        table.add_column("Action", justify="center", style="white", width=30)

        table.add_row("1", "👤 Register new player 👤")
        table.add_row("", "")
        table.add_row("2", "📋 List all players 📋")
        table.add_row("", "")
        table.add_row("3", "🏆 Create a tournament 🏆")
        table.add_row("", "")
        table.add_row("4", "⚙️ Register player for a tournament ⚙️")
        table.add_row("", "")
        table.add_row("5", "🔥 Launch tournament 🔥")
        table.add_row("", "")
        table.add_row("6", "📊 Reports 📊")
        table.add_row("", "")
        table.add_row("0", "🚪 Exit 🚪")

        console.print(Align.center(table))
        console.print()

        terminal_width = console.width
        text = " Enter your choice ➤ "
        padding = (terminal_width - len(text)) // 2

        console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")

        choice = input()
        while choice not in ["0", "1", "2", "3", "4", "5"]:
            console.print(Align.center("[red]❌ Invalid choice! Please try again.[/red]"))
            console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
            choice = input()
        return choice

    def display_secondary_menu(self):
        console.print("\n" * 5)
        table = Table(
            show_header=False,
            header_style="bold magenta",
            border_style="blue",
            box=box.ROUNDED,
            expand=False
        )

        table.add_column(justify="center", style="bold magenta", width=30)
        table.add_column(justify="center", style="bold magenta", width=30)
        table.add_column(justify="center", style="bold magenta", width=30)

        table.add_row("1 ➤  Retry ", "2 ➤  Back to menu ", "3 ➤  Exit ")

        console.print(Align.center(table))
        console.print()

        terminal_width = console.width
        text = " Enter your choice ➤ "
        padding = (terminal_width - len(text)) // 2

        console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")

        choice = input()
        while choice not in ["0", "1", "2", "3"]:
            console.print(Align.center("[red]❌ Invalid choice! Please try again.[/red]"))
            console.print(" " * padding + "[bold yellow]" + text + "[/bold yellow]", end="")
            choice = input()
        return choice

    def exit_message(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 20)
        console.print(
            Align.center(
                Panel(
                    "[bold magenta]Thank you for using Chess Manager ! Goodbye ! 👋[/bold magenta]",
                    style="bold blue",
                    expand=False)))
        console.print("\n" * 20)
