from rdkit import Chem  
from rdkit.Chem.PandasTools import LoadSDF

path1 = "/Users/mariochiaparini/Desktop/Rdkir2Orca/Molecules/benzene-3D-structure-CT1001419667.sdf"
path2 = "/Users/mariochiaparini/Desktop/Rdkir2Orca/Molecules/SULFURIC-ACID-3D-structure-CT1002595762.sdf"

benzene = LoadSDF(path1, smilesName='SMILES').SMILES
sulfuric_acid = LoadSDF(path2, smilesName='SMILES').SMILES

#smarts = "[C:1](=[0:2])0.[Nh:3]"

#amine_coupling = Chem.CombineMols()

#print(amine_coupling)

combine = Chem.CombineMols(benzene, sulfuric_acid)

