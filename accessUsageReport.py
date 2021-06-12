
'''
Access Report

o-gs6j79q9ib/r-vu7s

aws iam generate-organizations-access-report \
--entity-path o-gs6j79q9ib/r-vu7s

aws iam get-organizations-access-report \
    --job-id 26ba6147-1412-061a-9dd7-f40e94484731 > orgaccessreport.json
'''
import boto3
client = boto3.client('iam')

##Runs the command to run the access report and provides a job ID
# genOrgRep = client.generate_organizations_access_report(
#     EntityPath='o-gs6j79q9ib/r-vu7s'
# )

# pjobid = genOrgRep['JobId']
# print(pjobid)

def OrgAccessReport():

  #job set manually but can be dynamic
  pjobid = "26ba6147-1412-061a-9dd7-f40e94484731"
  results = client.get_organizations_access_report(
    JobId=pjobid,
    MaxItems=100
    # Marker='string', use this to get more of the report
  )
  return results

def OrgAccessReportMarker(pmarker):

  #job set manually but can be dynamic
  pjobid = "26ba6147-1412-061a-9dd7-f40e94484731"
  results = client.get_organizations_access_report(
    JobId=pjobid,
    MaxItems=100,
    Marker=pmarker
  )
  return results

getOrgRep = OrgAccessReport()

while getOrgRep['IsTruncated'] == True:
  for service in getOrgRep['AccessDetails']:
    if service['TotalAuthenticatedEntities'] > 0:
      print(service['ServiceName'])
      if getOrgRep['IsTruncated']:
        pmarker = getOrgRep['Marker']
        getOrgRep = OrgAccessReportMarker(pmarker)
      else:
        break

# print(getOrgRep)
print(getOrgRep['IsTruncated'])
print(getOrgRep['Marker'])

