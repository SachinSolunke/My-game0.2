from rich import print
from patterns import find_pattern

def start_game():
    print("[bold magenta]Welcome to the Code Pattern Game![/bold magenta]")
    code_list = [
        [34, 46, 64, 46, 56, 74],
        [16, 46, 58, 45, 14, 21],
        # Add more codes here...
    ]
    print("Codes loaded successfully.\n")
    
    target = int(input("Enter your target number to find the pattern: "))
    positions = find_pattern(code_list, target)

    if positions:
        print("[green]✅ Pattern Found! Positions:[/green]", positions)
    else:
        print("[red]❌ No Matching Pattern Found.[/red]")

if __name__ == "__main__":
    start_game()
