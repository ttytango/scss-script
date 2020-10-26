import os
from pathlib import Path

from directories import scss, dir_dict
from write_files import remove_affix


main_dir = scss
root_dir = Path("scss")
main_dir_names = dir_dict.keys()

main_file = "main.scss"


def main():
    for dir_name in main_dir_names:
        dir = root_dir / dir_name

        try:
            dir.mkdir(parents=True)
            print("Directory ", dir, " created")
        except FileExistsError:
            print("Directory ", dir, "already exists")

            if not dir.exists():
                dir.mkdir()

                print("Directory ", dir, " Created ")
            else:
                print("Directory ", dir, " already exists")

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

            with open(file_path, "w") as file_handle:
                file_handle.write("")

            import_statement += f'{remove_affix(file)}";\n'

        import_statement += "\n"
    filename = root_dir / main_file





    # import_statement = '@import "' + main_dir_names[0] + '/' + remove_affix(abstracts[0], abstracts) + '";\n' + \
    #                    '@import "' + main_dir_names[0] + '/' + remove_affix(abstracts[1], abstracts) + '";\n' + \
    #                    '@import "' + main_dir_names[0] + '/' + remove_affix(abstracts[2], abstracts) + '";\n\n' + \
    #                    '@import "' + main_dir_names[1] + '/' + remove_affix(base[0], base) + '";\n' + \
    #                    '@import "' + main_dir_names[1] + '/' + remove_affix(base[1], base) + '";\n' + \
    #                    '@import "' + main_dir_names[1] + '/' + remove_affix(base[2], base) + '";\n' + \
    #                    '@import "' + main_dir_names[1] + '/' + remove_affix(base[3], base) + '";\n\n' + \
    #                    '@import "' + main_dir_names[2] + '/' + remove_affix(components[0], components) + '";\n' + \
    #                    '@import "' + main_dir_names[2] + '/' + remove_affix(components[1], components) + '";\n' + \
    #                    '@import "' + main_dir_names[2] + '/' + remove_affix(components[2], components) + '";\n' + \
    #                    '@import "' + main_dir_names[2] + '/' + remove_affix(components[3], components) + '";\n\n' + \
    #                    '@import "' + main_dir_names[3] + '/' + remove_affix(layouts[0], layouts) + '";\n' + \
    #                    '@import "' + main_dir_names[3] + '/' + remove_affix(layouts[1], layouts) + '";\n' + \
    #                    '@import "' + main_dir_names[3] + '/' + remove_affix(layouts[2], layouts) + '";\n' + \
    #                    '@import "' + main_dir_names[3] + '/' + remove_affix(layouts[3], layouts) + '";\n' + \
    #                    '@import "' + main_dir_names[3] + '/' + remove_affix(layouts[4], layouts) + '";\n\n' + \
    #                    '@import "' + main_dir_names[4] + '/' + remove_affix(pages[0], pages) + '";\n' + \
    #                    '@import "' + main_dir_names[4] + '/' + remove_affix(pages[1], pages) + '";\n' + \
    #                    '@import "' + main_dir_names[4] + '/' + remove_affix(pages[2], pages) + '";\n'

    with open(filename, "w") as f:
        f.writelines(import_statement)


if __name__ == '__main__':
    main()
    file_make()
