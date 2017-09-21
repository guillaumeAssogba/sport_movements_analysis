from pylatex import Document, Section, Subsection, Figure, Table, Tabular, LineBreak, Package
from pylatex.utils import italic
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
            
def fillLoadingsregression(doc, loadings, correl, nb, nbPca, nbPerf, name):
    with doc.create(Subsection('Regressions using PCA\'s loadings and performance ')):
        for i in range(nb):
            correlStr = ""
            with doc.create(Figure(position='H')) as loadings_pic:
                for j in range(nbPca*nbPerf):
                    if(j%3 == 0 and j>0):
                        loadings_pic.append(LineBreak())
                    loadings_pic.add_image(loadings[i][j], width='150px')
                    correlStr = correlStr + str(correl[i][j]) + ', '
                loadings_pic.add_caption('regressions between performance values and the body variable' + name[i] +'\'s loadings. (R squared is respectively equals to [' + correlStr + '])')

        
def varianceExplainedTable(doc, pcs, name, nbPca, nb ):
    doc.append('By applying the PCA to the sportsmen\'s dataset, the first three PCs were computed and explain more than 95% of the variance for each body part.')
    doc.append('The percentage of variance explained by the PCs are shown in Table 1.')
    with doc.create(Table(position='h!')) as table:
        with doc.create(Tabular('ccc')) as tabular:
            tabular.add_hline()
            tabular.add_row(('Variable', 'PC number', 'Variance explained'))
            for i in range(nb):
                print(pcs.shape)
                tabular.add_hline()
                tabular.add_row((name[i],'',''))
                tabular.add_hline()
                for j in range(nbPca):
                    tabular.add_row(('','PC'+str(j+1), pcs[nbPca*i+j]))
        table.add_caption("Percent variation explained for the first "+ str(nbPca) +" Principle Components of the players’ body variables")

def PCAfigures(doc, pca, nb):
    doc.append('The representation of the projections of the data along the three axes is then performed as represented in the Figure 1.')
    with doc.create(Figure(position='H')) as pca_pic:
        for i in range(nb):
            if(i%3 ==0 and i>0):
                pca_pic.append(LineBreak())
            pca_pic.add_image(pca[i], width='150px')
        pca_pic.add_caption('representation of PC scores of the body variables')

def fillBestWorst(doc, data, nb, nbPca):
    with doc.create(Subsection('PC scores of the players\' groups')):
        doc.append('The PC scores of the groups formed by the K-means method were then plotted next to the PC scores of the kickers shown previously.')
        with doc.create(Figure(position='H')) as bestWorst_pic:
            for i in range(nb*nbPca):
                if(i%3 ==0 and i>0 ):
                    bestWorst_pic.append(LineBreak())
                bestWorst_pic.add_image(data[i], width='150px')
            bestWorst_pic.add_caption('PC scores of the body variables for the different PCs. the sportsmen with the best (respectively the worst) performance followed dashed green lines (respectively dased red lines).')

def fillstdDeviation(doc, data, nb, nbPca):
    with doc.create(Subsection('projections with the standard deviation of PCs\' loadings')):
        doc.append('Finally, the data was then projected to the space of the first three variables. The loadings\' weigth for each PC was then highlighted by observing the impact of their standard deviation on the projections.')
        with doc.create(Figure(position='H')) as stdDev_pic:
            print(data)
            for i in range(nb*nbPca):
                if(i%3 ==0 and i>0):
                    stdDev_pic.append(LineBreak())
                stdDev_pic.add_image(data[i], width='150px')
            stdDev_pic.add_caption('Projections of the body variables on the PCS axis  for highlighting the impact of the standard deviations of the PCs\' loadings.')
        
def fillPCArepresentation(doc, pca, pcs, name, nbPca, nb, algorithm):
    with doc.create(Subsection('PCA application ')):
        varianceExplainedTable(doc, pcs, name, nbPca, nb)
        if algorithm:
            PCAfigures(doc, pca, nb)
        
def fillPca(doc, pca, loadings, pcs, bestAndWorst, stdDev, name, correl, nbPerf, nbPca, nb, algorithm):
    with doc.create(Section('Statistical Analysis')):
        doc.append('This part describe the different results obtaining by applying the PrinciPal Components analysis to the body movement dataset. ')        
        fillPCArepresentation(doc, pca, pcs, name, nbPca, nb, algorithm[0])
        if algorithm[2]:
            fillBestWorst(doc, bestAndWorst, nb, nbPca)
        if algorithm[3]:
            fillstdDeviation(doc, stdDev, nb, nbPca)
        if algorithm[1]:
            fillLoadingsregression(doc, loadings, correl, nb, nbPca, nbPerf, name)

def launchReport(nb, nbPca, nbPerf, varName, pcs, correl, algorithm):
    loadings = []
    bestAndWorst = []
    stdDev = []
    pca = []
    for i in range(nb):
        load = []
        if algorithm[1]:
            for j in range(nbPerf):
                for k in range(nbPca):
                    load.append(os.path.join(os.path.dirname(__file__), 'plot\loadings\perf' + str(j) +'var' + str(i+1) + 'PC'+ str(k+1) +'.png'))
            loadings.append(load)
        if algorithm[0]:
            pca.append(os.path.join(os.path.dirname(__file__), 'plot\PCArepresentation\PCsVar' + str(i+1) +'.png'))
        if algorithm[2] or algorithm[3]:
            for j in range(nbPca): 
                if algorithm[2]:
                    bestAndWorst.append(os.path.join(os.path.dirname(__file__), 'plot\PcaBestworst\Var' + str(i+1) + 'PC' + str(j+1) + '.png'))
                if algorithm[3]:
                    stdDev.append(os.path.join(os.path.dirname(__file__), 'plot\PCAstdDeviation\Var' + str(i+1) + 'stdDeviationPC' + str(j+1) + '.png'))
    # Basic document
    geometry_options = {
        "head": "40pt",
        "margin": "1in",
        "bottom": "0.6in"
    }
    doc = Document('report/sportAnalysis', geometry_options=geometry_options)
    doc.packages.append(Package('float'))
    
    fillPca(doc, pca, loadings, pcs, bestAndWorst, stdDev, varName, correl, nbPerf, nbPca, nb, algorithm)

    doc.generate_pdf(clean_tex=False)