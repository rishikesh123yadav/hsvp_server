# Sample request and response for Bidder API.

## Post request  

- **input**

```
{
        "username": "root1",
        "email": "root@gamil.com",
        "contact_number": "+919923992388",
        "first_name": "root",
        "last_name": "root",
        "father_first_name": "root",
        "father_last_name": "root",
        "gst_no": "37893937",
        "otp": "3422"
    }
```

- **output**

```

{
    "id": 8,
    "date_joined": "2020-11-03T06:55:32+0000",
    "date_invited": "2020-11-03T06:55:32+0000",
    "last_login": null,
    "username": "root1",
    "email": "root@gamil.com",
    "contact_number": "+919923992388",
    "first_name": "root",
    "last_name": "root",
    "father_first_name": "root",
    "father_last_name": "root",
    "gst_no": "37893937",
    "otp": "3422"
}

```
## Patch request  

- **input**
```
{

        "father_first_name": "root2"
    }
```

- **output**

```

{
    "id": 8,
    "date_joined": "2020-11-03T06:55:32+0000",
    "date_invited": "2020-11-03T06:55:32+0000",
    "last_login": null,
    "username": "root1",
    "email": "root@gamil.com",
    "contact_number": "+919923992388",
    "first_name": "root",
    "last_name": "root",
    "father_first_name": "root2",
    "father_last_name": "root",
    "gst_no": "37893937",
    "otp": "3422",
    "otp_sent_at": "09:26"
}
```
