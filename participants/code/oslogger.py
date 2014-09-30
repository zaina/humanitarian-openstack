import logging


# Setup a logger to write messages to the console.
log = logging.getLogger("libcloud")
log.setLevel(logging.INFO)
fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(fmt)
log.addHandler(console)
