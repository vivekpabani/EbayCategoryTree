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
