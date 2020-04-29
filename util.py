import pprint

def print_mind_reponse(res):
    """
    Filter mind response fields based on status.
    :param res:
    :return: pretty print
    """
    # if successful, show only status and payload
    if res.status == "OK":
        res_dict = res.to_dict()
        res_dict.pop("summary")
        res_dict.pop("description")
        print(pprint.pformat(res_dict))
    else:
        print(res)