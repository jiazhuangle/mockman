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



