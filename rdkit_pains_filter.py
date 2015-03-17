# -*- coding: utf-8 -*-

from rdkit import Chem

inf = open("pains.txt", "r")
sub_strct = [ line.rstrip().split(" ") for line in inf ]

smarts = [ line[0] for line in sub_strct]
desc = [ line[1] for line in sub_strct]
dic = dict(zip(smarts, desc))

def pains_filt(mol):
    """
    >>> mol = Chem.MolFromSmiles("c1ccccc1N=Nc1ccccc1")
    >>> checkmol = pains_filt( mol )
    >>> props = [ prop for prop in checkmol.GetPropNames() ]
    >>> props[0]
    'azo_A(324)'
    
    """

    for k,v in dic.items():
        subs = Chem.MolFromSmarts( k )
        if subs != None:
            if mol.HasSubstructMatch( subs ):
                mol.SetProp(v,k)
    return mol


if __name__ == "__main__":
    import doctest
    doctest.testmod()

