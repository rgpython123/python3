#!/usr/bin/python3

import re

with open('apache_logs.txt', 'r') as f:
    file = f.readlines()

IP_REGEX = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
STATUS_CODE_REGEX = re.compile(r'\s\d\d\d\s')

ip_list = []
status_codes_list = []

for line in file:
    ip_list.extend(IP_REGEX.findall(line))

for line in file:
    status_codes_list.extend(STATUS_CODE_REGEX.findall(line))

status_codes_set = set(status_codes_list)

#print(ip_list)

print("\n\tStatus Codes List (All of them.):")
print(status_codes_list)

print("\n\tUnsorted Status Codes:")
print(status_codes_set)

print("\n\tSorted Status Codes:")
print(sorted(status_codes_set))

print("\n\tSorted Status Codes with Count:")
sorted_unique_status_codes_list = sorted(status_codes_set)
print(sorted_unique_status_codes_list)
for code in sorted_unique_status_codes_list:
    print("Code: {}   Count: {}".format(code, status_codes_list.count(code)))    

print("\n\tDictionary of Status Codes with Count:")
status_codes_dict = { code: status_codes_list.count(code) for code in status_codes_set }
print(status_codes_dict)
