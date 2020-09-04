"""~This file is part of the PennAI library~

Copyright (C) 2017 Epistasis Lab, University of Pennsylvania

PennAI is maintained by:
    - Heather Williams (hwilli@upenn.edu)
    - Weixuan Fu (weixuanf@pennmedicine.upenn.edu)
    - William La Cava (lacava@upenn.edu)
    - and many other generous open source contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
import urllib.request, urllib.parse
import json
import os
import datetime 
unixtime = int(datetime.datetime.now().strftime("%s")) * 1000
#last 8 hours
lastupdate = unixtime - (8 * 60 * 60 * 1000 )
#baseURL = os.environ['FGLAB_URL']
baseURL = 'http://hoth.pmacs.upenn.edu:5080'
experimentsURL=baseURL+'/api/experiments'
#postvars = {'apikey':os.environ['APIKEY'],'date_start':lastupdate} 
postvars = {'apikey':'Oed+kIyprDrUq/3oWU5Jpyd22PqhG/CsUvI8oc9l39E=','date_start':lastupdate}
params = json.dumps(postvars).encode('utf8')
req = urllib.request.Request(experimentsURL, data=params,
  headers={'content-type': 'application/json'})
r = urllib.request.urlopen(req)
data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
print(len(data))
