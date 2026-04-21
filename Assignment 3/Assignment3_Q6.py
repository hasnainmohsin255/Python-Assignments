date = input("Enter date (mm/dd/yyyy): ")

parts = date.split("/")

month = int(parts[0])
day = parts[1]
year = parts[2]

months = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]

print(months[month - 1], day + ",", year)