from flask import Flask, render_template, make_response,current_app,request,redirect,url_for,Response
import json,sys,getopt


conf_name = ''
data_file={}

# request.json 只能够接受方法为POST、Body为raw，header 内容为 application/json类型的数据


app = Flask(__name__)


@app.route('/')
def index():
    print('here')
    print (conf_name)
    resp=make_response(conf_name)
    resp.headers['Content-type'] = 'application/json'

    return resp


@app.route('/<requests>')
def mock_get(requests):
    print (requests)
    # if relation.has_key(requests):
    if requests in data_file.keys():
        print(requests)
        if check_request(data_file[requests]['request'] , request) :
            print (data_file[requests]['response'])
            resp=make_response(data_file[requests]['response']['text'])
            #xian jia ding shi json
            resp.headers['Content-type'] = 'application/json'

            return resp
        else:
            return response_error()
    elif requests == 'favicon.ico':
        ico_path = 'favicon.ico'
        mime_type='image/x-icon'
        with open(ico_path, 'rb') as f:
            image = f.read()
        return Response(image,mime_type)
    return response_error()
    # return make_response()

def check_request(respect,reality):
    if respect['method'] != reality.method:
        return False
    elif respect['Content-type'] != reality.content_type:
        return False
    else:
        return True


def response_error(error_type='Error',content_type='application/json',case_name='foo',message='u got an error'):
    resp_json ="{'error-type':'%s','case-name':'%s','message':'%s'}" % (error_type,case_name,message)
    resp=make_response(resp_json)
    if content_type == 'application/json':
        resp.headers['Content-type'] = 'application/json'
    return resp


def read_file(filename):
    with open(filename) as f:
        load_dict = json.load(f)
    return load_dict


if __name__ == "__main__":
    port =4444
    try:
        opts,args = getopt.getopt(sys.argv[1:], "f:p:", ["file","port"])
        for op, value in opts:
            if op == '-f' or op == '--file':
                conf_name = value
            if op == '-p' or op == '--port':
                port = value
    except:
        print("-f or -file for input json file")
        print("-p or -port for service port. default is 4444")
        exit(0)
    data_file = read_file(conf_name)
    app.run(debug=True,port=port)
