import os
from pathlib import Path

from directories import dir_dict
from write_files import remove_affix

main_dir = "scss"
root_dir = Path("scss")
main_dir_names = dir_dict.keys()

main_file = "main.scss"


def main():
    for dir_name in main_dir_names:
        new_dir = root_dir / dir_name

        try:
            new_dir.mkdir(parents=True)
            print("Directory ", new_dir, " created")
        except FileExistsError:
            print("Directory ", new_dir, "already exists")

            if not new_dir.exists():
                new_dir.mkdir()

                print("Directory ", new_dir, " Created ")
            else:
                print("Directory ", new_dir, " already exists")


def file_make():
    """
    :rtype: object
    """

    cwd = Path(os.getcwd())

    target_path = cwd / 'scss'

    while not target_path.exists():
        target_path.mkdir()

    import_statement = ""
    for name, files in dir_dict.items():
        dir_path = target_path / name

        for file in files:
            import_statement += f'@import "{name}/'
            file_path = dir_path / file

            with open(file_path, "a") as file_handle:
                file_handle.write("")

            import_statement += f'{remove_affix(file)}";\n'

        import_statement += "\n"
    filename = root_dir / main_file

    with open(filename, "a") as f:
        f.writelines(import_statement)


if __name__ == '__main__':
    main()
    file_make()
