# Sample request and response for Round API.

## Post request  

- **input**

```
 {
        "auction": 1,
        "h1_payment": 1,
        "starts_at": "2020-10-31T11:09:24+0000",
        "ends_at": "2020-10-31T11:09:27+0000",
        "base_price": "40000.00"
    }
```

- **output**

```

{
    "id": 2,
    "auction": {
        "id": 1,
        "seller": {
            "id": 2,
            "user": {
                "id": 6,
                "date_joined": "2020-10-27T11:32:27+0000",
                "date_invited": "2020-10-27T11:32:27+0000",
                "last_login": null,
                "username": "root",
                "email": "root@gmail.com",
                "contact_number": "+919823992389",
                "first_name": "root",
                "last_name": "root",
                "father_first_name": "root",
                "father_last_name": "root",
                "gst_no": "549349",
                "otp": "9349",
                "otp_sent_at": "09:26"
            },
            "primary_account": {
                "id": 4,
                "created_on": "2020-10-27T11:32:27+0000",
                "modified_on": "2020-10-27T11:32:27+0000",
                "name": "root",
                "bank_name": "sbi",
                "account_number": "989599494595490",
                "ifs": "sbii9349",
                "branch": "ald"
            },
            "created_on": "2020-10-27T11:32:27+0000",
            "modified_on": "2020-10-27T11:32:27+0000"
        },
        "details": {
            "id": 3,
            "created_on": "2020-10-24T09:00:01+0000",
            "modified_on": "2020-10-24T09:00:01+0000",
            "name": "rgegeg",
            "description": "rgrbrbe",
            "quantity": 4
        },
        "created_on": "2020-10-28T03:54:41+0000",
        "modified_on": "2020-10-28T03:54:41+0000",
        "name": "plot",
        "description": "on sell",
        "starts_at": "2020-10-28T03:53:54+0000",
        "ends_at": "2020-10-28T03:54:03+0000",
        "no_of_rounds": 10,
        "base_price": "10000.00",
        "registration_time_starts_at": "2020-10-28T03:54:17+0000",
        "registration_time_ends_at": "2020-10-28T03:54:21+0000",
        "emd_amount": "4000.00",
        "h1_payment_percent": "45.00",
        "h1_payment_end_date": "2020-10-28T03:54:39+0000"
    },
    "h1_payment": {
        "id": 1,
        "user": {
            "id": 1,
            "date_joined": "2020-10-22T11:32:12+0000",
            "date_invited": "2020-10-22T11:32:12+0000",
            "last_login": null,
            "username": "root",
            "email": "root@gamil.com",
            "contact_number": "+919923992382",
            "first_name": "root",
            "last_name": "root",
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
            "name": "root",
            "bank_name": "sbi",
            "account_number": "336749837334",
            "ifs": "sbi",
            "branch": "jhunsi"
        },
        "created_on": "2020-10-22T11:32:13+0000",
        "modified_on": "2020-10-22T11:32:13+0000"
    },
    "created_on": "2020-10-31T11:15:30+0000",
    "modified_on": "2020-10-31T11:15:30+0000",
    "starts_at": "2020-10-31T11:09:24+0000",
    "ends_at": "2020-10-31T11:09:27+0000",
    "base_price": "40000.00"
}
```
## Patch request  

- **input**

```

 {
        "auction": 1,
        "h1_payment": 1,
        "starts_at": "2020-10-31T11:09:24+0000",
        "ends_at": "2020-10-31T11:09:27+0000",
        "base_price": "50000.00"
    }
```

- **output**

```

{
    "id": 2,
    "auction": {
        "id": 1,
        "seller": {
            "id": 2,
            "user": {
                "id": 6,
                "date_joined": "2020-10-27T11:32:27+0000",
                "date_invited": "2020-10-27T11:32:27+0000",
                "last_login": null,
                "username": "root",
                "email": "root@gmail.com",
                "contact_number": "+919823992389",
                "first_name": "root",
                "last_name": "root",
                "father_first_name": "root",
                "father_last_name": "root",
                "gst_no": "549349",
                "otp": "9349",
                "otp_sent_at": "09:26"
            },
            "primary_account": {
                "id": 4,
                "created_on": "2020-10-27T11:32:27+0000",
                "modified_on": "2020-10-27T11:32:27+0000",
                "name": "root",
                "bank_name": "sbi",
                "account_number": "989599494595490",
                "ifs": "sbi9349",
                "branch": "ald"
            },
            "created_on": "2020-10-27T11:32:27+0000",
            "modified_on": "2020-10-27T11:32:27+0000"
        },
        "details": {
            "id": 3,
            "created_on": "2020-10-24T09:00:01+0000",
            "modified_on": "2020-10-24T09:00:01+0000",
            "name": "rgegeg",
            "description": "rgrbrbe",
            "quantity": 4
        },
        "created_on": "2020-10-28T03:54:41+0000",
        "modified_on": "2020-10-28T03:54:41+0000",
        "name": "plot",
        "description": "on sell",
        "starts_at": "2020-10-28T03:53:54+0000",
        "ends_at": "2020-10-28T03:54:03+0000",
        "no_of_rounds": 10,
        "base_price": "10000.00",
        "registration_time_starts_at": "2020-10-28T03:54:17+0000",
        "registration_time_ends_at": "2020-10-28T03:54:21+0000",
        "emd_amount": "4000.00",
        "h1_payment_percent": "45.00",
        "h1_payment_end_date": "2020-10-28T03:54:39+0000"
    },
    "h1_payment": {
        "id": 1,
        "user": {
            "id": 1,
            "date_joined": "2020-10-22T11:32:12+0000",
            "date_invited": "2020-10-22T11:32:12+0000",
            "last_login": null,
            "username": "root",
            "email": "root@gamil.com",
            "contact_number": "+919923992382",
            "first_name": "root",
            "last_name": "root",
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
            "name": "root",
            "bank_name": "sbi",
            "account_number": "336749837334",
            "ifs": "sbi",
            "branch": "jhunsi"
        },
        "created_on": "2020-10-22T11:32:13+0000",
        "modified_on": "2020-10-22T11:32:13+0000"
    },
    "created_on": "2020-10-31T11:15:30+0000",
    "modified_on": "2020-10-31T11:16:45+0000",
    "starts_at": "2020-10-31T11:09:24+0000",
    "ends_at": "2020-10-31T11:09:27+0000",
    "base_price": "50000.00"
}
```
