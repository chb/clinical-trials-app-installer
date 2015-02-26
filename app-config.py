#!/usr/bin/env python3
#
# App settings
# copy to "config.py"

DEBUG = 0
USE_TEST_PATIENT = 0
SESSION_SECRET = "goeu824-aoeuclr29348"

# SMART
SMART_APP_ID = "my_web_app"
SMART_API_BASE = "https://fhir-api.smartplatforms.org"
SMART_REDIRECT = "http://{{item.0.host}}/fhir-app/"

# LillyCOI API key (base64 encoded "key:secret" string)
LILLY_SECRET = ""

# Mongo params; leave host/port/db empty for default localhost connection
MONGO_HOST = None
MONGO_PORT = None
MONGO_DB = "clinicaltrialsapp"
MONGO_USER = None
MONGO_PASS = None
MONGO_BUCKET = "main"