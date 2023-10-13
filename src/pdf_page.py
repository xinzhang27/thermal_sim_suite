from pathlib import Path

import fitz
from nicegui import app, ui


def content() -> None:
    # get file names in the folded pdf_files
    file_names = Path.cwd().parent.joinpath("static").glob('*.pdf')
    with ui.right_drawer(fixed=True).style('background-color: #ebf1fa').props('bordered') as right_drawer:
        ui.label("PDF Files").classes("font-bold text-lg")
        pdf_list = [file_name.name for file_name in file_names]
        pdf = ui.radio(pdf_list, value=pdf_list[0], on_change=lambda: (load_pdf.refresh(), load_meta_data.refresh()))

        @ui.refreshable
        def load_meta_data() -> None:
            pdf_file = fitz.open(Path.cwd().parent.joinpath("static").joinpath(pdf.value))
            pdf_meta_data = pdf_file.metadata
            pdf_file.close()
            print(pdf_meta_data)
            ui.markdown(str(pdf_meta_data))

        load_meta_data()

    @ui.refreshable
    def load_pdf() -> None:
        ui.html(f"""
                    <div class="container w-full">
                        <iframe class="w-full h-screen" src="
                        {app.add_static_file(local_file=Path.cwd().parent.joinpath("static").joinpath(pdf.value))}" 
                        type='application/pdf'></iframe>
                    </div>
                """).classes("w-full")

    load_pdf()
