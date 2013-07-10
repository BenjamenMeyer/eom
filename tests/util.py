# Copyright (c) 2013 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR ONDITIONS OF ANY KIND, either express or
# implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from oslo.config import cfg
import testtools

CONF = cfg.CONF


class TestCase(testtools.TestCase):

    def setUp(self):
        super(TestCase, self).setUp()

        self.config_file = self.conf_path('eom.conf-sample')
        CONF(args=[], default_config_files=[self.config_file])

    def conf_path(self, filename):
        """Returns the full path to the specified Marconi conf file.

        :param filename: Name of the conf file to find (e.g.,
                         'wsgi_memory.conf')
        """

        module_dir = os.path.abspath(os.path.dirname(__file__))
        parent = os.path.dirname(module_dir)
        return os.path.join(parent, 'etc', filename)

    def create_env(self, path, roles=None, method='GET'):
        if not isinstance(roles, str):
            roles = ','.join(roles or [])

        return {
            'HTTP_X_ROLES': roles,
            'PATH_INFO': path,
            'REQUEST_METHOD': method
        }

    def start_response(self, status, headers):
        self.status = status
        self.headers = headers


def app(env, start_response):
    start_response('204 No Content', [])