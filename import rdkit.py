import rdkit
from rdkit.Chem import AllChem, Descriptors
mol = AllChem.MolFromSmiles('CC') 
hybridization = [AllChem.GetHybridization(atom) for atom in mol.GetAtoms()]