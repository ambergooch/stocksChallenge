stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE": "General Electric"
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]

for value in purchases:
    for key in stockDict.keys():
        if value[0] == key:
            print(f"I purchased {stockDict[key]} stock for ${value[1] * value[3]}")

summary = {}
for block in purchases:
    print("block", block[0])
    summary[block[0]] = list(block)

print(summary)


# print(stockDict)