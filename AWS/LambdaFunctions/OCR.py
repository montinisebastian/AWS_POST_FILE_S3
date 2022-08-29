import boto3
import re
  
## Textract APIs used - "start_document_text_detection", "get_document_text_detection"
def InvokeTextDetectJob(s3BucketName, objectName):
    response = None
    client = boto3.client('textract')
    response = client.start_document_text_detection(
            DocumentLocation={
                      'S3Object': {
                                    'Bucket': s3BucketName,
                                    'Name': objectName
                                }
           })
    return response["JobId"]

def CheckJobComplete(jobId):
    #time.sleep(5)
    client = boto3.client('textract')
    response = client.get_document_text_detection(JobId=jobId)
    status = response["JobStatus"]
    #print("Job status: {}".format(status))
    while(status == "IN_PROGRESS"):
        #time.sleep(5)
        response = client.get_document_text_detection(JobId=jobId)
        status = response["JobStatus"]
        #print("Job status: {}".format(status))
    return status

def JobResults(jobId):
    pages = []
    client = boto3.client('textract')
    response = client.get_document_text_detection(JobId=jobId)
 
    pages.append(response)
    #print("Resultset page recieved: {}".format(len(pages)))
    nextToken = None
    if('NextToken' in response):
        nextToken = response['NextToken']
        while(nextToken):
            response = client.get_document_text_detection(JobId=jobId, NextToken=nextToken)
            pages.append(response)
            #print("Resultset page recieved: {}".format(len(pages)))
            nextToken = None
            if('NextToken' in response):
                nextToken = response['NextToken']
    return pages

# S3 Document Data
 #conce-ml/textrackpython/

# Function invokes
def lambda_handler(event,context):
    res=[]
    filePath = event
    documentName = filePath
    s3BucketName = "react-bfa-proyect-pdfs"
    jobId = InvokeTextDetectJob(s3BucketName, documentName)
    processedResult =""
    #print("Started job with id: {}".format(jobId))
    if(CheckJobComplete(jobId)):
        response = JobResults(jobId)
        #print(response)
        for resultPage in response:
            for item in resultPage["Blocks"]:
                if item["BlockType"] == "LINE":
                    #print ('\033[94m' + item["Text"] + '\033[0m')
                    processedResult += item["Text"]
                    #print(item["Text"])

        dni = re.findall(r'\d{1,3}.\d{3}.\d{3}', processedResult)
        
        res.append("Nombre Fichero:"+filePath)
        res.append(processedResult)
        res.append(','.join(dni))
        return {
        'statusCode': 200,
        #'body': JSON.stringify(result)
        'body': res
        
        }
