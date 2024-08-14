def main():
    months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }

    while True:
        try:
            date = input("What's the date?: ")
            if "/" in date:
                m, d, y = map(int, date.split("/"))
                if 1 <= m <= 12 and 1 <= d <= 31:
                    print(f"{y:04}-{m:02}-{d:02}")
                    break
            elif "," in date:
                parts = date.rstrip(",").split()
                if len(parts) == 3:
                    month, day, year = parts
                    if month in months:
                        m = months[month]
                        try:
                            d = int(day)
                            y = int(year)
                            if 1 <= d <= 31:
                                print(f"{y:04}-{m}-{d:02}")
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            pass
                raise ValueError
        except ValueError:
            print("Invalid date format. Please try again.")

if __name__ == '__main__':
    main()
