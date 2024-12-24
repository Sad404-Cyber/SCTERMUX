import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def loading_animation(task_description, duration=2):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True
    ) as progress:
        task = progress.add_task(task_description, total=None)
        time.sleep(duration)
        progress.update(task, description="Selesai!")
os.system("clear")
def main_menu():
    console.print(
        Panel(
            "[bold red]██████╗  ██╗ ███████╗  █████╗   █████╗   █████╗\n██╔══██╗ ██║ ╚══███╔╝ ██╔══██╗ ██╔══██╗ ██╔══██╗\n██║  ██║ ██║   ███╔╝  ╚██████║ ╚██████║ ╚██████║[/bold red]\n[bold white]██║  ██║ ██║  ███╔╝    ╚═══██║  ╚═══██║  ╚═══██║\n██████╔╝ ██║ ███████╗  █████╔╝  █████╔╝  █████╔╝\n╚═════╝  ╚═╝ ╚══════╝  ╚════╝   ╚════╝   ╚════╝[/bold white]\n"
            "[bold white]PEMBUAT : DIZFLYZE\nYOUTUBE : DIZFLYZE999\nVERSION : v2.8.1 Ultimated\n\n"
            "[bold green]╭────────────[ ALL MENU ]\n"
            "[bold green]|─>1.[/bold green] TEKS KE BETUK BESAR\n"
            "[bold green]|─>2.[/bold green] GAMBAR MENJADI BENTUK TEKS\n"
            "[bold red]╰─>3.[bold red] KELUAR",
            title="[ SC GENERATE TAMPILAN ]",
            border_style="red"
        )
    )

def main():
    while True:
        main_menu()
        console.print(f"[bold yellow]╭────────────[ PILIH SALAH SATU MENU ]")
        choice = console.input("[bold yellow]╰─> [ 1/2/3 ] : [/bold yellow]")

        if choice == "1":
            loading_animation("LOADING TO OPEN SCRIPT")
            os.system("python3 cfonts.py")
            os.system("exit")  
        elif choice == "2":
            loading_animation("LOADING TO OPEN SCRIPT")
            os.system("python3 image.py")
            os.system("exit")  
        elif choice == "3":
            loading_animation("BYE")
            console.print(
                Panel(
                    "[bold cyan]THANK YOU BRO[/bold cyan]",
                    border_style="green"
                )
            )
            break
        else:
            console.print(
                Panel(
                    "[bold red]INVALID FITUR[/bold red]",
                    border_style="red"
                )
            )

if __name__ == "__main__":
    main()