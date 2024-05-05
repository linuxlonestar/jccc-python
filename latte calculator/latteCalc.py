from nicegui import ui

#uses nicegui, a gui framework using web browsers.

baseUSD = 1
euro = 1.08
pound = 1.25
yen = 0.0065
peso = 0.059
canadian = 0.73
convertFrom = baseUSD
convertTo = baseUSD

ui.dark_mode()
ui.label('Latte Calculator').style("font-size: 400%")
cost = ui.input("enter amount here")
ui.label("Convert From:").style("font-size: 150%")
fromSelect = ui.select(["USD", "Euros", "British Pounds", "Japanese Yen", "Mexican Pesos", "Canadian Dollars"])
ui.label("Convert To:").style("font-size: 150%")
toSelect = ui.select(["USD", "Euros", "British Pounds", "Japanese Yen", "Mexican Pesos", "Canadian Dollars"])


def convert():
    if fromSelect.value == "USD":
        convertFrom = float(cost.value)
    elif fromSelect.value == "Euros":
        convertFrom = euro * float(cost.value)
    elif fromSelect.value == "British Pounds":
        convertFrom = pound * float(cost.value)
    elif fromSelect.value == "Japanese Yen":
        convertFrom = yen * float(cost.value)
    elif fromSelect.value == "Mexican Pesos":
        convertFrom = peso * float(cost.value)
    elif fromSelect.value == "Canadian Dollars":
        convertFrom = canadian * float(cost.value)

    if toSelect.value == "USD":
        output = convertFrom * baseUSD
    elif toSelect.value == "Euros":
        output = convertFrom * 0.93
    elif toSelect.value == "British Pounds":
        output = convertFrom * 0.80
    elif toSelect.value == "Japanese Yen":
        output = convertFrom * 153.06
    elif toSelect.value == "Mexican Pesos":
        output = convertFrom * 16.97
    elif toSelect.value == "Canadian Dollars":
        output = convertFrom * 1.37
    ui.label(f"{output:0.2f} {toSelect.value}".format(output))

    


convertBut = ui.button('convert', on_click=lambda: convert())


ui.label("Output:").style("font-size: 200%")

ui.run()