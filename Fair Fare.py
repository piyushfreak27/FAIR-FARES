import pandas as pd





def menu():


    print()
    print()
    print()
    print(" ________________________________") 
    print("|                                | ")
    print("|    ||  FAIR BUS FARES  ||      |")
    print("|________________________________|")
    print()
    print()
    print(" 1. Know more about this Project")
    print(" 2. Reading file bus")
    print(" 3. Adding new bus detailS")
    print(" 4. Schedule of all Buses")
    print(" 5. Bus Enquiry")
    print(" 6. Fare of SKC001")
    print(" 7. Fare of SKC002")
    print(" 8. Cancel bus")
    print(" 9. Update fare of Bus")
    print(" 10.Ticket Reservation")
    print()
    print("*******************************************************************************")
    print()







menu()

def about():
    print("This Project is Developed on *BUS DEVELOPMENT SYSTEM*."
          "It contains 4 CSV files attached which are imported from MS Excel.")


def read_buses():
    print("reading details of file BUS")
    print()
    print()
    df=pd.read_csv("C:\\Users\\PIYUSH\\OneDrive\\Desktop\\Hackathon\\Buses.csv",index_col=0)
    print(df)


def new_buses():
    print('Adding new bus in the file')
    print()
    df=pd.read_csv("C:\\Users\\PIYUSH\\OneDrive\\Desktop\\Hackathon\\Buses.csv")
    print(df)
    print()
    n=(input('Enter bus no.'))
    a=(input('Enter bus name'))
    b=(input("Enter start"))
    c=(input('Enter stop'))
    d=float(input('Enter departure:'))
    e=float(input('Enter arrival:'))
    df.loc[n]=[a,b,c,d,e,]
    print(df)


def schedule():
    print('schedule of all buses')
    print()
    df=pd.read_csv("C:\\Users\\PIYUSH\\OneDrive\\Desktop\\Hackathon\\Buses.csv")
    print(df)

def SKC001_fare():
    print('show fares of SKC001 bus')
    print()
    df=pd.read_csv("C:\\Users\\PIYUSH\\OneDrive\\Desktop\\Hackathon\\SKC001.csv")
    print(df)

    
    
def SKC002_fare():
    print('show fares of SKC002 bus')
    print()
    df=pd.read_csv("C:\\Users\\PIYUSH\\OneDrive\\Desktop\\Hackathon\\SKC002.csv")
    print(df)
   


def cancelbus():
    print('deleting cancelled bus detils')
    df=pd.read_csv("C:\\Users\\PIYUSH\\OneDrive\\Desktop\\Hackathon\\Buses.csv")
    print(df)
    tnum=(input('enter bus name :'))
    print('record of bus deleted')
    print()
    print(df)


def changetiming():
    df=pd.read_csv("C:\\Users\\PIYUSH\\OneDrive\\Desktop\\Hackathon\\Buses.csv")
    print('previous timings of arrival')
    print()
    print(df)
    print()
    df.loc[df['BusNo.']=='SKC002',['Arrival']]=df['Arrival']+ 2.0
    print()
    print(df)

def updateSKC001():
    print('to increase Fare and save')
    print('previous Fare')
    print()
    df=pd.read_csv("C:\\Users\\PIYUSH\\OneDrive\\Desktop\\Hackathon\\SKC001.csv")
    print(df)
    print()
    print('increase FARE by Rs.50')
    print()
    df=pd.read_csv("C:\\Users\\PIYUSH\\oneDrive\\Desktop\\Hackathon\\SKC001.csv")
    df["FARE"]+=50
    print(df)


    
    


opt=''
opt=int(input('Enter your choice:'))
if opt==1:
    about()
elif opt==2:
    read_buses()
elif opt==3:
    new_buses()
elif opt==4:
    schedule()
elif opt==5:
    SKC001_fare()
elif opt==6:
    SKC002_fare()
elif opt==7:
    cancelbus()
elif opt==8:
    changetiming()
elif opt==9:
    updateSKC001()
else:
    print('invalid option entered')
    print('')



    
    
    
    
    
    
