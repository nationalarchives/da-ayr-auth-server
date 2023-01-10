FROM quay.io/keycloak/keycloak:20.0.2
USER root

WORKDIR /opt/keycloak
COPY ayr-realm.json data/
COPY keycloak.conf conf/
COPY quarkus.properties conf/
