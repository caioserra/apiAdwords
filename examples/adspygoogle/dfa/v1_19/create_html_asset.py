#!/usr/bin/python
#
# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example creates a HTML creative asset in a given advertiser. To create
an advertiser, run create_advertiser.py.

Tags: creative.saveCreativeAsset
"""

__author__ = 'api.jdilallo@gmail.com (Joseph DiLallo)'

import base64
import os
import sys
sys.path.insert(0, os.path.join('..', '..', '..', '..'))

# Import appropriate classes from the client library.
from adspygoogle.common import Utils
from adspygoogle import DfaClient


ADVERTISER_ID = 'INSERT_ADVERTISER_ID_HERE'
ASSET_NAME = 'INSERT_SWF_ASSET_NAME_HERE'
PATH_TO_FILE = 'INSERT_PATH_TO_SWF_FILE_HERE'


def main(client, advertiser_id, asset_name, path_to_file):
  # Initialize appropriate service.
  creative_service = client.GetCreativeService(
      'https://advertisersapitest.doubleclick.net', 'v1.19')

  # Convert file into format that can be sent in SOAP messages.
  content = Utils.ReadFile(path_to_file)
  content = base64.encodestring(content)

  # Construct and save HTML asset.
  html_asset = {
      'name': asset_name,
      'advertiserId': advertiser_id,
      'content': content,
      # Set he following to true if this asset is being used for HTML creative.
      'forHTMLCreatives': 'true'
  }
  result = creative_service.SaveCreativeAsset(html_asset)[0]

  # Display results.
  print ('Creative asset with file name of \'%s\' was created.'
         % result['savedFilename'])


if __name__ == '__main__':
  # Initialize client object.
  client = DfaClient(path=os.path.join('..', '..', '..', '..'))
  main(client, ADVERTISER_ID, ASSET_NAME, PATH_TO_FILE)
