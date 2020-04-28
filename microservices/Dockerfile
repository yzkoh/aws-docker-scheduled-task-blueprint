# Python 3
FROM python:3-onbuild

# Copy folder to / and build
COPY . /

# Arguments from docker-compose
ARG APP_ENV
ARG APP_CONFIG
ARG AWS_DEFAULT_REGION

# Export environment variables
ENV APP_ENV ${APP_ENV} 
ENV APP_CONFIG ${APP_CONFIG} 
ENV AWS_DEFAULT_REGION ${AWS_DEFAULT_REGION}

# Entrypoint for docker to run handlers
COPY entrypoint.sh /

# Permission to run entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]