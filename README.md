# EbayCategoryTree
Fetch Ebay category data and provide storing and retrieving category tree functions. 

### Details of Implementation

1. Used the GetCategories API from eBay.com to download the entire eBay category tree.
2. Following data is stored in a SQLite database after fetching is done: 
    * CategoryID
    * CategoryName
    * CategoryLevel
    * BestOfferEnabled
    * ParentID
3. Data from SQLite database is used to render category trees in HTML. 

### Instructions

Make sure that: 

1. current directory is EbayCategoryTree.
2. catogeries.py and category.sh is executable.

Run following commands to use the features:


To fetch the data from ebay and populate database
``` bash
$ ./categories --rebuild
```

To generate an html page for category tree for given id
``` bash
$ ./categories --render <CATEGORY_ID>
```

The html page will be generated with category-id as name.
