#!/bin/sh
HANDLER="$1"

# Run microservice handler
python -m src.handlers.${HANDLER}