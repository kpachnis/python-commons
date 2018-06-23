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

import json

from django.core.mail import BadHeaderError, mail_admins
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator


class CspReportView(View):
    http_method_names = 'post'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CspReportView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            report = json.loads(request.body).get('csp-report')
        except (KeyError, ValueError):
            return HttpResponseBadRequest()

        if report:
            try:
                self.__send_email_report(request.META, report)
            except BadHeaderError:
                return HttpResponseBadRequest()

        return HttpResponse()

    def __send_email_report(self, meta, report):
        email = loader.get_template('csp_report/email.txt')

        context = Context({'report': report,
                           'meta': meta})

        mail_admins('CSP violation report', email.render(context))
