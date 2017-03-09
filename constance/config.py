from constance.models import Config as ModelConfig

class Config(object):
    def __getattr__(self, key):
        try:
            return ModelConfig.objects.get(key=key).value
        except:
            return None

