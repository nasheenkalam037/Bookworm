#!/bin/bash

echo =================================================
echo Running the Docker Ubuntu Setup Script for ECE651
echo =================================================


# set noninteractive installation
export DEBIAN_FRONTEND=noninteractive
#install tzdata package
apt install -y tzdata
apt update && apt install -y curl wget gnupg2 gcc musl-dev python3
# INSTALL POSTGRES
export RELEASE=$(cat /etc/os-release  | grep VERSION_CODENAME  | cut -d= -f2)
echo "deb http://apt.postgresql.org/pub/repos/apt/ ${RELEASE}"-pgdg main | tee  /etc/apt/sources.list.d/pgdg.list
cat /etc/apt/sources.list.d/pgdg.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
apt update
apt search postgresql-11
echo exit 0 > /usr/sbin/policy-rc.d
apt install -qq -y postgresql-11 postgresql-server-dev-11 libpq-dev
# INSTALL NODEJS
curl -sL https://deb.nodesource.com/setup_10.x | bash -
apt install -qq -y nodejs
#
#
# Check versions of software
node --version
python3 --version
psql --version
# 
# 
# SWITCH TO postgres USER AND SETUP USER TO CONNECT
su postgres
/etc/init.d/postgresql start
psql --command "CREATE USER $POSTGRES_USER WITH SUPERUSER PASSWORD '$POSTGRES_PASSWORD';"
createdb -O $POSTGRES_USER $POSTGRES_DB
exit