

def month_to_convert(month):
    if type(month) != str:
        return "month need to be in letters"
    month = str(month).lower()
    switcher={
        "jan":"January",
        "feb":"February",
        "mar":"March",
        "apr":"April",
        "may":"May",
        "jun":"June",
        "jul":"July",
        "aug":"August",
        "oct":"October",
        "nov":"November",
        "dec":"Decmber"
    }
    return switcher.get(month,"Not a valid key")  # the second one is if no value matches
    # same as switcher[name]

print(month_to_convert("1"))

for i in range(10,20):
    print(i)

    
