
from rich import print
from rich.table import Column, Table

table = Table(show_header=True, header_style="bold magenta")

table.add_column("software", style="dim", width=25)
table.add_column("language")
table.add_column("fuction", justify="right")

table.add_row("TOM/AV3", "MATLAB", "Tomo/STA")
table.add_row("PyTOM", "Python", "Tomo/STA")
table.add_row("IMOD/PEET", "JAVA", "Tomo/STA")
table.add_row("Jsubtomo/Bsoft", "JAVA", "Tomo/STA")
table.add_row("protomo/i3", "shell", "Tomo/STA")
table.add_row("SPIDER/ SPIRE/RAMOS", "C++/JAVA", "Tomo/STA")
table.add_row("EMAN", "Python", "Tomo/STA")
table.add_row("Dynamo", "MATLAB", "STA")
table.add_row("MLTOMO/RELION", "C++", "STA")
table.add_row("STOPGAP/novaSTA", "MATLAB", "STA")
table.add_row("emClarity", "MATLAB", "Tomo/STA")
print(table)