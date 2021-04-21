FROM openjdk:16-jdk

# Declare all expected args
ARG BINARY_PATH_APP
ARG PSQL_HOSTNAME
ARG PSQL_PASSWORD
ARG JWT_SECRET

# Test that all declared args are provided
RUN test $BINARY_PATH_APP && \
    test $PSQL_HOSTNAME && \
    test $PSQL_PASSWORD && \
    test $JWT_SECRET

# Create live config
RUN echo { >> config.json \
  && echo \"psql_url\":\"postgresql://$PSQL_HOSTNAME/main\", >> config.json \
  && echo \"psql_user\":\"main_user\", >> config.json \
  && echo \"psql_pass\":\"$PSQL_PASSWORD\", >> config.json \
  && echo \"db_connection_attempts_timeout_seconds\": 180, >> config.json \
  && echo \"jwt_secret\":\"$JWT_SECRET\" >> config.json \
  && echo } >> config.json
RUN echo "app config: " && cat config.json

# Declare env vars used in CMD
ENV BINARY_PATH_APP $BINARY_PATH_APP

# Run tests and start the server app.
CMD java -jar $BINARY_PATH_APP --config-path config.json
