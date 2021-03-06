"""Setup the isitopen application"""
import logging

from paste.deploy import appconfig
from pylons import config

from isitopen.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_config(command, filename, section, vars):
    """Place any commands to setup isitopen here"""
    conf = appconfig('config:' + filename)
    load_environment(conf.global_conf, conf.local_conf)
    import isitopen.model as model
    model.repo.create_db()
