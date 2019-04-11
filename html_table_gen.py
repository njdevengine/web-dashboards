# begin table
print("<table>")

# column headers
print("<th>")
for i in range(0,10):
    print("<td>"+df.columns[i]+"</td>")
print("</th>")

my_file = open("cities.csv","r")

    row = line.split(",")
    City_ID=row[0]
    City=row[1]
    Cloudiness=row[2]
    Country=row[3]
    Date=row[4]
    Humidity=row[5]
    Lat=row[6]
    Lng=row[7]
    MaxTemp=row[8]
    WindSpeed=row[9]

    print("<tr>")
    print("<td>%s</td>" % City_ID)
    print("<td>%s</td>" % City)
    print("<td>%s</td>" % Cloudiness)
    print("<td>%s</td>" % Country)
    print("<td>%s</td>" % Date)
    print("<td>%s</td>" % Humidity)
    print("<td>%s</td>" % Lat)
    print("<td>%s</td>" % Lng)
    print("<td>%s</td>" % MaxTemp)
    print("<td>%s</td>" % WindSpeed)
    print("</tr>")

# end the table
print("</table>")
