from logging.config import dictConfig
from flask import Flask

from .routes import api

def create_app():
	dictConfig(
		{
			"version": 1,
			"formatters": {"default": {"format": "%(asctime)s %(levelname)s: %(message)s"}},
			"handlers": {
				"console": {
					"class": "logging.StreamHandler",
					"formatter": "default",
					"stream": "ext://sys.stdout",
				}
			},
			"root": {"level": "INFO", "handlers": ["console"]},
		}
	)

	app = Flask(__name__)

	app.register_blueprint(api)

	return app
