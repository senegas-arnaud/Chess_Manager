from rich.console import Console

console = Console()

class View_player_info:

    def player_info(self):
        name = input("Enter player's name: ")
        surname = input("Enter player's surname: ")
        birthday = input("Enter player's date of birth (YYYY-MM-DD): ")
        national_id = input("Enter player's national ID: ")
        return name, surname, birthday, national_id
    
    
    def display_error(self, text):
        console.print(f"[red]{text}[/red]")

    def display_success(self, text):
        console.print(f"[green]{text}[/green]")
    
    def display_info(self, text):
        console.print(f"[blue]{text}[/blue]")

