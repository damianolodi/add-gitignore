# Add gitignore

_Add gitignore_ is a simple Python script useful to help with the creation of `.gitignore` files for new and existing Git projects.

## Examples
Let's suppose that you have a project called `my-project` wherever you want on your system and you are using KiCad. The simplest way to add a `.gitignore` to that project is to `cd` into it and typing

```
add-gitignore.py -h kicad
```

This will create a new `.gitignore` file (or append content to the one that already exists) containing the common template and the KiCad template. For more information on what _templates_ are, read the [documentation](#documentation).

## Dependencies
The script is based on Python and it is tested on my machine with version 3.7.4. Only the `os` and `sys` modules are used, so no other dependency is needed.

## Installation
The installation process is correct for _macOS_ and is very similar for _Linux_. For Windows, the process is similar but I have not a Windows machine and I cannot test the installation.

First of all, `cd` where you want to store the script and clone the repository using
```bash
git clone https://github.com/damianolodi/add-gitignore.git
```

Then, you should change the _shebang_, the very first line of the script which is telling where the Python interpreter is located on your system. The one provided in the script is correct for the Anaconda distribution installed on macOS. The simplest way to know where Python is located on your system is typing
```bash
which python3
```
on your terminal. So, for example on _Linux_ the command should return `/usr/bin/env python3`. This means that you should change the first line of the script with
```py
#!/usr/bin/env python3
```

You should also make the script file executable. To do that, `cd` into the script direcotry and type the following command
```bash
chmod +x add-gitignore.py
```

Finally, to be able to call the script from whichever place on your system, you should add the script directory to your `PATH`. Type the following on your terminal:
```bash
cd
nano .bashrc
```
and add the following at the end of the file
```
# Add Automation directory to the PATH
export PATH="$PATH:<your-path>/add-gitignore"
```
where `<your-path>` is the path in which you choose to place the script.

Finally, close and reopen the terminal or use `source .bashrc` to apply changes.

## Documentation

The basic way in which the _add gitignore_ script can be called once correctly installed is 
```
add-gitignore.py <path> <program-1> <program-2> ...
```
where:

- `<path>` should be the path in which the `.gitignore` file should be created. You can replace this with `-h` (stand for _here_) to tell the script that you want the new file in the current directory.
- `<program-1> <program-2> ...` is the list of program that you will be using in your project. Each program is associated with a template that contains a list of files and folders to be added to the `.gitinore` file. This list is optional. If no program name is passed to the script, only the _main_ template will be used.

### List of templates
In the following, you can find the list of supported programs/templates. To see the exact files and folders associated with each template, check the content of the `templates.py` file.

- `main` &rarr; This is the base template included every time the script is called. It is taken from this [gist](https://gist.github.com/octocat/9257657) on the _Octocat_ Github profile and is design to include common files that should not be included in the project history.
- `kicad` &rarr; [KiCad](https://www.kicad-pcb.org/) is an open-source EDA program used PCB design.
- `freecad` &rarr; [FreeCAD](https://www.freecadweb.org/) is an open-source CAD program.

### Working Principles
If you want to know the working principles for the script and the reason for
some design choice refer to the [project page](https://damianolodi.com/project/add-gitignore) on my website.

## License
_Add gitignore_ is released under the [MIT License](https://github.com/damianolodi/add-gitignore/blob/master/LICENSE).
