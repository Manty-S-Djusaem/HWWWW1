from decouple import config

passw = config("PASSWORD", default=123, cast=int)