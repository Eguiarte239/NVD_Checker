import requests, json
from datetime import date
from datetime import timedelta
import pandas as pd
today = date.today()
lastWeek = today - timedelta(days=7)
url = "https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate="+str(lastWeek)+"T00:00:00.000&pubEndDate="+str(today)+"T00:00:00.000"
request = requests.get(url)
response = json.loads(request.text)
descriptionsList = list()
for item in response['vulnerabilities']:
    descriptionsList.append(item['cve']['descriptions'][0]['value'])
df = pd.DataFrame(descriptionsList, columns=['q_data'])
df.to_excel("cveDescriptions.xlsx")