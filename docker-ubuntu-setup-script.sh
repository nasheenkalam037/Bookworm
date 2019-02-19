#!/bin/bash

echo =================================================
echo Running the Docker Ubuntu Setup Script for ECE651
echo =================================================

echo 
echo 
echo ==============================================
echo Installing Python 3 and Misc/Required Packages
echo ==============================================
# set noninteractive installation
export DEBIAN_FRONTEND=noninteractive
#install tzdata package
apt update && apt install -y tzdata
apt update && apt install -y curl wget gnupg2 gcc musl-dev python3
echo 
echo 
echo ==============================================
echo Installing Postgres 11
echo ==============================================
# INSTALL POSTGRES
export RELEASE=$(cat /etc/os-release  | grep VERSION_CODENAME  | cut -d= -f2)
echo "deb http://apt.postgresql.org/pub/repos/apt/ ${RELEASE}"-pgdg main 11 | tee  /etc/apt/sources.list.d/pgdg.list
cat /etc/apt/sources.list.d/pgdg.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
apt update && apt search postgresql-11
echo exit 0 > /usr/sbin/policy-rc.d
apt update && apt install -qq -y postgresql-11 postgresql-server-dev-11 libpq-dev
echo 
echo 
echo ==============================================
echo Installing Nodejs
echo ==============================================
# INSTALL NODEJS
curl -sL https://deb.nodesource.com/setup_10.x | bash -
apt update && apt install -qq -y nodejs
#
#
echo 
echo 
echo ==============================================
echo Testing Installed Versions of Software
echo ==============================================
# Check versions of software
node --version
python3 --version
psql --version
# 
# 
echo 
echo 
echo ==============================================
echo Setting up Database User and new Database
echo ==============================================
# SWITCH TO postgres USER AND SETUP USER TO CONNECT
su postgres
/etc/init.d/postgresql start
psql --command "CREATE USER $POSTGRES_USER WITH SUPERUSER PASSWORD '$POSTGRES_PASSWORD';"
createdb -O $POSTGRES_USER $POSTGRES_DB
exit