from rdkit import Chem 
import os 
from rdkit import RDConfig
import sys 
import kora.install.rdkit 
from rdkit.Chem import AllCHem 
import py3Dmol
import copy
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole 
from rdkit.Chem import AllChem, TorsionFingerprints
from rdkit.Chem import rdBase
from rdkit.Chem import rdMolAlign 
from rdkit.Chem import rdMolDescriptors
import os 
import sys
from rdkit.Chem import PandasTools 
from rdkit import RDConfig
from ipywidgets import interact, fixed

class fileUploader:
    def __init__(self, path1, path2):
        self.path1 = path1 
        self.path2 = path2
        #self.smilename =  smilename
    
    # def UploadSDF(self, remove, Fingerprints, smilename):

    #def UploadSDF(self, path):
    #    Fileupload = os.path.join(RDConfig,f"{path}")
    #    SdfLoaded = PandasTools.LoadSDF(Fileupload, smilesName=self.smilename, molColName="Molecule",
    #                            includeFingerprints=self.Fingerprints, removeHs=self.remove, strictParsing=True)
    #    return SdfLoaded
    
    def UploadSDF(self, path1, path2):
        sdf = Chem.SDMolSupplier(path1)
        write = Chem.SDWrite(path2)
        for mol in sdf:
            number = mol.GetProp('_Name')
            mol.SetProp('ID', number)
            write.write(mol)
        write.flush
        write.show

        mol1 = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol1)
        return mol1

class MoleculeDisplay():
    def __init__(self, molecule, nconf=None):
        self.molecule = molecule 
        self.nconf = nconf

    #def GetConformers(self, path):
    #    atoms = [a for a in Chem.SDMolSupplier(path) if a != None][:6]
    #    for atom in atoms:
    #        atom.RemoveAllConformers()
    #    copy.deepcopy([Chem.AddHs(a) for a in atoms])

    def GenConformers(self, molecule, nconf):
        results = AllChem.MMFFOptimizeMoleculeConfs(molecule)
        for i in len(molecule):
            print(f"\n Result [{i}]: ", results[i])
        parameters = AllChem.ETKDG()
        AllChem.EmbedMultipleConfs(molecule, numConfs = nconf , params = parameters)
        return molecule
    
    def GetConformersData(self, molecule, rms1=None, rms2=None, confId=-1):
        rmslist = []
        AllChem.AlignMolConformers(molecule, RMSlist=rmslist)
        rms = AllChem.GetConformerRMS(molecule, rms1, rms2, prealigned=True)
        print(f"RMS [{rms1}]-[{rms2}] = {rms}")

        for i in len(rmslist):
            print(f"\n RMS[{i}]: ", rmslist[i])
        
        p = py3Dmol.view(width=400,height=400)
        mb = Chem.MolToMolBlock(m,confId=confId)
        p.removeAllModels()
        p.addModel(mb,'sdf')
        p.setStyle({'stick':{}})
        p.setBackgroundColor('0xeeeeee')
        p.zoomTo()
        #interact(GetConformers, m=fixed(m1),p=fixed(p),confId=(0,m1.GetNumConformers()-1));
        return p.show()
         