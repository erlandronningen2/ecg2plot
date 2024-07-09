# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Developed further by @Erland Rønningen
#
# start command: C:\Users\ADMERLARO\AppData\Local\Programs\Python\Python310\Python.exe D:\hjertesvikt\ekg\src\call2VertexV2.py
#
# program process all png files in jobfolder. calls vertex for each file. returns an messgae file with the prediction
# V2, transfer to pipe based message back instad of json string
#
import base64
from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict
import datetime
import os


jobfolder = "E:/InnoutahAFS/IN_Innoutah/"

def predict_image_classification(thejob, jobid,
    project="146378050205",
    endpoint_id="6697829012225392640",
    location="europe-west4",
    api_endpoint: str = "europe-west4-aiplatform.googleapis.com",
    outfoldername = "E:/InnoutahAFS/OUT_Innoutah/"
):
    response_filename = outfoldername + jobid
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    with open(thejob, "rb") as f:
        file_content = f.read()

    # The format of each instance should conform to the deployed model's prediction input schema.
    encoded_content = base64.b64encode(file_content).decode("utf-8")
    instance = predict.instance.ImageClassificationPredictionInstance(
        content=encoded_content,
    ).to_value()
    instances = [instance]
    # See gs://google-cloud-aiplatform/schema/predict/params/image_classification_1.0.0.yaml for the format of the parameters.
    parameters = predict.params.ImageClassificationPredictionParams(
        confidence_threshold=0.1, max_predictions=2,
    ).to_value()
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id#, credentials=credentials
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )
    predictions = response.predictions
    for prediction in predictions:
        etk = list(dict(prediction)['displayNames'])
        scr = list(dict(prediction)['confidences'])
        with open(outfoldername + jobid + '.json', 'w') as f:
            if (len(etk)) > 1:
                f.write(etk[0] + "|" + "{:.2}".format(scr[0]) + "|" + etk[1] + "|" + "{:.2}".format(scr[1]))
            else:
                f.write(etk[0] + "|" + "{:.2}".format(scr[0])) 
                

def log(msg):
    print(datetime.datetime.now(), msg)

def filelog(msg):
    f = open("D:/hjertesvikt/ekg/src/logs/call2vertex.log", "a")
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " --> " + msg + "\n")
    f.close()

if __name__ == '__main__':
    # Call2vertexV2 starting...
    log("start")
    filelog("Started and found " + str(len(os.listdir(jobfolder))) + " objects in jobfolder") 
    for filename in os.scandir(jobfolder):
        if filename.is_file():
            predict_image_classification(filename.path,filename.name.rsplit('.png')[0])
            filelog("Prosessed job id " + filename.name.rsplit('.png')[0])
            os.remove(filename.path)
    #        
    log("stopp")
    filelog("Stopping...")
