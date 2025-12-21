from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich import box
import os

console = Console()

class View_tournament:

    def tournament_info(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n" * 3)
        
        title = Panel(
            "[bold magenta]📋  TOURNAMENT REGISTRATION  📋[/bold magenta]",
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
        name = console.input("[bold yellow]📝 Enter tournament's name ➤[/bold yellow] ")
        console.print()
        
        console.print(" " * padding_left, end="")
        location = console.input("[bold yellow]📝 Enter tournament's location ➤[/bold yellow] ")
        console.print()
        
        console.print(" " * padding_left, end="")
        beginning_date = console.input("[bold yellow]📅 Enter beginning date of tournament (YYYY-MM-DD) ➤[/bold yellow] ")
        console.print()

        console.print(" " * padding_left, end="")
        ending_date = console.input("[bold yellow]📅 Enter ending date of tournament (YYYY-MM-DD) ➤[/bold yellow] ")
        console.print()
        
        console.print(" " * padding_left, end="")
        remark = console.input("[bold yellow]🆔 Add any additionnal remarks ➤[/bold yellow] ")
        console.print()
        
        console.print(Align.center("[blue]" + "─" * 60 + "[/blue]"))
        
        return name, location, beginning_date, ending_date, remark
    
    
    def display_error(self, text):
        console.print(Align.center(f"\n [bold red]{text}[/bold red] \n"))

    def display_success(self, text):
        console.print(Align.center(f"[bold green]{text}[/bold green] \n"))
    
    def display_info(self, text):
        console.print(Align.center(f"[bold blue]{text}[/bold blue] \n"))

