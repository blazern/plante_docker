#!/bin/bash
set -e

test $USER_PASSWORD

createuser main_user
createdb main
psql -c "GRANT ALL ON schema public TO main_user;"
psql -c "ALTER USER main_user WITH SUPERUSER;"
psql -c "ALTER USER main_user with encrypted password '$USER_PASSWORD'";
