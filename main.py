import os
from directories import scss, abstracts, base, components, layouts, pages
from write_files import remove_affix

main_dir = scss
root_dir = "scss"
main_dir_names = ["abstracts", "base", "components", "layouts", "pages"]
main_file = "main.scss"


def main():
    for i in range(0, len(main_dir)):
        dirname = str(root_dir) + '/' + str(main_dir_names[i])

        try:
            os.makedirs(dirname)
            print("Directory ", dirname, " created")
        except FileExistsError:
            print("Directory ", dirname, "already exists")

            if not os.path.exists(dirname):
                os.makedirs(dirname)

                print("Directory ", dirname, " Created ")
            else:
                print("Directory ", dirname, " already exists")

    def file_make():
        """
        :rtype: object
        """

        cwd = os.getcwd()

        target_path = os.path.join(cwd, 'scss/abstracts/')
        while not os.path.exists(target_path):
            os.mkdir(target_path)

        filenames = abstracts
        for j in range(0, len(filenames)):
            target_file = os.path.join(target_path, filenames[j])

            file = open(target_file, "w")
            file.write("")
            file.close()

        target_path = os.path.join(cwd, 'scss/base/')

        while not os.path.exists(target_path):
            os.mkdir(target_path)

        filenames = base
        for j in range(0, len(filenames)):
            target_file = os.path.join(target_path, filenames[j])

            file = open(target_file, "w")
            file.write("")
            file.close()

        target_path = os.path.join(cwd, 'scss/components/')

        while not os.path.exists(target_path):
            os.mkdir(target_path)

        filenames = components
        for j in range(0, len(filenames)):
            target_file = os.path.join(target_path, filenames[j])

            file = open(target_file, "w")
            file.write("")
            file.close()

        target_path = os.path.join(cwd, 'scss/layouts/')

        while not os.path.exists(target_path):
            os.mkdir(target_path)

        filenames = layouts
        for j in range(0, len(filenames)):
            target_file = os.path.join(target_path, filenames[j])

            file = open(target_file, "w")
            file.write("")
            file.close()

        target_path = os.path.join(cwd, 'scss/pages/')

        while not os.path.exists(target_path):
            os.mkdir(target_path)

        filenames = pages
        for j in range(0, len(filenames)):
            target_file = os.path.join(target_path, filenames[j])

            file = open(target_file, "w")
            file.write("")
            file.close()

        filename = str(root_dir) + '/' + str(main_file)

        import_statement = '@import "' + main_dir_names[0] + '/' + remove_affix(abstracts[0], abstracts) + '";\n' + \
                           '@import "' + main_dir_names[0] + '/' + remove_affix(abstracts[1], abstracts) + '";\n' + \
                           '@import "' + main_dir_names[0] + '/' + remove_affix(abstracts[2], abstracts) + '";\n\n' + \
                           '@import "' + main_dir_names[1] + '/' + remove_affix(base[0], base) + '";\n' + \
                           '@import "' + main_dir_names[1] + '/' + remove_affix(base[1], base) + '";\n' + \
                           '@import "' + main_dir_names[1] + '/' + remove_affix(base[2], base) + '";\n' + \
                           '@import "' + main_dir_names[1] + '/' + remove_affix(base[3], base) + '";\n\n' + \
                           '@import "' + main_dir_names[2] + '/' + remove_affix(components[0], components) + '";\n' + \
                           '@import "' + main_dir_names[2] + '/' + remove_affix(components[1], components) + '";\n' + \
                           '@import "' + main_dir_names[2] + '/' + remove_affix(components[2], components) + '";\n' + \
                           '@import "' + main_dir_names[2] + '/' + remove_affix(components[3], components) + '";\n\n' + \
                           '@import "' + main_dir_names[3] + '/' + remove_affix(layouts[0], layouts) + '";\n' + \
                           '@import "' + main_dir_names[3] + '/' + remove_affix(layouts[1], layouts) + '";\n' + \
                           '@import "' + main_dir_names[3] + '/' + remove_affix(layouts[2], layouts) + '";\n' + \
                           '@import "' + main_dir_names[3] + '/' + remove_affix(layouts[3], layouts) + '";\n' + \
                           '@import "' + main_dir_names[3] + '/' + remove_affix(layouts[4], layouts) + '";\n\n' + \
                           '@import "' + main_dir_names[4] + '/' + remove_affix(pages[0], pages) + '";\n' + \
                           '@import "' + main_dir_names[4] + '/' + remove_affix(pages[1], pages) + '";\n' + \
                           '@import "' + main_dir_names[4] + '/' + remove_affix(pages[2], pages) + '";\n'

        with open(filename, "w") as f:
            f.writelines(import_statement)

    file_make()


if __name__ == '__main__':
    main()
