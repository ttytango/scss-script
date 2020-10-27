# scss-script

This is an alpha version of my scss script.

This is made using python 3.8.4 but works with the new python 3.9

Simply clone this repo into the root directory of your project and open up your root directory.
Once inside there will be a new folder named scss-script.
Open this folder and run main.py in the terminal (often by right clicking on it and pressing run presuming you have python installed, and it will automatically create an scss folder structure in the project directory, with partials and a main.scss file automatically created for you.
The files that are created will automatically be imported with an @import statement into the main.scss that is created upon running the script.

The script needs to be run from the root directory of the project/ or directory you would like to run it from, or it will create the scss folder in the wrong directory.

### To clone and run this script from the command line:
```
>mkdir <new-project>
>cd <new-project>
    (optional: create a couple of files in the root of <new-directory> with >touch index.html script.js)
>git clone <this-repo>
>python ./scss-script/main.py
>code .
```

### This is meant as a one-shot script to run at the beginning of the project, but the project has just been edited so that the files that are there already should not be overwritten. However, it could cause issues with the import statements if run twice.

Upon creation of the scss files you can delete the entire scss-script folder from your project.
You can use the following command to do so:
```
> rm -rf scss-script/

```

## How to configure the script to suit your project

The directories.py file contains a dictionary data-type named 'dir_dict' with scss sub-directory names to be created on the left-hand side. The contents of the corresponding square brackets represents the key-paired values, and files that will be created.
You can add or take away files in this dictionary, and add or change any of the directory names as long as they are in the same format in the provisional directory.
Again, it is best to use this as a one-shot script to make sure the files are imported into the main.scss file.

### To-do

- Automate some more content
- Package the script
