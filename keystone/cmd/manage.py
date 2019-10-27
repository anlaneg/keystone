#!/usr/bin/env python
# encoding:utf-8

# Copyright 2013 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import sys

from keystone.cmd import cli


# If ../../keystone/__init__.py exists, add ../../ to Python search path, so
# that it will override what happens to be installed in
# /usr/(local/)lib/python...
# 当前目录是 keystone/cmd/__init__.py,添加../../../后变更为 keystone的父目录
possible_topdir = os.path.normpath(os.path.join(os.path.abspath(__file__),
                                   os.pardir,
                                   os.pardir,
                                   os.pardir))
#将keystone添加进system path中
#解决未安装进python path路径中的问题
if os.path.exists(os.path.join(possible_topdir,
                               'keystone',
                               '__init__.py')):
    sys.path.insert(0, possible_topdir)


# entry point.
def main():
    #开发人员配置为keystone/etc/keystone.conf
    developer_config = os.path.join(possible_topdir, 'etc', 'keystone.conf')
    if not os.path.exists(developer_config):
        developer_config = None
    #使用开发人员配置
    cli.main(argv=sys.argv, developer_config_file=developer_config)
