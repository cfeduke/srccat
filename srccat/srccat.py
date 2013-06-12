#!/usr/bin/env python
#encoding: utf-8

# composes a colout command for syntax highlighting source code
# while colout is capable of doing this itself it requires hints
# for determining which language to use when syntax highlighting
# through pygments
# Licensed under GPL v3
# (c)2013 Charles Feduke <charles.feduke@gmail.com>
import ConfigParser

import sys
import os
import language_association


if __name__ == '__main__':
    config = ConfigParser.SafeConfigParser()
    config.read(os.path.expanduser("~/.srccat"))
    try:
        style = config.get("Config", "style")
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
        style = "monokai"

    filename = sys.argv[1]
    language = language_association.LanguageAssociation()(filename)
    cmd = "cat \"%s\" | colout -s \"%s\" \"%s\"" % (filename, language, style)
    os.system(cmd)
