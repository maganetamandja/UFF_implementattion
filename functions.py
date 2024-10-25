import math
import csv 
from rdkit.Chem import GetPeriodicTable
import numpy as np
# Initialize the periodic table
pt = GetPeriodicTable()
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

#function to get dissociation energy take bond order as an argument.

def get_diss_energy(n: int):
    return n*70

#function to get effective charges
def get_effective_charge(atom_type : str):
    return_value = None
    for row in rows:
        
        if str(row[0]) == atom_type:
            return_value =  float(row[6])
        else:
            pass
            

    if return_value != None:
        return return_value
    else:
        print(atom_type , " atom type not found")

#function to get bond radii
def get_bond_radi(atom_type : str):
    return_value = None
    for row in rows:
        
        if str(row[0]) == atom_type:
            return_value =  float(row[1])
        else:
            pass
            

    if return_value != None:
        return return_value
    else:
        print(atom_type , " atom type not found")

#function to get distance
def get_par_x(atom_type : str):
    return_value = None
    for row in rows:
        
        if str(row[0]) == atom_type:
            return_value =  float(row[21])
        else:
            pass
            

    if return_value != None:
        return return_value
    else:
        print(atom_type , " atom type not found")
#get natural angle bend 

def get_natural_angle(atom_type : str):
    return_value = None
    for row in rows:
        
        if str(row[0]) == atom_type:
            return_value =  float(row[2])
        else:
            pass
            

    if return_value != None:
        return return_value
    else:
        print(atom_type , " atom type not found")

#get geometrical form
def get_geometrical_form(atom_type : str):
    return_value = None
    for row in rows:
        
        if str(row[0]) == atom_type:
            return_value =  row[9]
        else:
            pass
            

    if return_value != None:
        return return_value
    else:
        print(atom_type , " atom type not found")

#get torsion barrier parameters for sp3
def get_torsion_barrier_par_3(atom_type : str):
    return_value = None
    for row in rows:
        
        if str(row[0]) == atom_type:
            return_value =  row[38]
        else:
            pass
            

    if return_value != None:
        return return_value
    else:
        print(atom_type , " atom type not found")


#get van der wals distance
def get_vanderwal_distance(atom_type : str):
    return_value = None
    for row in rows:
        
        if str(row[0]) == atom_type:
            return_value =  row[3]
        else:
            pass
            

    if return_value != None:
        return return_value
    else:
        print(atom_type , " atom type not found")


#get van der wals energy
def get_vanderwal_energy(atom_type : str):
    return_value = None
    for row in rows:
        
        if str(row[0]) == atom_type:
            return_value =  row[4]
        else:
            pass
            

    if return_value != None:
        return return_value
    else:
        print(atom_type , " atom type not found")
# Obtain the number of valence electrons

def get_valence_electrons(element_symbol):
    return_value = None
    for row in rows:
        
        if str(row[8]) == element_symbol:
            return_value =  pt.GetNOuterElecs(element_symbol) 
        else:
            pass
            

    if return_value != None:
        return return_value
    else:
        print(element_symbol , " atom element not found")

#get the piriod

def get_atom_period(atom_type : str):
    return_value = None
    for row in rows:
        
        if str(row[0]) == atom_type:
            return_value =  row[17]
        else:
            pass
            

    if return_value != None:
        return return_value
    else:
        print(atom_type , " atom type not found") 


#get big_u
def get_big_u(period):
    return_value = None

    if period == 1:
        return_value = 2
    elif period == 2:
        return_value = 2
    elif period == 3:
        return_value = 1.25
    elif period == 4:
        return_value = 0.7
    elif period == 5:
        return_value = 0.2
    elif period == 6:
        return_value = 0.1

    return return_value


#get torsion barrier parameters for sp2
def get_torsion_barrier_par_2(bond_order,big_u_j,big_u_k ):
    return_value = None
    big_u_j = None
    big_u_k = None
    return 5*math.sqrt(big_u_j*big_u_k)*(1+ 4.18*math.ln(bond_order))
    

    





#function to get bond order correction

def get_bond_order_correction(bond_ri, bond_rj, bond_order):
    return -0.1332*(bond_ri +bond_rj)*math.log(bond_order)

#function to get the electronegativity correction
def get_electronegativity_correction(bond_ri,bond_rj, dist_i, dist_j):
    return bond_ri *bond_rj ((math.sqrt(dist_i) - math.sqrt(dist_j))^2 )/(dist_i *bond_ri + dist_j*bond_rj)

#function to get the bond radii at equilibrium aka rij

def get_natural_bond_length(ri,rj, rbo, ren):
    return ri+rj+rbo-ren


#function to get the force constant aka kij

def get_force_constant(effective_charge_i, effectivecharge_j, natural_bond_length):
    return 664.12 * (effective_charge_i *effectivecharge_j)/natural_bond_length^3 

#function to get rik
def get_rik(rij, rjk, theta_0):
    return rij^2 + rjk^2 - 2*rij*rjk*math.cos(theta_0)

#function to get alfa

def get_alfa(dissociation_energy, force_constant):
    return math.sqrt(force_constant/(2*dissociation_energy))

#function to find betha

def get_beta(natural_bond_lengthij,natural_bond_lengthjk):
    return 664.12/(natural_bond_lengthij * natural_bond_lengthjk)

#function to get angle bend constant :  K_IJK

def get_K_IJK(beta, eff_char_i, eff_char_j, natural_bond_lengh_ik, natural_bond_lengh_ij, natural_bond_lengh_jk, std_angle):
    return beta *((eff_char_i*eff_char_j)/natural_bond_lengh_ik^5) * natural_bond_lengh_ij * natural_bond_lengh_jk*(3*natural_bond_lengh_ij * natural_bond_lengh_jk*(1-(math.cos(std_angle))^2) - natural_bond_lengh_ik^2 * math.cos(std_angle))

#function to get angle bend
def get_angle_bend(std_angle, K_IJK, angle):
    C_2 = 1/ (4*(math.sin(std_angle))^2)
    C_1 = -4*C_2  * math.cos(std_angle)
    C_0 = C_2*(2*(math.cos(std_angle))+1)

    return K_IJK * [C_0 + C_1 * math.cos(angle) + C_2 * math.cos(2 * angle)]


#function to get the bond strech
#Er = D_ij[e^{- a (r - rij)}-1]^2
def get_bond_stretch(dissociation_energy, alfa, equi_radii,r):
    return dissociation_energy*(math.exp(-alfa*(r-equi_radii))-1)^2


#function to get the torsional barrier V 3

def get_torsional_barrier_3( torsional_par_j,torsional_par_k ):
    
    return math.sqrt(torsional_par_j*torsional_par_k)

#function to get the torsional barrier V 2
def get_torsional_barrier_2( torsional_par_j,torsional_par_k, BOJK ): #BOJK is the bond order between atomes j and k
    return 5*math.sqrt(torsional_par_j*torsional_par_k)*(1+4.18*math.log(BOJK))

#function to get the torsional barrier V when j, k belong to the 16th group.
def get_torsional_barrier_V(atom):
    return_value: None
    if atom == "O":
        return_value = 2.0
    else:
        return_value = 6.8
    return return_value


#get the value of fie_equilibrium
def get_fie_equi(type_of_atom_i, type_of_atom_j):
    return_value = None
    if (type_of_atom_i == type_of_atom_j):
        return_value = 180
    elif(type_of_atom_j != type_of_atom_i):
        return_value = 60

    return return_value

#get torsion n_value

def get_torsion_n_value(atom, mol):
    pass

#function to get the torsion 
#The torsional terms for two bonds IJ and KL connected via a common bond JK
def get_torsion(torsional_par, torsion_n_value, fie_equi, fie):
    return (1/2)*torsional_par*(1- math.cos(torsion_n_value*fie_equi)*math.cos(torsion_n_value*fie))

#get the Inversion aka improper torsion Ew


#get inverion parameter

def get_inversion_parameter(atom_symbol,j_type, j_neighbour):
    return_value = [None,None,None, None]
    if ((j_type == "C_R" or j_type == "C_2" ) and (j_neighbour == "O_2")):

        return_value[0]= 1#C0
        return_value[1]= -1#C1
        return_value[2]= 0#C2
        return_value[3]=50/3 #Kijkl
    
    elif (j_type == "C_R" or j_type == "C_2" or j_type == "N_2" or j_type == "N_R" or j_type == "O_2" or j_type == "O_R") :
        return_value[0]= 1
        return_value[1]= -1
        return_value[2]= 0
        return_value[3]=6/3

    elif(atom_symbol == "P" or atom_symbol == "As" or atom_symbol =="Sb" or atom_symbol == "Bi"):
        
        if(atom_symbol == "P"):
            w0 = 84.4339
        elif(atom_symbol == "As"):
            w0 = 86.97305
        elif(atom_symbol == "Sb" ):
            w0 = 87.7047
        elif(atom_symbol == "Bi" ):
            w0 = 90
        return_value[2] = 1
        return_value[1] = -1*return_value[2]*math.cos(w0)
        return_value[0] = -(return_value[1]*math.cos(w0)+return_value[2]*math.cos(2*w0))
        return_value[6] = 22/(return_value[0]+return_value[1]+return_value[2])/3
    else:
        return_value = 0

    return return_value




#get the Inversion aka improper torsion Ew

def get_inversion(C0,C1,w,C2):
    return C0 + C1*math.cos(w)+ C2*math.cos(2*w)


#get van der waals pair contribution

def get_vdW(xi,xj,r,Di,Dj):
    Dij = math.sqrt(Di*Dj)
    xij= math.sqrt(xi*xj)
    return Dij*(-2*(xij/r)^6+(xij/r)^12)
