#tester program
import functions



#dissociation energy tester:
def det():
    bond_order = input("Enter the bond order : ")
    print("the dissociation energy is :", functions.get_diss_energy(int(bond_order)))

#function to get effective charges

def ec():
    my_atom_type = input("enter the atom type : ")
    print("the effective charge is :" , functions.get_effective_charge(my_atom_type))

#function to get bond radii

def br():
    my_atom_type = input("enter the atom type : ")
    print("the bond radii is :" , functions.get_bond_radi(my_atom_type))

def tester(n):
    match n:
      case "1":
            det()
      case "2":
            ec()
      case "3":
            br()
      


choice = input(""" what program do you want to test?
      1:function to get dissociation energy take bond order as an argument.
      2:function to get effective charges
      3:function to get bond radii         
""")
tester(choice)