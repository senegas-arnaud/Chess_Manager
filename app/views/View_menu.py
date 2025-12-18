from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich import box

console = Console()

class View_menu:
    
    def display_main_menu(self):
        console.clear()
        
        # Titre avec bordure
        title = "[bold magenta]  ♟️    CHESS TOURNAMENT MANAGER    ♟️  [/bold magenta]"
        console.print(Align.center(Panel(title, style="bold blue", expand=False)))
        console.print()
        
        # Menu avec tableau stylisé
        table = Table(
            show_header=True,
            header_style="bold magenta",
            border_style="blue",
            box=box.ROUNDED,
            expand=False  # Important pour centrer
        )
        
        table.add_column("Option", justify="center", style="cyan", width=8)
        table.add_column("Action", justify="center", style="white", width=30)
        
        table.add_row("1", "👤 Add a player 👤")
        table.add_row("", "")
        table.add_row("2", "📋 List all players 📋")
        table.add_row("", "")
        table.add_row("3", "🏆 Create a tournament 🏆")
        table.add_row("", "")
        table.add_row("4", "⚙️  Manage tournament ⚙️")
        table.add_row("", "")
        table.add_row("5", "🔥 Launch tournament 🔥")
        table.add_row("", "")
        table.add_row("0", "🚪 Exit 🚪")
        
        console.print(Align.center(table))
        console.print()
        
        # Calculer le padding pour centrer manuellement
        terminal_width = console.width
        prompt_text = " Enter your choice ➤ "
        padding = (terminal_width - len(prompt_text)) // 2
        
        # Afficher le prompt centré sur la même ligne
        console.print(" " * padding + "[bold yellow]" + prompt_text + "[/bold yellow]", end="")
        
        choice = input()
        while choice not in ["0", "1", "2", "3", "4", "5"]:
            console.print(Align.center("[red]❌ Invalid choice! Please try again.[/red]"))
            console.print(" " * padding + "[bold yellow]" + prompt_text + "[/bold yellow]", end="")
            choice = input()
        return choice