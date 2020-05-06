import pprint
from tabulate import tabulate

def print_mind_response(res):
    """
    Filter mind response fields based on status.
    :param res:
    :return: pretty print MindResponse
    """
    # if successful, show only status and payload
    res_dict = res.to_dict()
    if res.status == "OK":
        res_dict.pop("summary")
        res_dict.pop("description")
        print(pprint.pformat(res_dict))
    else:
        res_dict.pop("payload")
        print(pprint.pformat(res_dict))


def pprint_ls(ls):
    """
    pretty print list with new line.
    :param ls:
    :return: pretty printed list
    """
    print(*ls, sep="\n")


def pprint_table(data, header):
    """

    :param data:
    :param header:
    :return:
    """
    print(tabulate(data, header, tablefmt='orgtbl'))
