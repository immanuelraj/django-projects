#!/bin/sh
echo "Started ------------------------------------------------------"

set -e

export PGUSER=admin
# Perform all actions as $POSTGRES_USER
"${psql[@]}" <<- EOSQL
    CREATE USER postgres WITH SUPERUSER;
    CREATE USER admin WITH SUPERUSER;
    CREATE DATABASE masterdb;
    GRANT ALL PRIVILEGES ON DATABASE masterdb TO admin;
EOSQL

# Load PostGIS into both template_database and $POSTGRES_DB
for DB in masterdb; do
	echo "Loading PostGIS extensions into $DB"
	"${psql[@]}" --dbname="$DB" <<-'EOSQL'
		CREATE EXTENSION IF NOT EXISTS postgis;
EOSQL
done

echo "Done ------------------------------------------------------"