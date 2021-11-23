FROM grafana/grafana:5.1.0

# Declare params
ARG GRAFANA_ADMIN_PASSWORD
RUN test $GRAFANA_ADMIN_PASSWORD

# Copy config file
COPY grafana.ini /etc/grafana/grafana.ini

# Put password into the config file
USER root
RUN sed -i "s|GRAFANA_ADMIN_PASSWORD|$GRAFANA_ADMIN_PASSWORD|g" /etc/grafana/grafana.ini
USER grafana

# Copy data source
COPY data_source.yml /etc/grafana/provisioning/datasources/automatic.yml

# Copy dashboard
COPY dashboards_desc.yml /etc/grafana/provisioning/dashboards/all.yml
COPY dashboard.json /var/lib/grafana/dashboards/dashboard.json

# Too verbose, commented out
# RUN echo "grafana config: " && cat /etc/grafana/grafana.ini
