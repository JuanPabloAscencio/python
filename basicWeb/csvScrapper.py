from urllib import request
csvURL = "https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/datasets/AirPassengers.csv"
#placeholder csv
def csvScrapper(csvUrl):
    response = request.urlopen(csvUrl)
    csv = response.read()
    csv_str = str(csv)
    file = csv_str.split("\\n")
    dest_url = r"scprr.csv"
    fx = open("scprr.csv", "w")
    for line in file:
        fx.write(line + "\n")
    fx.close()
csvScrapper(csvURL)
