import math

# Bond strech form 1
#Er= 1/2 * K_ij *(r-r_ij)^2


# Bond strech form 2
#Er = D_ij[e^{- a (r - rij)}-1]^2

Zi , Zj, Zk =0 #effective charges 


#function to get an effective charge

xi, xj, ri , rj , atom_type_bond_radii = 0 # ri +rj

proportionality_constant  = 0.1332

bond_order = 1

bond_order_correction =  -proportionality_constant*(atom_type_bond_radii)*math.log(bond_order) 

electronegativity_correction = ri *rj ((math.sqrt(xi) - math.sqrt(xj))^2 )/(xi *ri + xj*rj)

dissociacion_energy = 70 #kcal/mol (D_ij)
natural_bond_length = atom_type_bond_radii + bond_order_correction + electronegativity_correction #r_ij = ri +rj + rBO + rEN

force_constant = 664.12 * (Zi *Zj)/natural_bond_length^3 

angle = 0 

theta_0=0

C_2 = 1/ (4*(math.sin(theta_0))^2)

C_1 = -4*C_2  * math.cos(theta_0)



betha = 664.12/(natural_bond_length * natural_bond_length)

C_0 = C_2*(2*(math.cos(theta_0))+1)


K_IJK = betha *((Zi*Zk)/natural_bond_length^5) * natural_bond_length * natural_bond_length*[natural_bond_length*natural_bond_length*(1-(math.cos(theta_0))^2) - natural_bond_length^2 * math.cos(theta_0)]

#Angle bend 

angle_bend = K_IJK * [C_0 + C_1 * math.cos(angle) + C_2 * math.cos(2 * angle)]

#torsion
#The torsional terms for two bonds IJ and KL
#connected via a common bond JK is described with a small cosine
#Fourier expansion in

