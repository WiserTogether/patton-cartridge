# env.sh - sets up environment for the project
#
# do not modify this file
# see etc/environment.sh for more details
#
export PROJECT_HOME_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ -f "${PROJECT_HOME_DIR}/etc/environment.sh" ]; then
    . ${PROJECT_HOME_DIR}/etc/environment.sh
fi

