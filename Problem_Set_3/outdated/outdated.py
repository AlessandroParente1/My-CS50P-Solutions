def main():
    months ={
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }

    while True:
        try:
            date =input("Date: ").strip()

            #Controllo formato numerico (M/D/YYYY)
            if "/" in date:
                month, day, year = map(int, date.split("/"))
            #Controllo formato testuale (Month D, YYYY)
            elif "," in date:
                month_str, rest = date.split(" ",1)
                day, year = map(int, rest.replace(",","").split())
                if month_str in months:
                    month =int (months[month_str])
                else:
                    continue #Riprova se il mese non è valido
            else:
                continue #Riprova se il formato non è riconosciuto

            #Verifica che il giorno sia valido
            if 1<= month <=12 and 1<=day <=31:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
            else:
                continue #Se il giorno è maggiore di 31, riprova
            
        except (ValueError, IndexError):
            pass #Se c'è un errore, riprova

main()
