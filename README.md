# docker-events-exporter

Service for listening on given docker events and pushing them directly to the ELK stack

# Usage

This service is designed to be run as a docker container.

# Design

The service is using the Python `elasticsearch` library to send events to the ELK stack. More regarding
the library here https://elasticsearch-py.readthedocs.io/en/v8.18.1/ . The service is using the `docker` library to
listen on docker events.

Currently, it is configured to listen on the following events types:

- `container`
- `image`

and will push the events to the ELK stack if the event status is:

- `start`
- `die`

