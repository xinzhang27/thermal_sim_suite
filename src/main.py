import data_page
import home_page
import pdf_page
import theme

from nicegui import ui


@ui.page("/")
def index_page() -> None:
    """
    Create the index page.
    :return:
    """
    with theme.frame("Homepage"):
        home_page.content()


@ui.page("/pdf_viewer")
def pdf_viewer_page() -> None:
    """
    Create the pdf viewer page.
    :return:
    """
    with theme.frame("PDF Viewer"):
        pdf_page.content()


@ui.page("/data_analysis")
def data_analysis_page() -> None:
    """
    Create the data analysis page.
    :return:
    """
    with theme.frame("Data Analysis"):
        data_page.content()


ui.run(title="Thermal Simulation Suite", reload=True, native=False)
