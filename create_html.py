#!/usr/bin/env python

def create_html_page(cid, category_list):
    """
    Create an html file with given cid as name, and category_list as data.
    :param cid (int): category id
    :param category_list (list): list of record lists.
    """

    html = "<html>"

    html += "<header><h2>Category Tree Rooted at ID: {} </h2></header>".format(cid)

    html += "<body>"
    html += create_html_list(category_list)
    html += "</body>"
    html += "</html>"

    f = open(str(cid) +".html", "w+", encoding='utf-8')
    f.write(html)
    f.close()


def create_html_list(category_list):
    """
    Create an html list recursively using arg data

    :param category_list (list): list of category data

    :return (str): html script of recursive ul
    """

    html_list = "<ul>"

    for item in category_list:
        if isinstance(item, list):
            html_list += create_html_list(item)
        else:
            html_list += "<li> ID: {}  Name: {}  OfferEnable: {}</li>\n".format(item[0], item[2], "True" if item[3] else "False")

    html_list += "</ul>\n"

    return html_list
