FROM openjdk:16-jdk

# Declare all expected args
ARG BINARY_PATH_APP

# Test that all declared args are provided
RUN test $BINARY_PATH_APP

# Declare env vars used in CMD
ENV BINARY_PATH_APP $BINARY_PATH_APP

# Run tests and start the server app.
CMD java -jar $BINARY_PATH_APP
