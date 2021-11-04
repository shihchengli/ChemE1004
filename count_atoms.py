#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module is a chemical formula parser.
"""

# A list of the elements, sorted by increasing atomic number
element_list = [
 'X', 'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 
 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 
 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 
 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 
 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 
 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 
 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 
 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 
 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 
 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 
 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 
 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 
 'Mt', 'Ds', 'Rg', 'Cn']

def count_atoms(formula):
    """
    Return a list containing a series of lists of composed elements of the given formula and their corresponding numbers.
    """
    pairs = []
    output = ''
    for atom in element_list:
        if atom in formula:
            # determine the number of atom
            i = formula.index(atom) # the index of atom in formula
            i += len(atom) - 1 # consider the number of character of an  atom
            j = i + 1 # 'j' is a variable to check the number of characters behind 'i' being a number
            while j != len(formula) and formula[j] not in element_list:
                j += 1
            if j == i + 1:
                n_atom = 1
            else:
                n_atom = int(formula[i+1:j])
            pairs.append([atom, n_atom])
            output += ' ' + str(n_atom) + ' ' + atom
    print(formula + ' has' + output)
    return pairs

if __name__ == "__main__":
    chloroquine = 'C18H26ClN3'
    pairs = count_atoms(chloroquine)
