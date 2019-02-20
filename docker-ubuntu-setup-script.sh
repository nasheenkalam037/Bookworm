#!/bin/bash

echo =================================================
echo Running the Docker Ubuntu Setup Script for ECE651
echo =================================================
cat /etc/os-release
echo 
echo 
echo ==============================================
echo Installing Required Packages
echo ==============================================
# set noninteractive installation
export DEBIAN_FRONTEND=noninteractive
#install tzdata package
apt-get update && apt-get install -y tzdata
apt-get update && apt-get install -y curl wget gnupg2
echo 
echo 
if [[ -z "${POSTGRES_11}" ]]; then
    echo ==============================================
    echo Installing Postgres 10
    echo ==============================================
    echo exit 0 > /usr/sbin/policy-rc.d
    apt-cache show postgresql-10
    apt-get update && apt-get install -y postgresql-10 postgresql-server-dev-10 libpq-dev
    service postgresql start
else
    echo ==============================================
    echo Installing Postgres 11
    echo ==============================================
    # INSTALL POSTGRES
    export RELEASE=$(cat /etc/os-release  | grep VERSION_CODENAME  | cut -d= -f2)
    echo "deb http://apt.postgresql.org/pub/repos/apt/ ${RELEASE}"-pgdg 11 | tee  /etc/apt/sources.list.d/pgdg.list
    cat /etc/apt/sources.list.d/pgdg.list
    wget --quiet https://www.postgresql.org/media/keys/ACCC4CF8.asc
    apt-key add ACCC4CF8.asc
    apt-get update
    apt-cache show postgresql-11
    echo exit 0 > /usr/sbin/policy-rc.d
    apt-get update && apt-get install -y postgresql-11 postgresql-server-dev-11 libpq-dev
fi

echo 
echo 
echo ==============================================
echo Installing Python3 and Pip3
echo ==============================================
apt-get install -y python3-pip python3
#
#
echo 
echo 
echo ==============================================
echo Installing Nodejs
echo ==============================================
curl -sL https://deb.nodesource.com/setup_10.x | bash -
apt-get update && apt-get install -y nodejs
#
#
echo 
echo 
echo ==============================================
echo Installing WebDriver and Chromium
echo ==============================================
# Taken from https://www.blazemeter.com/blog/how-to-run-selenium-tests-in-docker
# Use above when creating the docker image
apt-get update && apt-get install -yq \
    firefox-esr=52.6.0esr-1~deb9u1 \
    chromium=62.0.3202.89-1~deb9u1 \
    xvfb=2:1.19.2-1+deb9u2 \
    xsel=1.2.0-2+b1 \
    unzip=6.0-21 \
    python-pytest=3.0.6-1 \
    libgconf2-4=3.2.6-4+b1 \
    libncurses5=6.0+20161126-1+deb9u2 \
    libxml2-dev=2.9.4+dfsg1-2.2+deb9u2 \
    libxslt-dev \
    libz-dev \
    xclip=0.12+svn84-4+b1
# GeckoDriver v0.19.1
wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz" -O /tmp/geckodriver.tgz \
    && tar zxf /tmp/geckodriver.tgz -C /usr/bin/ \
    && rm /tmp/geckodriver.tgz

# chromeDriver v2.35
wget -q "https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip

# xvfb - X server display
ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \
    && chmod 777 /usr/bin/xvfb-chromium

# create symlinks to chromedriver and geckodriver (to the PATH)
ln -s /usr/bin/geckodriver /usr/bin/chromium-browser \
    && chmod 777 /usr/bin/geckodriver \
    && chmod 777 /usr/bin/chromium-browser
#
#
echo 
echo 
echo ==============================================
echo Testing Installed Versions of Software
echo ==============================================
node --version
python3 --version
pip3 --version
psql --version
# 
# 
echo 
echo 
echo ==============================================
echo Setting up Database User and new Database
echo ==============================================
# SWITCH TO postgres USER AND SETUP USER TO CONNECT
echo Starting the Postgresql server if needed
service postgresql status
service postgresql start
service postgresql status
su - postgres -c "whoami"
su - postgres -c "psql --command \"CREATE USER $POSTGRES_USER WITH SUPERUSER PASSWORD '$POSTGRES_PASSWORD';\""
su - postgres -c "createdb -O $POSTGRES_USER $POSTGRES_DB"
