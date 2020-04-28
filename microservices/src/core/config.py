'''
Required config variables are:

MONGO_URI - uri of mongodb being used

'''


class Config(object):

    requried_configs = [
        'MONGO_URI',
    ]

    def __init__(self, config):

        # check if there are missing
        missing_configs = self._get_missing_configs(config)
        if missing_configs:
            error_message = ', '.join(missing_configs)
            error_message = error_message + ' are missing!'
            raise Exception(error_message)

        # set attributes
        for key, value in config.items():
            self.__dict__[key.strip().upper()] = value

    def _get_missing_configs(self, config):
        missing = []
        for r in self.requried_configs:
            if r not in config:
                missing.append(r)

        return missing if missing else None
