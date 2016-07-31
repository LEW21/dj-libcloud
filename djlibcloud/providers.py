from django.conf import settings as _settings
from .storage import LibCloudStorage as _LCS
from django.utils.module_loading import import_string as _import_string

def _init(config):
	classname = config.get("class", "djlibcloud.storage.LibCloudStorage")
	class_ = _import_string(classname)
	return class_(config)

for _name, _config in _settings.LIBCLOUD_PROVIDERS.items():
	globals()[_name] = lambda: _init(_config)
