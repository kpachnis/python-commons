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

from django.contrib.staticfiles.storage import CachedStaticFilesStorage
from django.conf import settings

from pipeline.storage import GZIPMixin, PipelineMixin


class BugeffectPipelineMixin(PipelineMixin):
    def __init__(self, location=settings.STATIC_ROOT, *args, **kwargs):
        super(BugeffectPipelineMixin, self).__init__(location, *args, **kwargs)


class GZIPCachedStorage(GZIPMixin, BugeffectPipelineMixin,
                        CachedStaticFilesStorage):
    pass
