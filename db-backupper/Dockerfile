FROM python:3.8

COPY main.py /main.py

# Declare all expected args
ARG BACKUPS_DIR_PATH
ARG BACKUPS_HOUR_MINUTE
ARG PSQL_URL

# Test that all declared args are provided
RUN test $BACKUPS_DIR_PATH && \
    test $BACKUPS_HOUR_MINUTE && \
    test $PSQL_URL

RUN apt-get update && \
    apt install -y postgresql-client

ENV BACKUPS_DIR_PATH $BACKUPS_DIR_PATH
ENV BACKUPS_HOUR_MINUTE $BACKUPS_HOUR_MINUTE
ENV PSQL_URL $PSQL_URL

CMD python3 /main.py \
    --out-folder="$BACKUPS_DIR_PATH" \
    --psql-url=$PSQL_URL \
    --when="$BACKUPS_HOUR_MINUTE"
