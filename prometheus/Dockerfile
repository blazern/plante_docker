FROM prom/prometheus:v2.31.1

# Declare params
ARG METRICS_ENDPOINT
RUN test $METRICS_ENDPOINT

# Copy config file and put the endpoint into it
COPY prometheus.yml /etc/prometheus/prometheus.yml
RUN sed -i "s|METRICS_ENDPOINT|$METRICS_ENDPOINT|g" /etc/prometheus/prometheus.yml

RUN echo "prometheus config: " && cat /etc/prometheus/prometheus.yml
