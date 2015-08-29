#!/usr/bin/env python
#####################################
# Installation module for NFSshell
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Ari Davies (@kussic)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update nfsshell - a handy NFS exploration tool"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/NetDirect/nfsshell.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="nsfshell"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="libreadline6 libreadline6-dev libncurses5-dev"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make"
