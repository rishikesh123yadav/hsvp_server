
# Sample request and response for User Document API.

## Post request  

- **input**

```
 {
        "user": 3,
        "document": 3
    }
```

- **output**

```

{
    "id": 2,
    "user": {
        "id": 3,
        "date_joined": "2020-10-22T18:07:24+0000",
        "date_invited": "2020-10-22T18:07:24+0000",
        "last_login": null,
        "username": "root",
        "email": "root@gmail.com",
        "contact_number": "+919898989898",
        "first_name": "root",
        "last_name": "root",
        "father_first_name": "root",
        "father_last_name": "root",
        "gst_no": "2348745878",
        "otp": "43289",
        "otp_sent_at": "09:09"
    },
    "document": {
        "id": 3,
        "created_on": "2020-10-27T10:56:49+0000",
        "modified_on": "2020-10-27T10:56:49+0000",
        "name": "adhar card",
        "doc_type": "jpeg",
        "file_url_1": "hello.jpeg",
        "file_url_2": "lol.jpeg"
    },
    "created_on": "2020-10-31T16:47:09+0000",
    "modified_on": "2020-10-31T16:47:09+0000"
}
```
