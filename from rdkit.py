from rdkit.Chem import GetPeriodicTable

# Initialize the periodic table
pt = GetPeriodicTable()

def get_valence_electrons(element_symbol_or_atomic_number):
    # Obtain the number of valence electrons
    if isinstance(element_symbol_or_atomic_number, int):
        valence_electrons = pt.GetNOuterElecs(element_symbol_or_atomic_number)
    else:
        atomic_number = pt.GetAtomicNumber(element_symbol_or_atomic_number)
        valence_electrons = pt.GetNOuterElecs(atomic_number)
    return valence_electrons

# Example Usage:
element = "O"  # Oxygen, as an example
print(f"Valence electrons in {element}: {get_valence_electrons(element)}")

# Alternatively, using an atomic number
atomic_number = 23  # Oxygen's atomic number
print(f"Valence electrons for atomic number {atomic_number}: {get_valence_electrons(atomic_number)}")
