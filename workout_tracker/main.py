import random

import requests
import json
from datetime import datetime, timedelta

with open('../config.json') as f:
    config_data = json.load(f)

nutritionix_apikey = config_data["nutritionix"]["API_KEY"]
nutritionix_appid = config_data["nutritionix"]["APP_ID"]
