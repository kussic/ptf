#!/usr/bin/env python
#####################################
# Installation module for SpoofMAC
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Ari Davies (@kussic)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update SpoofMAC - a MAC address spoofing tool for Linux/OS X/Windows"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/feross/SpoofMAC.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="spoofmac"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="python-setuptools"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python setup.py install"
