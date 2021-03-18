FROM postgres:9.6

# Declare params
ARG USER_PASSWORD
RUN test $USER_PASSWORD
ENV USER_PASSWORD $USER_PASSWORD
ENV POSTGRES_PASSWORD $USER_PASSWORD

# Add user
RUN useradd -p $USER_PASSWORD main_user

# Initialization finish is in the .sh
COPY db-related-init.sh /docker-entrypoint-initdb.d/
