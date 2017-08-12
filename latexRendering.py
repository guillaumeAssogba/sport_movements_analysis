from pylatex import Document, Section, Subsection, Command, Figure
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
                loadings_pic.add_image(loadings[i], width='200px')
            loadings_pic.add_caption('Title 1')  

def fillPca(doc, loadings):
    with doc.create(Section('Statistical Analysis')):
        doc.append('This part describe the different results obtaining by\
                  applying the PrinciPal Components analysis to the dataset')
    fillLoadingsregression(doc, loadings)

if __name__ == '__main__':
    loadings = []
    loadings.append(os.path.join(os.path.dirname(__file__), 'plot\RegressionDistLoadingvar1PC1.png'))
    loadings.append(os.path.join(os.path.dirname(__file__), 'plot\RegressionDistLoadingvar1PC2.png'))
    loadings.append(os.path.join(os.path.dirname(__file__), 'plot\RegressionDistLoadingvar1PC3.png'))
    
    # Basic document
    geometry_options = {
        "head": "40pt",
        "margin": "1in",
        "bottom": "0.6in"
    }
    doc = Document('report/basic', geometry_options=geometry_options)
    fillPca(doc, loadings)

    doc.generate_pdf(clean_tex=False)