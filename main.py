import pandas as pd
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def menu():
    global console
    console.print("[b red]╔══════════════════════════════════════════════════════════╗[/]", justify="center")
    console.print("[b red]║                     [u]FAIR BUS FARES[/u]                       ║[/]", justify="center")
    console.print("[b red]╚══════════════════════════════════════════════════════════╝[/]", justify="center")
    console.print()
    console.print("01) Know more about this Project", style="blue")
    console.print("02) Reading file bus", style="blue")
    console.print("03) Adding new bus detailS", style="blue")
    console.print("04) Schedule of all Buses", style="blue")
    console.print("05) Bus Enquiry", style="blue")
    console.print("06) Fare of SKC001", style="blue")
    console.print("07) Fare of SKC002", style="blue")
    console.print("08) Cancel bus", style="blue")
    console.print("09) Update fare of Bus", style="blue")
    console.print("10) Ticket Reservation", style="blue")
    console.print("11) Quit", style="blue")

def about():
    global console
    TEXT = "This Project is Developed on **BUS DEVELOPMENT SYSTEM**. It contains 4 CSV files attached which are imported from MS Excel."
    console.print(Markdown(TEXT))


def read_buses():
    global console
    with console.status("Reading details of file BUS"):
        df = pd.read_csv("./data/Buses.csv")
        console.print(df)


def new_buses():
    global console
    with console.status("Adding new bus in the file"):
        df = pd.read_csv("./data/Buses.csv")
        console.print(df)
        console.print()
        a = input("Enter bus no.")
        b = input("Enter start")
        c = input("Enter stop")
        d = float(input("Enter departure:"))
        e = float(input("Enter arrival:"))
        df = df.append([a, b, c, d, e], ignore_index=True)
        console.print("Added record to Database", style="green bold")


def schedule():
    print("schedule of all buses")
    print()
    df = pd.read_csv("./data/Buses.csv")
    print(df)


def SKC001_fare():
    print("show fares of SKC001 bus")
    print()
    df = pd.read_csv("./data/SKC001.csv")
    print(df)


def SKC002_fare():
    print("show fares of SKC002 bus")
    print()
    df = pd.read_csv("./data/SKC002.csv")
    print(df)


def cancelbus():
    print("deleting cancelled bus detils")
    df = pd.read_csv("./data/Buses.csv")
    print(df)
    tnum = input("enter bus name :")
    print("record of bus deleted")
    print()
    print(df)


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
        console.print()
        console.rule()
        console.print()
        opt = int(input("Enter your choice: "))
        if opt == 1:
            about()
        elif opt == 2:
            read_buses()
        elif opt == 3:
            new_buses()
        elif opt == 4:
            schedule()
        elif opt == 5:
            SKC001_fare()
        elif opt == 6:
            SKC002_fare()
        elif opt == 7:
            cancelbus()
        elif opt == 8:
            changetiming()
        elif opt == 9:
            updateSKC001()
        elif opt == 10:
            print("Service Not Implemented.")
        elif opt == 11:
            break
        else:
            print("invalid option entered")
    console.print()
    console.rule()
    console.print()
    print("Thank you for choosing This service.")
