import flet as ft
import pandas as pd

def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        # selected_files.value = (
        #     ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        # )
        # selected_files.update()

        # todo https://github.com/flet-dev/examples/blob/main/python/apps/controls-gallery/layout/datatable/01_basic_datatable.py

        dfcoll = None
        for file in e.files:
            # page.add(ft.Text(f"{file.name}  {file.path}  {file.size}"))
            dictt = {'filename': file.name, 'size': file.size}
            df = pd.DataFrame.from_dict(dictt, orient='index')
            df = df.T
            dfcoll = pd.concat([dfcoll, df], axis=0, ignore_index=True)
        print(dfcoll)

        # openfile(files=selected_files.value)

    def openfile(files):
        # Program to read the entire file using read() function
        file = open(files, "r")
        content = file.read()
        print(content)
        file.close()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Column(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ]
        )
    )


ft.app(target=main)
