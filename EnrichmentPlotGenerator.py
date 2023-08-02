from pandas import DataFrame, concat
from gseapy import enrichr
from gseapy.plot import dotplot
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import tkinter as tk
from base64 import b64decode
from os import remove
from ico import img
from tkinter import filedialog


class GeneOntologyEnrichment(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Enrichment Plot Generator")
        self.resizable(False, False)
        self.CenterWindow()
        self.setIcon()

        label = tk.Label(self, text="选择基因列表文件：")
        label.grid(row=0, column=0, padx=5, pady=10)

        self.filePath = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.filePath, width=40, state='readonly')
        entry.grid(row=0, column=1, pady=10, columnspan=4)

        button = tk.Button(self, text="打开", command=self.OpenFileDialog)
        button.grid(row=0, column=5, pady=10, padx=10)

        label2 = tk.Label(self, text="待进行的富集：")
        label2.grid(row=1, column=0, padx=5)
        self.goeVar = tk.IntVar(value=1)
        self.keggVar = tk.IntVar(value=1)
        goeCheckbox = tk.Checkbutton(self, text="GO富集", variable=self.goeVar)
        keggCheckbox = tk.Checkbutton(self, text="KEGG富集", variable=self.keggVar)
        goeCheckbox.grid(row=1, column=1, padx=10, columnspan=2)
        keggCheckbox.grid(row=1, column=3, padx=10, columnspan=2)

        generateButton = tk.Button(self, text="一键富集 -> 生成图表", command=self.GenerateGraph)
        generateButton.grid(row=2, column=0, columnspan=6, padx=10, pady=10)

    def setIcon(self):
        tmp = open("tmp.ico", "wb+")
        tmp.write(b64decode(img))
        tmp.close()
        self.iconbitmap("tmp.ico")
        remove("tmp.ico")

    def CenterWindow(self):
        windowWidth = 460
        windowHeight = 130
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        x = (screenWidth - windowWidth) // 2
        y = (screenHeight - windowHeight) // 2
        self.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

    def OpenFileDialog(self):
        filePath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.filePath.set(filePath)

    def GenerateGOEnrichmentGraph(self):
        if (self.goeVar.get() == 1):
            with open(self.filePath.get(), 'r') as fileObject:
                    genelist = [gene.strip('\n') for gene in fileObject.readlines()]

            results = DataFrame()

            for db in ['GO_Biological_Process_2023', 'GO_Cellular_Component_2023', 'GO_Molecular_Function_2023']:
                enr = enrichr(genelist, db, organism='human')
                results = concat([results, enr.res2d[:10]])
            
            mapping = {
                'GO_Biological_Process_2023': 'BP',
                'GO_Cellular_Component_2023': 'CC',
                'GO_Molecular_Function_2023': 'MF'
                }
            
            results['Gene_set'] = results['Gene_set'].replace(mapping)
            results['Number of Genes'] = results['Genes'].apply(lambda x: x.count(';') + 1)
            results['Term'] = results['Term'].apply(lambda x: x[: -12])
            results = results[: : -1]

            plt.figure(figsize=(8, 10))
            plt.title('Top 10 Gene Ontology Enrichment Terms', fontsize=20, fontweight='bold', loc='center')
            plt.xlabel('Number of Genes', fontsize=16)
            plt.ylabel('Term', fontsize=16)

            colors = {'BP': 'blue', "CC": 'red', 'MF': 'green'}

            for i in range(len(results['Term'])):
                plt.barh(list(results['Term'])[i], list(results['Number of Genes'])[i], color=colors[list(results['Gene_set'])[i]], height=0.75)

            legendHandles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colors.values()]
            legendLabels = colors.keys()
            plt.legend(legendHandles, legendLabels, loc='center right')

            plt.xticks(fontsize=16)
            plt.yticks(fontsize=13)
            plt.ylim([-0.5, 29.5])
            plt.savefig('gene_ontology_enrichment_figure.png', bbox_inches='tight', dpi=300)

    def GenerateKEGGEnrichmentGraph(self):
        if (self.keggVar.get() == 1):
            with open(self.filePath.get(), 'r') as fileObject:
                genelist = [gene.strip('\n') for gene in fileObject.readlines()]
            enr = enrichr(genelist, 'KEGG_2021_Human')
            br = ['cornflowerblue', 'red']
            cmap1 = LinearSegmentedColormap.from_list("b2r", br)
            dotplot(enr.res2d, column='Combined Score', title='KEGG', cmap=cmap1, size=60, figsize=(3,5), ofname='kegg_figure.png')

    def GenerateGraph(self):
        self.title("处理中...")
        try:
            self.GenerateGOEnrichmentGraph()
            self.GenerateKEGGEnrichmentGraph()
        
        finally:
            self.title("Enrichment Plot Generator")
        
if __name__ == '__main__':
    app = GeneOntologyEnrichment()
    app.mainloop()