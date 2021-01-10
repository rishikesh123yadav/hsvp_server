# Sample request and response for Joint_Holder API.

## Post request  

- **input**

``` 

{
        "bidder":1,
        "user": {
                "username": "root",
                "email": "root@gmail.com",
                "contact_number": "+919723992054",
                "first_name": "root",
                "last_name": "root",
                "father_first_name": "root",
                "father_last_name": "root",
                "gst_no": "37893937",
                "otp": "3422",
                "otp_sent_at": "09:26"
        },
        "refund_account": {
                "name": "root",
                "bank_name": "HDFC",
                "account_number": "336749037059",
                "ifs": "hdfc1903",
                "branch": "jhunsi"
            }
}
```
- **output**


```

{
    "id": 3,
    "bidder": {
        "id": 1,
        "user": {
            "id": 1,
            "date_joined": "2020-10-22T11:32:12+0000",
            "date_invited": "2020-10-22T11:32:12+0000",
            "last_login": null,
            "username": "rishikesh",
            "email": "root@1123gamil.com",
            "contact_number": "+919923992382",
            "first_name": "rishi",
            "last_name": "yadav",
            "father_first_name": "root",
            "father_last_name": "root",
            "gst_no": "37893937",
            "otp": "3422",
            "otp_sent_at": "09:26"
        },
        "refund_account": {
            "id": 1,
            "created_on": "2020-10-22T11:32:12+0000",
            "modified_on": "2020-10-22T11:33:26+0000",
            "name": "rishikesh",
            "bank_name": "sbi",
            "account_number": "336749837334",
            "ifs": "sbi",
            "branch": "jhunsi"
        },
        "created_on": "2020-10-22T11:32:13+0000",
        "modified_on": "2020-10-22T11:32:13+0000"
    },
    "user": {
        "id": 12,
        "date_joined": "2020-11-08T08:38:20+0000",
        "date_invited": "2020-11-08T08:38:20+0000",
        "last_login": null,
        "username": "root0",
        "email": "rooot@gmail.com",
        "contact_number": "+919723992054",
        "first_name": "roooot",
        "last_name": "roooot",
        "father_first_name": "root",
        "father_last_name": "root",
        "gst_no": "37893937",
        "otp": "3422",
        "otp_sent_at": "09:26"
    },
    "refund_account": {
        "id": 11,
        "created_on": "2020-11-08T08:38:20+0000",
        "modified_on": "2020-11-08T09:02:10+0000",
        "name": "rooooot",
        "bank_name": "HDFC",
        "account_number": "336749007059",
        "ifs": "hdfc1903",
        "branch": "jaipur"
    },
    "created_on": "2020-11-08T08:38:20+0000",
    "modified_on": "2020-11-08T08:38:20+0000"
}

```
## Patch request  

- **input**

```
{
    "user": {
        "username":"root0",
        "first_name": "roooot",
        "last_name": "roooot"
     
    },
    "refund_account": {
        "name":"roooot",
        "bank_name": "HDFC",
        "account_number": "336749007059",
        "ifs": "hdfc1903",
        "branch": "jaipur"
    }
}

```
- **output**

```
{
    "id": 3,
    "bidder": {
        "id": 1,
        "user": {
            "id": 1,
            "date_joined": "2020-10-22T11:32:12+0000",
            "date_invited": "2020-10-22T11:32:12+0000",
            "last_login": null,
            "username": "rishikesh1",
            "email": "root@1123gamil.com",
            "contact_number": "+919923992382",
            "first_name": "rishi",
            "last_name": "yadav",
            "father_first_name": "root",
            "father_last_name": "root",
            "gst_no": "37893937",
            "otp": "3422",
            "otp_sent_at": "09:26"
        },
        "refund_account": {
            "id": 1,
            "created_on": "2020-10-22T11:32:12+0000",
            "modified_on": "2020-10-22T11:33:26+0000",
            "name": "rishikesh",
            "bank_name": "sbi",
            "account_number": "336749837334",
            "ifs": "sbi",
            "branch": "jhunsi"
        },
        "created_on": "2020-10-22T11:32:13+0000",
        "modified_on": "2020-10-22T11:32:13+0000"
    },
    "user": {
        "id": 12,
        "date_joined": "2020-11-08T08:38:20+0000",
        "date_invited": "2020-11-08T08:38:20+0000",
        "last_login": null,
        "username": "root0",
        "email": "rooot@gmail.com",
        "contact_number": "+919723992054",
        "first_name": "roooot",
        "last_name": "roooot",
        "father_first_name": "root",
        "father_last_name": "root",
        "gst_no": "37893937",
        "otp": "3422",
        "otp_sent_at": "09:26"
    },
    "refund_account": {
        "id": 11,
        "created_on": "2020-11-08T08:38:20+0000",
        "modified_on": "2020-11-08T09:02:10+0000",
        "name": "rooooot",
        "bank_name": "HDFC",
        "account_number": "336749007059",
        "ifs": "hdfc1903",
        "branch": "jaipur"
    },
    "created_on": "2020-11-08T08:38:20+0000",
    "modified_on": "2020-11-08T08:38:20+0000"
}
```
