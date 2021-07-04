import json
import urllib2
import time
import sys


arq = open("ip.txt") 

linhas = arq.readlines()

for iplinefile in linhas:
    EnderecoAPI="http://ip-api.com/json/"+iplinefile
    JsonResultanteAPI = urllib2.urlopen(EnderecoAPI).read()
    JsonResultanteAPI = unicode(JsonResultanteAPI,errors='ignore')
    JsonParseado = json.loads(JsonResultanteAPI)
    
    print("-----Localizacao obtida-----")
    print("IP: "+JsonParseado["query"])
    print("Cidade: "+JsonParseado["city"])
    print("Estado (UF): "+JsonParseado["region"])
    print("Pais: "+JsonParseado["country"])
    print("Latitude: "+str(JsonParseado["lat"]))
    print("Longitude: "+str(JsonParseado["lon"]))
    print("---------------------------")


