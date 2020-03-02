# Support desktop.


## Installation on Ubuntu server

### Soft

    sudo apt-get update
    sudo apt-get install python3 python3-venv python3-pip python3-wheel git pip npm

    export LC_ALL="en_US.UTF-8"
    export LC_CTYPE="en_US.UTF-8"
    sudo dpkg-reconfigure locales

### Project

    git clone git@bitbucket.org:wezom/support.git
    cd support
    ./bin/install

    
    
## Start web server 

    ./manage.py runserver 8080 
    or ./bin/serv

## Start teleramm bot

    ./bin/tbot