import json

# people_data = '''
# {
#     "people": [
#         {
#             "name" : "John Smith",
#             "phone" : "615-555-7164",
#             "emails" : ["johnsmith@bogusemail.com", "john.smith@work_place.com"],
#             "has_license" : false
#         },
#         {
#             "name" : "Jane Doe",
#             "phone" : "560-555-5153",
#             "emails" : null,
#             "has_license" : true
#         }
#     ]
# }
# '''

# data = json.loads(people_data)

# print(data)
# for person in data["people"]:
#     del person["phone"]


# print(type(data))

# new_string = json.dumps(data, indent=2, sort_keys=True)
# print(new_string)

with open('states.json') as f:
    data = json.load(f) 

print("Interface Status")
print("=" * 160)
print("DN", " " * 45, "Description", " " * 10, "Speed", " " * 40, "MTU")
print("-" * 28, " " * 15, "-" * 15, " " * 15, "-" * 25, " " * 10, "-" * 15)
for item in data['imdata']:
    print(item["l1PhysIf"]["attributes"]["dn"], " "*35, item["l1PhysIf"]["attributes"]['speed'], " "*25, item["l1PhysIf"]["attributes"]['mtu'])