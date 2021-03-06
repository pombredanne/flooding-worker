#!/usr/bin/python
# (c) Nelen & Schuurmans.  GPL licensed.

from optparse import make_option

from django.core.management.base import BaseCommand
from flooding_worker import executor
from flooding_worker.worker.broker_connection import BrokerConnection
from flooding_worker.worker.message_logging_handler import AMQPMessageHandler
from flooding_worker.worker.action_workflow import ActionTaskPublisher
from django.conf import settings

import logging
log = logging.getLogger("flooding.management.start_scenario")


class Command(BaseCommand):

    help = ("Example: bin/django workerbeat --log_level DEBUG")

    option_list = BaseCommand.option_list + (
            make_option('--log_level',
                        help='logging level DEBUG, INFO',
                        default='INFO',
                        type='str'),)

    def handle(self, *args, **options):
        """
        Send a message to the broker.
        """
        if hasattr(logging, options["log_level"].upper()):
            executor.start_heartbeat(options["log_level"])
        else:
            log.error("Invalid log level: %s" % options["log_level"])
