# 0x00. Pagination

## About
- REST API pagination
- HATEOAS REST principle

## Tasks
0. Helper function `index_range` that returns the start and indices for datasets given a requested page and page size.
    - File: [0-simple_helper_function.py](0-simple_helper_function.py)

1. Simple pagination method `get_page` of class `Server`
    - File: [1-simple_pagination.py](1-simple_pagination.py)

2. Hypermedia pagination method `get_hyper`
    - File: [2-hypermedia_pagination.py](2-hypermedia_pagination.py)

3. Deletion-resilient hypermedia pagination with method `get_hyper_index`
    - File: [3-hypermedia_del_pagination.py](3-hypermedia_del_pagination.py)
