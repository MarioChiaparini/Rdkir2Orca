import py3Dmol
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import PandasTools 
from rdkit.Chem.PandasTools import LoadSDF

path1 = "/Users/mariochiaparini/Desktop/Rdkir2Orca/Molecules/benzene-3D-structure-CT1001419667.sdf"
path2 = "/Users/mariochiaparini/Desktop/Rdkir2Orca/Molecules/SULFURIC-ACID-3D-structure-CT1002595762.sdf"

benzene = LoadSDF(path1, smilesName='SMILES').SMILES
sulfuric_acid = LoadSDF(path2, smilesName='SMILES').SMILES

mol_benzene = Chem.MolFromSmiles(benzene[0])
benzene = Chem.AddHs(mol_benzene)

mol_sulfuric_acid = Chem.MolFromSmiles(sulfuric_acid[0])

combine = Chem.CombineMols(benzene, mol_sulfuric_acid)
w1 = Chem.SDWriter('/Users/mariochiaparini/Desktop/Rdkir2Orca/Molecules/foo.sdf')
w1.write(combine)
w1.close() 