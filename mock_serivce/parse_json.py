from flask import Flask, render_template, make_response,current_app,request,redirect,url_for,Response
from flask_api import status
import json

#
# def read_file(filename):
#     with open(filename) as f:
#         load_dict = json.load(f)
#
#     # print (load_dict)
#     print(load_dict['mock1']['request']['text'])
#     if  load_dict.has_key('mock1'):
#         print ("a")
#     return load_dict

# read_file()


def read_file(filename):
    with open(filename) as f:
        load_dict = json.load(f)

    # print (load_dict)
    # relations={}
    # print(load_dict['mock1']['request']['text'])
    #
    # for k,v in load_dict.items():
    #     case_name = k
    #     case_uri = v['request']['uri'].replace('/','')
    #
    #     relations[case_uri] = case_name
    #

    # return load_dict,relations
    return load_dict
#
# a  = read_file('test.json')
# print (a['abc']['request'])

def test_read(filename):
    with open(filename) as f:
        load_dict = json.load(f)
    return load_dict

def test_parse(dict):
    for k,v in dict.items():
        print('urls is %s'%k)
        for case in v:
            print (case)
            req = case['request']
            resp = case['response']
            #use for check

def check_reqest(dict,request):
    for k,v in dict.items():
        if request.url == k:
            for case in v:
                req = case['request']
                resp = case['response']
                if req['method'] is not None :
                    if req['method'] == request.method:
                        if req['Content-Type'] is not None:
                            if req['Content-Type'] == request.mimetype:
                                return True, req, resp
    return False, None, None

def make_mock_response(req,resp):
    resp=make_response(resp['text'])
    if req['Content-type'] == 'application/json':
        resp.headers['Content-type'] = 'application/json'

    return resp status.HTTP_200_OK

a = test_read('template.json')
test_parse(a)

