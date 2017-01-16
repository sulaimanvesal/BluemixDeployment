import json
from os.path import join, dirname
from os import environ
from json2html import *
import os
import fileinput
import webbrowser
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='a725a8b083d84215e86fa74ef64cc824dbe1090e')

test_url = 'https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg'
print(json2html.convert(json = json.dumps(visual_recognition.classify(images_url=test_url), indent=2)))
#strs = json2html.convert(json = json.dumps(visual_recognition.classify(images_url=test_url), indent=2))

#strs = json2html.convert(json = json.dumps(visual_recognition.detect_faces(images_url=test_url), indent=2)))



for i in range(1,3):
    imgurl='resources/'+str(i)+'.jpg'

    with open(join(dirname(__file__), imgurl), 'rb') as image_file:
        strs=json2html.convert(json = json.dumps(visual_recognition.classify(images_file=image_file, threshold=0.1,
                                                     classifier_ids=['CarsvsTrucks_1675727418', 'default']), indent=2))

    print ('<img src="/Users/sulaimanvesal/PythonProjects/VisualRecognitionIBMWatson/'+imgurl+'>"')
    print ('/Users/sulaimanvesal/PythonProjects/VisualRecognitionIBMWatson/'+imgurl)
    str2=strs.replace('/Users/sulaimanvesal/PythonProjects/VisualRecognitionIBMWatson/'+imgurl,
                      '<img src="/Users/sulaimanvesal/PythonProjects/VisualRecognitionIBMWatson/'+imgurl+'">')
    my_file=open("demo.html","w")
    my_file.write(str2)
    my_file.close()

    webbrowser.open_new_tab('file://' + os.path.realpath("demo.html"))

