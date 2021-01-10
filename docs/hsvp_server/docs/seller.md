# Sample request and response for Seller API.

## Post request  

- **input**

```
{
        "user": {
            "username": "Root",
            "email": "root@gamil.com",
            "contact_number": "+919923902382",
            "first_name": "root",
            "last_name": "root",
            "father_first_name": "root",
            "father_last_name": "root",
            "gst_no": "37893937",
            "otp": "3422",
            "otp_sent_at": "09:26"
        },
        "primary_account": {
            "name": "Root",
            "bank_name": "sbi",
            "account_number": "33674983733",
            "ifs": "sbi9422",
            "branch": "Jaipur"
        }
    }

```

- **output**

```
{
    "id": 1,
    "user": {
        "id": 5,
        "date_joined": "2020-10-28T08:43:32+0000",
        "date_invited": "2020-10-28T08:43:32+0000",
        "last_login": null,
        "username": "root",
        "email": "root@11234gamil.com",
        "contact_number": "+919923902382",
        "first_name": "root",
        "last_name": "root",
        "father_first_name": "root",
        "father_last_name": "root",
        "gst_no": "37893937",
        "otp": "3422",
        "otp_sent_at": "09:26"
    },
    "primary_account": {
        "id": 5,
        "created_on": "2020-10-28T08:43:32+0000",
        "modified_on": "2020-10-28T08:43:32+0000",
        "name": "cmm",
        "bank_name": "sbi",
        "account_number": "33674943733",
        "ifs": "sbi",
        "branch": "Jaipur"
    },
    "created_on": "2020-10-28T08:43:32+0000",
    "modified_on": "2020-10-28T08:43:32+0000"
}
```
## Patch request  

- **input**


