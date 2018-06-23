csp-report
==========

csp-report will accept a CSP (Content Security Policy) policy violation
report from the browser, and send a notification email to the django admins.

The email includes the policy violation report and the request HTTP headers.

Installation
------------

Add csp_report to the django INSTALLED_APPS::

   INSTALLED_APPS = (
       ...
       'csp_report',
   )

Usage
-----

Include the csp_report URLs to your project urls.py::

   url(r'^csp/report/', include('csp_report.urls')),


If you have django-csp install set the CSP_REPORT_URI to /csp/report/::

   CSP_REPORT_URI = '/csp/report/'


Additional information
-----------------------

* `Content Security Policy 1.0 <http://www.w3.org/TR/CSP/>`_
* `django-csp <https://github.com/mozilla/django-csp>`_
