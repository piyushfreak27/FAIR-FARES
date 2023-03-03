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
    console.print("05) Cancel bus", style="blue")
    console.print("06) Update fare of Bus", style="blue")
    console.print("07) Ticket Reservation", style="blue")
    console.print("08) Know more about this Project", style="blue")
    console.print("09) Quit", style="blue")


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


def send_ticket(bus: str, start: str, end: str, fare: int, email: str) -> None:
    from trycourier import Courier

    atk = "pk_test_08Q6VNQG9GMZVPNV1S39W77J4CVN"
    client = Courier(auth_token=atk)
    resp = client.send_message(
        message={
            "to": {
                "email": email,
            },
            "data": {
                "subject": "Ticket Confirmed",
                "bus": bus,
                "start": start,
                "end": end,
                "fare": fare,
            },
            "template": "DJRV8MJGKRMQG8MSRYH3T8S38A1R",
        }
    )

    return OTP


def ticket_reservation():
    global console
    console.print("[yellow]Ticket Reservation:[/]")
    df = pd.read_csv("./data/Buses.csv")
    print(df[["BusNo.", "Departure", "Arrival"]])
    bus = IntPrompt.ask("Enter bus no.")
    df = pd.read_csv(f"./data/SKC{bus:03d}.csv")
    console.print(df)

    start = Prompt.ask("Enter start", default=df["START"][0])
    end = Prompt.ask("Enter end", default=df["STOP"][0])
    fare = df["FARE"][0]
    console.print(f"Total fare: Rs.{fare}", style="green bold")
    email = Prompt.ask("Enter email")
    confirm = Prompt.ask("Confirm ticket?", choices=["y", "n"], default="y")

    if confirm == "y":
        send_ticket(bus, start, end, fare, email)
        console.print("Ticket confirmed", style="green bold")
    else:
        console.print("Booking cancelled", style="red bold")


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
            "Enter your choice", choices=[str(i) for i in range(1, 10)], default=1
        )
        console.print()
        if opt == 1:
            read_buses()
        elif opt == 2:
            new_buses()
        elif opt == 3:
            schedule()
        elif opt == 4:
            cancelbus()
        elif opt == 5:
            changetiming()
        elif opt == 6:
            updateSKC001()
        elif opt == 7:
            ticket_reservation()
        elif opt == 8:
            about()
        elif opt == 9:
            break
        else:
            print("invalid option entered")
    divider()
    console.print("[red b]Thank you for choosing This service.[/]", justify="center")
    divider()
