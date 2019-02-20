#!/bin/bash

echo =================================================
echo Running the Docker Ubuntu Setup Script for ECE651
echo =================================================
cat /etc/os-release
echo 
echo 
echo ==============================================
echo Installing Python 3 and Misc/Required Packages
echo ==============================================
# set noninteractive installation
export DEBIAN_FRONTEND=noninteractive
#install tzdata package
apt-get update && apt-get install -y tzdata

apt-get update && apt-get install -y curl wget gnupg2

echo 
echo 
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

sleep 2

apt-cache show postgresql-11

echo exit 0 > /usr/sbin/policy-rc.d

apt-get update && apt-get install -y postgresql-11 postgresql-server-dev-11 libpq-dev

echo 
echo 
echo ==============================================
echo Installing Nodejs
echo ==============================================
# INSTALL NODEJS
curl -sL https://deb.nodesource.com/setup_10.x | bash -
apt-get update && apt-get install -y nodejs
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
echo Starting the Postgresql server if needed
/etc/init.d/postgresql start
/etc/init.d/postgresql status
sleep 2
/etc/init.d/postgresql status
su postgres
whoami
psql --command "CREATE USER $POSTGRES_USER WITH SUPERUSER PASSWORD '$POSTGRES_PASSWORD';"
createdb -O $POSTGRES_USER $POSTGRES_DB
exit