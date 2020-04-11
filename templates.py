main = """# OS generated files #
######################
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Miscellanea #
###############
__pycache__/
.vscode
"""

freecad = """# FreeCAD generated files #
###########################
*.FCStd1"""

kicad = """# KiCAD generated files #
#########################
# Temporary files
*.000
*.bak
*.bck
*.kicad_pcb-bak
*.sch-bak
*~
_autosave-*
*.tmp
*-save.pro
*-save.kicad_pcb
fp-info-cache

# Netlist files (exported from Eeschema)
*.net

# Autorouter files (exported from Pcbnew)
*.dsn
*.ses"""

c = """### C ###
# Prerequisites
*.d

# Object files
*.o
*.ko
*.obj
*.elf

# Linker output
*.ilk
*.map
*.exp

# Precompiled Headers
*.gch
*.pch

# Libraries
*.lib
*.a
*.la
*.lo

# Executables
*.out

# Debug files
*.dSYM/
*.su
*.idb
*.pdb
"""

programs = {"freecad": freecad, "kicad": kicad, "c": c}
