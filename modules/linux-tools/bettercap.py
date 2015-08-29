#!/usr/bin/env python
#####################################
# Installation module for Bettercap
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Ari Davies (@kussic)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update bettercap - a (much) better Ettercap"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://gist.githubusercontent.com/kussic/72697145cfcf3238a602/raw/e80f0922524eeb50a123dce49c71588fc31872c2/bettercap.sh"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="bettercap"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="ruby-dev libpcap-dev"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="gem install bettercap"
