FROM quay.io/keycloak/keycloak:20.0.2
USER root

ARG KEYCLOACK_PATH=/opt/keycloak

WORKDIR $KEYCLOACK_PATH

ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]
CMD ["start-dev"]
