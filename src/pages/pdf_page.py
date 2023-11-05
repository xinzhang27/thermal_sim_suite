from pathlib import Path

import fitz
import paramiko
from nicegui import app, ui

from src.backend.cluster import Cluster

hostname = Cluster.hostname
username = Cluster.username
password = Cluster.password
python_path = Cluster.python_path
wd = "/home/zhangxin/Projects/pdf_analyzer"


def upload_pdf(local_file) -> None:
    remote_file_path = f"{wd}/files/{local_file.name}"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port=22, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.put(local_file, remote_file_path)
    sftp.close()
    ssh.close()
    ui.notify(f"Upload {local_file.name} to {remote_file_path}")


def extract_refs(local_file) -> None:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port=22, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(f"{python_path} {wd}/ref_extract.py {wd}/files/{local_file.name}")
    print(stdout.read().decode("utf-8"))
    ui.notify(stdout.read().decode("utf-8"))
    ssh.close()


def extract_tables(local_file) -> None:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port=22, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(f"{python_path} {wd}/table_extract.py {wd}/files/{local_file.name}")
    print(stdout.read().decode("utf-8"))
    ui.notify(stdout.read().decode("utf-8"))
    ssh.close()


def show_tables(local_file) -> None:
    pass


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
        ui.button("Upload",
                  on_click=lambda: upload_pdf(local_file=Path.cwd().parent.joinpath("static").joinpath(pdf.value)))
        ui.button("Get References",
                  on_click=lambda: extract_refs(local_file=Path.cwd().parent.joinpath("static").joinpath(pdf.value)))

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
