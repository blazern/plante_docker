FROM openjdk:16-jdk

# Declare all expected args
ARG BINARY_PATH_APP
ARG LOGS_DIR
ARG IOS_PRIVATE_KEY_PATH
ARG PSQL_HOSTNAME
ARG PSQL_PASSWORD
ARG OSM_PROD_USER
ARG OSM_PROD_PASSWORD
ARG OSM_TESTING_USER
ARG OSM_TESTING_PASSWORD
ARG OFF_PROD_USER
ARG OFF_PROD_PASSWORD
ARG OFF_TESTING_USER
ARG OFF_TESTING_PASSWORD
ARG AWS_S3_BUCKET_NAME
ARG AWS_S3_REGION
ARG AWS_S3_ACCESS_KEY_ID
ARG AWS_S3_SECRET_ACCESS_KEY
ARG JWT_SECRET
ARG METRICS_ENDPOINT

# Test that all declared args are provided
RUN test $BINARY_PATH_APP && \
    test $LOGS_DIR && \
    test $IOS_PRIVATE_KEY_PATH && \
    test $PSQL_HOSTNAME && \
    test $PSQL_PASSWORD && \
    test $OSM_PROD_USER && \
    test $OSM_PROD_PASSWORD && \
    test $OSM_TESTING_USER && \
    test $OSM_TESTING_PASSWORD && \
    test $OFF_PROD_USER && \
    test $OFF_PROD_PASSWORD && \
    test $OFF_TESTING_USER && \
    test $OFF_TESTING_PASSWORD && \
    test $AWS_S3_BUCKET_NAME && \
    test $AWS_S3_REGION && \
    test $AWS_S3_ACCESS_KEY_ID && \
    test $AWS_S3_SECRET_ACCESS_KEY && \
    test $JWT_SECRET && \
    test $METRICS_ENDPOINT

# Create live config
RUN echo { >> config.json \
  && echo \"psql_url\":\"postgresql://$PSQL_HOSTNAME/main\", >> config.json \
  && echo \"psql_user\":\"main_user\", >> config.json \
  && echo \"psql_pass\":\"$PSQL_PASSWORD\", >> config.json \
  && echo \"osm_prod_user\":\"$OSM_PROD_USER\", >> config.json \
  && echo \"osm_prod_password\":\"$OSM_PROD_PASSWORD\", >> config.json \
  && echo \"osm_testing_user\":\"$OSM_TESTING_USER\", >> config.json \
  && echo \"osm_testing_password\":\"$OSM_TESTING_PASSWORD\", >> config.json \
  && echo \"off_prod_user\":\"$OFF_PROD_USER\", >> config.json \
  && echo \"off_prod_password\":\"$OFF_PROD_PASSWORD\", >> config.json \
  && echo \"off_testing_user\":\"$OFF_TESTING_USER\", >> config.json \
  && echo \"off_testing_password\":\"$OFF_TESTING_PASSWORD\", >> config.json \
  && echo \"aws_s3_bucket_name\":\"$AWS_S3_BUCKET_NAME\", >> config.json \
  && echo \"aws_s3_region\":\"$AWS_S3_REGION\", >> config.json \
  && echo \"aws_s3_access_key_id\":\"$AWS_S3_ACCESS_KEY_ID\", >> config.json \
  && echo \"aws_s3_secret_access_key\":\"$AWS_S3_SECRET_ACCESS_KEY\", >> config.json \
  && echo \"db_connection_attempts_timeout_seconds\": 180, >> config.json \
  && echo \"jwt_secret\":\"$JWT_SECRET\", >> config.json \
  && echo \"metrics_endpoint\":\"$METRICS_ENDPOINT\", >> config.json \
  && echo \"ios_backend_private_key_file_path\":\"$IOS_PRIVATE_KEY_PATH\" >> config.json \
  && echo } >> config.json
RUN echo "app config: " && cat config.json

# Declare env vars
ENV BINARY_PATH_APP $BINARY_PATH_APP
# Used by the Ktor library
ENV LOG_DEST $LOGS_DIR

# Run tests and start the server app.
CMD java -jar $BINARY_PATH_APP --config-path config.json
