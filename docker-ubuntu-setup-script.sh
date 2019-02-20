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
apt-get update && apt-get install -yq tzdata software-properties-common \
    curl wget gnupg2 apt-transport-https \
    ca-certificates
echo 
echo 
if [[ -z "${POSTGRES_11}" ]]; then
    echo ==============================================
    echo Installing Postgres 10
    echo ==============================================
    echo exit 0 > /usr/sbin/policy-rc.d
    apt-cache show postgresql-10
    apt-get update && apt-get install -yq postgresql-10 postgresql-server-dev-10 libpq-dev
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
    apt-get update && apt-get install -yq postgresql-11 postgresql-server-dev-11 libpq-dev
fi

echo 
echo 
echo ==============================================
echo Installing Python3 and Pip3
echo ==============================================
apt-get install -yq python3-pip python3
#
#
echo 
echo 
echo ==============================================
echo Installing Nodejs
echo ==============================================
curl -sL https://deb.nodesource.com/setup_10.x | bash -
apt-get update && apt-get install -yq nodejs
#
#
echo 
echo 
echo ==============================================
echo Installing WebDriver and Chromium
echo ==============================================
# Taken from https://www.blazemeter.com/blog/how-to-run-selenium-tests-in-docker
# Use above when creating the docker image
curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
echo "deb https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
apt-get update
apt-get install -yq \
	google-chrome-stable \
	fontconfig \
	fonts-ipafont-gothic \
	fonts-wqy-zenhei \
	fonts-thai-tlwg \
	fonts-kacst \
	fonts-symbola \
	fonts-noto \
	--no-install-recommends

# chromeDriver v2.35
wget -q "https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/bin/chromedriver
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
