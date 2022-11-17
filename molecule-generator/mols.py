from rdkit import Chem 
from rdkit.Chem import PandasTools 
import os 
from rdkit import RDConfig
import sys 
import kora.install.rdkit 
from rdkit.Chem import AllCHem 
import py3Dmol
import copy

class fileUploader:
    def __init__(self, remove, Fingerprints, smilename):
        self.remove = remove 
        self.Fingerprints = Fingerprints
        self.smilename =  smilename
    # def UploadSDF(self, remove, Fingerprints, smilename):

    def UploadSDF(self, path):
        Fileupload = os.path.join(RDConfig,f"{path}")
        SdfLoaded = PandasTools.LoadSDF(Fileupload, smilesName=self.smilename, molColName="Molecule",
                                includeFingerprints=self.Fingerprints, removeHs=self.remove, strictParsing=True)
        return SdfLoaded

class MoleculeDisplay():
    def __init__(self, molecule):
        self.molecule = molecule 
    def GetConformers(self, path):
        atoms = [a for a in Chem.SDMolSupplier(path) if a != None][:6]
        for atom in atoms:
            atom.RemoveAllConformers()
        copy.deepcopy([Chem.AddHs(a) for a in atoms])
        for atom in 