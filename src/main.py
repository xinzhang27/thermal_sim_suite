from nicegui import ui

from core import theme
from pages.info import PageInfo


def generate_page(page):
    @ui.page(page.get("target"))
    def page_content():
        with theme.frame(page.get("text")):
            page.get("page").content()


generate_page(PageInfo.home_page)
generate_page(PageInfo.pdf_page)
generate_page(PageInfo.data_page)
generate_page(PageInfo.results_page)
generate_page(PageInfo.search_page)

ui.run(title="Thermal Simulation Suite", reload=True, native=False, window_size=(1200, 800))
