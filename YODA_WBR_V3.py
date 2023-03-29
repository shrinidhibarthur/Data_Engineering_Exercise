import json
import requests
import urllib3
from requests_ntlm import HttpNtlmAuth
import pandas as pd
import io
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers_json = {
    'accept': 'application/json',
    'content-type': 'application/json',
    'X-RequestForceAuthentication': 'true'
}

file_name = []
file_name1 = []
file_name2 = []
file_name3 = []


def get_sharepoint_auth():
    # Authentication function
    username = 'bshrinid'
    password = 'Cisco@890'
    return HttpNtlmAuth('ant\{}'.format(username), password)


# Enter site, folder URL without "https://share.amazon.com", and file name
site = 'IN_COBRA'
folder_link = '/sites/IN_COBRA/Shared%20Documents/YODA_WBR_Source_Data'
folder_link1 = '/sites/IN_COBRA/Shared%20Documents/UDAI_EMPLOYEE_RECORD'
folder_link2 = '/sites/IN_COBRA/Shared%20Documents/UDAI_WBR_Source_Data'
folder_link3 = '/sites/IN_COBRA/Shared%20Documents/module_mapping'

# Generating file links and fetching planning file
file_url = "/sites/" + site + "/_api/Web/GetFolderByServerRelativeUrl('" + folder_link + "')/Files"
file_url1 = "/sites/" + site + "/_api/Web/GetFolderByServerRelativeUrl('" + folder_link1 + "')/Files"
file_url2 = "/sites/" + site + "/_api/Web/GetFolderByServerRelativeUrl('" + folder_link2 + "')/Files"
file_url3 = "/sites/" + site + "/_api/Web/GetFolderByServerRelativeUrl('" + folder_link3 + "')/Files"

# get files
base_url = 'https://share.amazon.com'
file_url = base_url + file_url
file_url1 = base_url + file_url1
file_url2 = base_url + file_url2
file_url3 = base_url + file_url3

resp = requests.get(file_url, auth=get_sharepoint_auth(), headers={'accept': 'application/json;odata=verbose'},
                    verify=False)
resp1 = requests.get(file_url1, auth=get_sharepoint_auth(), headers={'accept': 'application/json;odata=verbose'},
                     verify=False)
resp2 = requests.get(file_url2, auth=get_sharepoint_auth(), headers={'accept': 'application/json;odata=verbose'},
                     verify=False)
resp3 = requests.get(file_url3, auth=get_sharepoint_auth(), headers={'accept': 'application/json;odata=verbose'},
                     verify=False)

request_json = json.loads(resp.text)['d']['results']
request_json1 = json.loads(resp1.text)['d']['results']
request_json2 = json.loads(resp2.text)['d']['results']
request_json3 = json.loads(resp3.text)['d']['results']

for file in request_json:
    # doc URL is located here
    doc_url = file['__metadata']['uri']
    # this gets us the actual relative path for where the file is on the site, we're just stripping away some special
    # chars - this will break if you have multiple ( or ) in the doc_url
    true_file_path = base_url + doc_url.split('(')[1].split(')')[0].replace("'", "")
    # This gives us a list of the entire URL split by '/', last item in it is the name of the file file
    # e.g. https://share.amazon.com/sites/<your_site_here>/Shared%20Documents/<path>/<to>/<your>/<folder>/some_file.type
    url_list_split = true_file_path.split('/')
    # get the file name hosted on the site
    name = url_list_split[len(url_list_split) - 1]
    file_name.append(name)
    # print(file_name)

for file1 in request_json1:
    # doc URL is located here
    doc_url1 = file1['__metadata']['uri']
    # this gets us the actual relative path for where the file is on the site, we're just stripping away some special
    # chars - this will break if you have multiple ( or ) in the doc_url
    true_file_path1 = base_url + doc_url1.split('(')[1].split(')')[0].replace("'", "")
    # This gives us a list of the entire URL split by '/', last item in it is the name of the file file
    # e.g. https://share.amazon.com/sites/<your_site_here>/Shared%20Documents/<path>/<to>/<your>/<folder>/some_file.type
    url_list_split1 = true_file_path1.split('/')
    # get the file name hosted on the site
    name1 = url_list_split1[len(url_list_split1) - 1]
    file_name1.append(name1)
    # print(file_name1)

for file2 in request_json2:
    # doc URL is located here
    doc_url2 = file2['__metadata']['uri']
    # this gets us the actual relative path for where the file is on the site, we're just stripping away some special
    # chars - this will break if you have multiple ( or ) in the doc_url
    true_file_path2 = base_url + doc_url2.split('(')[1].split(')')[0].replace("'", "")
    # This gives us a list of the entire URL split by '/', last item in it is the name of the file file
    # e.g. https://share.amazon.com/sites/<your_site_here>/Shared%20Documents/<path>/<to>/<your>/<folder>/some_file.type
    url_list_split2 = true_file_path2.split('/')
    # get the file name hosted on the site
    name2 = url_list_split2[len(url_list_split2) - 1]
    file_name2.append(name2)
    # print(file_name2)

for file3 in request_json3:
    # doc URL is located here
    doc_url3 = file3['__metadata']['uri']
    # this gets us the actual relative path for where the file is on the site, we're just stripping away some special
    # chars - this will break if you have multiple ( or ) in the doc_url
    true_file_path3 = base_url + doc_url3.split('(')[1].split(')')[0].replace("'", "")
    # This gives us a list of the entire URL split by '/', last item in it is the name of the file file
    # e.g. https://share.amazon.com/sites/<your_site_here>/Shared%20Documents/<path>/<to>/<your>/<folder>/some_file.type
    url_list_split3 = true_file_path3.split('/')
    # get the file name hosted on the site
    name3 = url_list_split3[len(url_list_split3) - 1]
    file_name3.append(name3)
    # print(file_name3)

file_name.sort(reverse=True)
asa = file_name[0]
file_name1.sort(reverse=True)
asa1 = file_name1[0]
file_name2.sort(reverse=True)
asa2 = file_name2[0]
file_name3.sort(reverse=True)
asa3 = file_name3[0]

# print('YODA WBR: ', file_name)
print('YODA WBR: ', asa)
# print('UDAI_EMPLOYEE_RECORD: ', file_name1)
print('UDAI_EMPLOYEE_RECORD: ', asa1)
# print('UDAI_WBR_Source_Data: ', file_name2)
print('UDAI_WBR_Source_Data: ', asa2)
# print('module_mapping: ', file_name3)
print('module_mapping: ', asa3)

# dump data to pandas DataFrame
YODA_WBR = requests.get('https://share.amazon.com/sites/IN_COBRA/Shared%20Documents/YODA_WBR_Source_Data/' + asa,
                        auth=get_sharepoint_auth(), verify=False)
bytes_file_obj = io.BytesIO()
bytes_file_obj.write(YODA_WBR.content)
bytes_file_obj.seek(0)
df = pd.read_csv(bytes_file_obj, low_memory=False, sep='\t', encoding='UTF-8', skipinitialspace=True)
# df['year'] = pd.DatetimeIndex(df['visit_date']).year
# df['month'] = pd.DatetimeIndex(df['visit_date']).month
# df['week'] = pd.DatetimeIndex(df['visit_date']).week
# df['quarter'] = pd.DatetimeIndex(df['visit_date']).quarter
# df = df.drop(['module'], axis=1)
df.drop_duplicates(keep=False, inplace=True)
print(df.head(10))
print(df.shape[0])

UDAI_EMPLOYEE_RECORD = requests.get(
    'https://share.amazon.com/sites/IN_COBRA/Shared%20Documents/UDAI_EMPLOYEE_RECORD/' + asa1,
    auth=get_sharepoint_auth(), verify=False)
bytes_file_obj = io.BytesIO()
bytes_file_obj.write(UDAI_EMPLOYEE_RECORD.content)
bytes_file_obj.seek(0)
df1 = pd.read_csv(bytes_file_obj, low_memory=False, sep='\t', encoding='UTF-8', skipinitialspace=True)
df1.rename(columns={'employee_login': 'username', 'reports_to_level_6_full_name': 'Director'}, inplace=True)
df1 = df1[['username', 'Director']]
df1.drop_duplicates(keep=False, inplace=True)
print(df1.head(10))
print(df1.shape[0])

UDAI_WBR_Source_Data = requests.get(
    'https://share.amazon.com/sites/IN_COBRA/Shared%20Documents/UDAI_WBR_Source_Data/' + asa2,
    auth=get_sharepoint_auth(), verify=False)
bytes_file_obj = io.BytesIO()
bytes_file_obj.write(UDAI_WBR_Source_Data.content)
bytes_file_obj.seek(0)
df2 = pd.read_csv(bytes_file_obj, low_memory=False, sep='\t', encoding='UTF-8', skipinitialspace=True)
df2.drop_duplicates(keep=False, inplace=True)
print(df2.head(10))
print(df2.shape[0])

module_mapping = requests.get('https://share.amazon.com/sites/IN_COBRA/Shared%20Documents/module_mapping/' + asa3,
                              auth=get_sharepoint_auth(), verify=False)
bytes_file_obj = io.BytesIO()
bytes_file_obj.write(module_mapping.content)
bytes_file_obj.seek(0)
df3 = pd.read_csv(bytes_file_obj, low_memory=False, sep=',', skipinitialspace=True)
df3.rename(columns={'report': 'report_name'}, inplace=True)
df3.drop_duplicates(keep=False, inplace=True)
pd.set_option('max_columns', None)
print(df3.head(10))
print(df3.shape[0])

# merger YODA_WBR+module_mapping+UDAI_EMPLOYEE_RECORD
# Master_df = pd.merge(df, df3, on='report_name', how='left')
# Master_df = pd.merge(Master_df, df1, on='username', how='left')
# Master_df.drop_duplicates(keep=False, inplace=True)

# print(Master_df.head(10))
# print(Master_df.columns)
# print(Master_df.shape[0])

# Master_df.to_csv('/Users/bshrinid/Desktop/CoBRA/YODA_WBR/Master_df.csv')

df_2022 = df[df[['year']].isin([2022]).all(axis=1)]
table = pd.pivot_table(data=df_2022, index=['module'], columns=['week'], values=['visits'], aggfunc={'visits': np.sum})
table1 = pd.pivot_table(data=df_2022, index=['module'], columns=['month'], values=['visits'], aggfunc={'visits': np.sum})
table2 = pd.pivot_table(data=df_2022, index=['module'], columns=['quarter'], values=['visits'], aggfunc={'visits': np.sum})
table3 = pd.pivot_table(data=df_2022, index=['module'], values=['visits'], aggfunc={'visits': np.sum})
pd.set_option('max_columns', None)
print(table)
print(table1)
print(table2)
print(table3)

table_df = pd.merge(table, table1, on='module', how='left')
table_df1 = pd.merge(table_df, table2, on='module', how='left')
table_df2 = pd.merge(table_df1, table3, on='module', how='left')
# sums = table_df2.select_dtypes(np.number).sum().rename('total')
pd.set_option('max_columns', None)
print(table_df2)
table_df2.to_csv('/Users/bshrinid/Desktop/CoBRA/YODA_WBR/yoda_wbr.csv')

