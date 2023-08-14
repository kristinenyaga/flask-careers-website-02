# gunicorn.conf.py

# The address and port where Gunicorn should bind
bind = '0.0.0.0:8000'  # Binds to all available network interfaces on port 8000

# Number of worker processes
workers = 4  # You can adjust this based on your server's resources

# The maximum number of simultaneous client connections
# (This should be a reasonably high number)
worker_connections = 1000

# The user and group that the server process should run as
# user = 'yourusername'
# group = 'yourgroupname'

# Logging configuration
accesslog = '-'  # Logs to stdout
errorlog = '-'   # Logs to stdout
loglevel = 'info'

# Enable Gunicorn's daemon mode
daemon = False

# Set the maximum number of requests a worker can handle before being restarted
max_requests = 1000

# Set the maximum number of seconds a worker can run before being restarted
max_requests_jitter = 100

# Set the timeout for handling requests (in seconds)
timeout = 30
