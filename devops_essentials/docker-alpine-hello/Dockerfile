# Use the official Alpine Linux image from the Docker Hub
FROM alpine:latest

# Install the curl package
RUN apk add --no-cache curl

# Copy the config.txt file to the container
COPY config.txt /app/config.txt

# Default command to keep the container running (could be overridden)
CMD ["sh"]
