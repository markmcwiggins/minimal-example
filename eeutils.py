import os, json, errno, subprocess, sys
import re
from config import Config

from utils.common import retrieve_ftp_info

binary_dir = os.path.dirname(os.path.realpath(__file__))
cfg_dir = os.path.join(binary_dir, os.pardir, "conf")
cfg = Config(open(os.path.join(cfg_dir,"our.cfg")))
ftp_info = retrieve_ftp_info(cfg["config"]["secret_path"])
cfg['config']['user'] = ftp_info['username']
cfg['config']['password'] = ftp_info['password']
print(cfg['config']['password'])
PASSWORD = ftp_info['password']
print(PASSWORD)
             
