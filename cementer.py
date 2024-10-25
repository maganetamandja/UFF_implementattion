
import csv 

filename = "cemented.csv"



# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    

header = '<?xml version="1.0" encoding="UTF-8"?>'
doctag = '<atoms>'
print (header)
print(doctag)

for row in rows:
    name = row[7]

    symbol = row[8]

    geometry_sym = row[9]

    geometry_name = row[10]

    formal_oxidation = row[11]
    atom_type = row[0]

    bond = row[1]

    angle = row[2]

    distance = row[3]

    energy = row[4]

    scale = row[5]

    effective_charge = row[6]

    coreline = f"""

        <atom_name>

            {name}
            <atom_symbol>
            {symbol}
            </atom_symbol>
            <atom_type>
                {atom_type}
            </atom_type>

            <geometry_sym>
            {geometry_sym}
            </geometry_sym>

            <geometry_name>
            {geometry_name}
            </geometry_name>
            
            <formal_oxidation>
            {formal_oxidation}
            </formal_oxidation>

            <valence>
                
                <bond>
                    {bond}
                </bond>

                <angle>
                    {angle}
                </angle>

            </valence>

            <nonbond>
                
                <distance>
                    {distance}
                </distance>

                <energy>
                    {energy}
                </energy>

                <scale>
                    {scale}
                </scale>
            </nonbond>

            <effective_charge>
                    {effective_charge}
            </effective_charge>
    </atom_name>
    """
    print(coreline)
enddoc = '</atoms>'
print(enddoc)