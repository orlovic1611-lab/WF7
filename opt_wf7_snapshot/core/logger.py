
import logging

logging.basicConfig(
filename="/var/log/wf/wf.log",
level=logging.INFO,
format="%(asctime)s %(message)s"
)


def log(msg):
    logging.info(msg)

