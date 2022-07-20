import pandas as pd
from rich.console import Console
from rich.markdown import Markdown
from rich.pretty import pprint
from rich.prompt import FloatPrompt, IntPrompt, Prompt

console = Console()


def menu():
    global console
    console.print(
        "[b red]╔══════════════════════════════════════════════════════════╗[/]",
        justify="center",
    )
    console.print(
        "[b red]║                     [u]FAIR BUS FARES[/u]                       ║[/]",
        justify="center",
    )
    console.print(
        "[b red]╚══════════════════════════════════════════════════════════╝[/]",
        justify="center",
    )
    console.print()
    console.print("01) Reading file bus", style="blue")
    console.print("02) Adding new bus detailS", style="blue")
    console.print("03) Schedule of all Buses", style="blue")
    console.print("04) Bus Enquiry", style="blue")
    console.print("05) Fare of SKC001", style="blue")
    console.print("06) Fare of SKC002", style="blue")
    console.print("07) Cancel bus", style="blue")
    console.print("08) Update fare of Bus", style="blue")
    console.print("09) Ticket Reservation", style="blue")
    console.print("10) Know more about this Project", style="blue")
    console.print("11) Quit", style="blue")


def divider():
    global console
    console.print()
    console.rule()
    console.print()


def about():
    global console
    TEXT = """
    This Project is Developed on **BUS DEVELOPMENT SYSTEM**.
    
    It contains 4 CSV files attached which are imported from MS Excel.
    """
    console.print(Markdown(TEXT))


def read_buses():
    global console
    console.print("[yellow]Reading details of file BUS...[/]")
    df = pd.read_csv("./data/Buses.csv")
    console.print(df)


def new_buses():
    global console
    console.print("[yellow]Adding new bus in the file...[/]")
    df = pd.read_csv("./data/Buses.csv")
    # console.print(df)
    # console.print()
    no = Prompt.ask("Enter bus no.")
    start = Prompt.ask("Enter start", default="Kuniyamuthur")
    stop = Prompt.ask("Enter stop", default="Gandhipuram")
    departure = FloatPrompt.ask("Enter departure", default="17.00")
    arrival = FloatPrompt.ask("Enter arrival", default="19.30")
    df = df.append([no, start, stop, departure, arrival], ignore_index=True)
    df.to_csv("./data/Buses.csv")
    console.print("Added record to Database", style="green bold")


def schedule():
    global console
    console.print("[yellow]Schedule of all buses:[/]")
    df = pd.read_csv("./data/Buses.csv")
    print(df[["BusNo.", "Departure", "Arrival"]])


def SKC001_fare():
    global console
    console.print("[yellow]show fares of SKC001 bus[/]")
    df = pd.read_csv("./data/SKC001.csv")
    print(df[[]])


def SKC002_fare():
    global console
    with console.status("show fares of SKC002 bus"):
        df = pd.read_csv("./data/SKC002.csv")
        print(df)


def cancelbus():
    global console
    with console.status("deleting cancelled bus detils"):
        df = pd.read_csv("./data/Buses.csv")
        # print(df)
        tnum = Prompt.ask("enter bus name")
        print("record of bus deleted")
        # print(df)


def changetiming():
    df = pd.read_csv("./data/Buses.csv")
    print("previous timings of arrival")
    print()
    print(df)
    print()
    df.loc[df["BusNo."] == "SKC002", ["Arrival"]] = df["Arrival"] + 2.0
    print()
    print(df)


def updateSKC001():
    print("to increase Fare and save")
    print("previous Fare")
    print()
    df = pd.read_csv("./data/SKC001.csv")
    print(df)
    print()
    print("increase FARE by Rs.50")
    print()
    df["FARE"] += 50
    print(df)


if __name__ == "__main__":
    menu()
    while True:
        divider()
        opt = IntPrompt.ask(
            "Enter your choice", choices=[str(i) for i in range(1, 12)], default=1
        )
        console.print()
        if opt == 1:
            read_buses()
        elif opt == 2:
            new_buses()
        elif opt == 3:
            schedule()
        elif opt == 4:
            SKC001_fare()
        elif opt == 5:
            SKC002_fare()
        elif opt == 6:
            cancelbus()
        elif opt == 7:
            changetiming()
        elif opt == 8:
            updateSKC001()
        elif opt == 9:
            print("Service Not Implemented.")
        elif opt == 10:
            about()
        elif opt == 11:
            break
        else:
            print("invalid option entered")
    divider()
    console.print("[red b]Thank you for choosing This service.[/]", justify="center")
    divider()
