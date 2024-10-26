import xml.etree.ElementTree as ET

#load the XML file

tree = ET.parse('atoms.xml')
root = tree.getroot()




#for atom_name in root.findall('effective_charge'):
 #   eff_charge = 


# Create a new element (tag) with text or attributes
new_element = ET.Element('atom_name')
new_element.text = 'AN'
new_element.set('atom_name', 'my_atom')

# Create a new element (tag) with text or attributes
new_element = ET.Element('atom symbol')
new_element.text = 'AS'
new_element.set('atom_symbol', 'a_s')


#find the element you want to update

#for element in root.findall()






#H_b  indicates a bridging hydrogen as in B2H6

#O_3_z is an oxygen suited for framework oxygens of a zeolite lattice.

#P_3_q is a tetrahedral four-coordinate phosphorus used to describe organo-metallic 
# coordinated phosphines, e.g., (Ph3P)2PtC

#extract the name  
