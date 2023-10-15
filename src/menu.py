from nicegui import ui


def menu() -> None:
    """
    This is the menu creator and add link while creating new page
    :return:
    """
    ui.link('Home', '/').classes("text-white")
    ui.link("PDF Viewer", "/pdf_viewer").classes("text-white")
    ui.link("Data Analysis", "/data_analysis").classes("text-white")
    ui.link("Machine Learning", "/machine_learning").classes("text-white")
    ui.link("Heuristic Method", "/heuristic_method").classes("text-white")