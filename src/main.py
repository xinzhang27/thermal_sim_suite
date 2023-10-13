from nicegui import app, ui
from pathlib import Path


@ui.page("/")
def index():
    path = app.add_static_file(local_file="./pdf_files/test.pdf")

    with ui.header().classes("justify-between") as header:
        ui.label("Thermal Simulation Suite")

    with ui.footer(value=False) as footer:
        ui.label('Footer')

    with ui.left_drawer().classes("bg-blue-100") as left_drawer:
        ui.label("Left Drawer")

    with ui.element('div').classes("row justify-center") as element:
        ui.label("Thermal Simulation Suite")
        ui.label("Welcome to the Thermal Simulation Suite!")

    ui.link("Materials", target=get_materials).classes("btn btn-primary")

    # @app.get("/{filename}")
    # def get_pdf(filename):
    #     return Path(f"./pdf_files/{filename}").read_bytes()

    # window-height window-width justify-center items-center
    ui.html(f"""
        <div class="window-height window-width row justify-center items-center">
            <iframe src="{path}" width="100%" height="100%" type='application/pdf' frameborder="1"></iframe>
        </div>
    """)
    # ui.image("./pdf_files/test.pdf")
    # ui.image("../static/letter-npj-CXS.png")


@ui.page("/materials")
def get_materials():
    ui.label("Thermal Simulation Suite")
    ui.label("Welcome to the Thermal Simulation Suite!")


ui.run(title="Thermal Simulation Suite", reload=True, native=False)
