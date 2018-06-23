# Copyright 2015 Konstantinos Pachnis

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf import settings
from django.contrib.gis.geoip import GeoIP
from django.http import HttpResponseNotFound
from django.template import Context, loader


class GeoIPAdminAccess(object):
    """
    Permit access to django admin site based on user location.
    """
    def process_response(self, request, response):
        if not settings.DEBUG:
            if (request.path_info.startswith('/admin') and not
                    self.admin_site_access_permitted(request)):
                t = loader.get_template('404.html')
                c = Context()
                return HttpResponseNotFound(t.render(c))
            else:
                return response
        else:
            return response

    def admin_site_access_permitted(self, request):
        g = GeoIP()
        country_code = g.country(request.META['REMOTE_ADDR'])['country_code']

        if country_code not in settings.ADMIN_ALLOWED_COUNTRIES:
            return False

        return True
