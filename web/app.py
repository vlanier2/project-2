"""
Vincent Lanier
"""

from flask import Flask, send_from_directory, abort
import os, configparser

def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f 
            break
    
    if config_path is None:
        raise RuntimeError("Configuration file not found")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

config = parse_config(["credentials.ini", "default.ini"])
port = config["SERVER"]["PORT"]
debug = True if config["SERVER"]["DEBUG"] == 'True' else False
app = Flask(__name__)

@app.route("/<string:filename>")
def index(filename):
    if ".." in filename or "~" in filename:
        abort(403)
    if not os.path.isfile(os.path.join('pages', filename)):
        abort(404)
    return send_from_directory('pages/', filename), 200

@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('pages/', '403.html'), 403

@app.errorhandler(404)
def not_found(e):
    return send_from_directory('pages/', '404.html'), 404

if __name__ == "__main__":
    app.run(debug=debug, host='0.0.0.0', port=port)