# Sample request and response for Document API.

## Post request  

- **input**

```
    {
        "name": "adhar card",
        "doc_type": "pdf",
        "file_url_1": "root.pdf",
        "file_url_2": "root1.pdf"
    }
```

- **output**

```

{
    "id": 4,
    "created_on": "2020-11-03T07:21:51+0000",
    "modified_on": "2020-11-03T07:21:51+0000",
    "name": "adhar card",
    "doc_type": "pdf",
    "file_url_1": "root.pdf",
    "file_url_2": "root1.pdf"
}

```
## Patch request  

- **input**
```
    {

        "file_url_2": "root2.pdf"
    }
```

- **output**

```

{
    "id": 4,
    "created_on": "2020-11-03T07:21:51+0000",
    "modified_on": "2020-11-03T07:29:08+0000",
    "name": "adhar card",
    "doc_type": "pdf",
    "file_url_1": "root.pdf",
    "file_url_2": "root2.pdf"
}
```
