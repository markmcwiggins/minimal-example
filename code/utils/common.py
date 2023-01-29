import os
import re


def retrieve_ftp_info(path):
    if not os.path.exists(path):
        raise Exception("the ftp secret path %s doesn't exist" % path)

    ftp_info = {}
    with open(path) as fin:
        for config_line in fin:
            config_line = config_line.strip()
            m_username = re.search(r"^sem.ftp.username=(.+)", config_line)
            if m_username:
                ftp_info["username"] = m_username.group(1)
            
            m_password = re.search(r"^sem.ftp.password=(.+)", config_line)
            if m_password:
                ftp_info["password"] = m_password.group(1)
    
    for key in ftp_info:
        if not ftp_info[key]: 
            raise Exception("failed to retrieve ftp info from secrets file %s" % path)
    
    return ftp_info
