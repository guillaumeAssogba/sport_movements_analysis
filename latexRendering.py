from pylatex import Document, Section, Subsection, Command, Figure, Table, Tabular
from pylatex.utils import italic, NoEscape
import os

def fill_document(doc):
    """Add a section, a subsection and some text to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    with doc.create(Section('A section')):
        doc.append('Some regular text and some ')
        doc.append(italic('italic text. '))

        with doc.create(Subsection('A subsection')):
            doc.append('Also some crazy characters: $&#{}')
            
def fillLoadingsregression(doc, loadings):
    with doc.create(Subsection('Regressions using PCA\'s loadings and performance ')):
        with doc.create(Figure(position='h!')) as loadings_pic:
            for i in range(3):
                loadings_pic.add_image(loadings[i], width='150px')
            loadings_pic.add_caption('Title 1')
            
def varianceExplainedTable(doc, pcs, name ):
    doc.append('By applying the PCA to the sportsmen\'s dataset, the first three PCs were computed and explain more than 95\% of the variance for each body part.')
    doc.append('The percentage of variance explained by the PCs are shown in Table 1.')
    with doc.create(Table(position='h!')) as table:
        with doc.create(Tabular('ccc')) as tabular:
            tabular.add_hline()
            tabular.add_row(('Variable', 'PC number', 'Variance explained'))
            
            for i in range(len(pcs)):
                tabular.add_hline()
                tabular.add_row((name[i],'',''))
                tabular.add_hline()
                for j in range(len(pcs[0])):
                    tabular.add_row(('','PC'+str(j+1),pcs[i][j]))
        table.add_caption("Percent variation explained for the first "+ str(len(pcs[0])) +" Principle Components of the rugby players’ body variables")

def PCAfigures(doc, pca):
    doc.append('The representation of the projections of the data along the three axes is then performed as represented in the Figure 1.')
    with doc.create(Figure(position='h!')) as pca_pic:
        for i in range(3):
            pca_pic.add_image(pca[i], width='150px')
        pca_pic.add_caption('Projection of the PC scores of respectively the variable A, variable B and variable C')
    
def fillPCArepresentation(doc, pca, pcs, name):
    with doc.create(Subsection('PCA application ')):
        varianceExplainedTable(doc, pcs, name)
        PCAfigures(doc, pca)
        
def fillPca(doc, loadings, pcs, name):
    with doc.create(Section('Statistical Analysis')):
        doc.append('This part describe the different results obtaining by applying the PrinciPal Components analysis to the body movement dataset. ')
    fillPCArepresentation(doc, pca, pcs, name)
    #fillLoadingsregression(doc, loadings)

if __name__ == '__main__':
    nb = 3
    loadings = []
    pca = []
    pcs = [[82.7, 13.4, 2.0],[98.9, 0.8, 0.1], [98.6, 0.9, 0.3]]
    name = ['variable A', 'variable B', 'variable C']
    print(len(pcs))
    for i in range(nb):
        #loadings.append(os.path.join(os.path.dirname(__file__), 'plot\Regression1\DistLoadingvar1PC' + str(i+1) +'.png'))
        pca.append(os.path.join(os.path.dirname(__file__), 'plot\PCArepresentation\PCsVar' + str(i+1) +'.png'))
    
    # Basic document
    geometry_options = {
        "head": "40pt",
        "margin": "1in",
        "bottom": "0.6in"
    }
    doc = Document('report/basic', geometry_options=geometry_options)
    fillPca(doc, loadings, pcs, name)

    doc.generate_pdf(clean_tex=False)