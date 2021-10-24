print("THis is my first git")
print("This is feature changes done ")
print("This is done is feature 1")
import yaml

#This is done in main branch

counts=[12,32,13,42,56,65]
platlist=['SAML20','SAML20',"RP","RP","OAuth","OAuth"]
envs=["PROD","STG","PROD","STG","PROD","STG"]
count_dict_list=[]
for a in range(6):
    count_dict_list.append("first")
    count_dict_list.append({'apps_count':counts[a],'environment':envs[a],'platform':platlist[a]})

print(count_dict_list)

print(yaml.dump(count_dict_list))

with open('consolidation_report.yml', 'w') as f:
    data = yaml.dump(count_dict_list, f)

a_yaml_file = open("consolidation_report.yml")
parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)

print(parsed_yaml_file)