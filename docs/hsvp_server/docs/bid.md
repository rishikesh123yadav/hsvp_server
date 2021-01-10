# Sample request and response for Bid API.

## Post request  

- **input**

```
 {
        "bidder": 1,
        "auction":2,
        "price": "2000000.00",
        "placed_at": "2020-10-29"
    }

```

- **output**

```

{
    "id": 2,
    "auction": {
        "id": 2,
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
                "first_name": "rishikesh",
                "last_name": "yadav",
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
            "id": 4,
            "created_on": "2020-10-27T11:53:13+0000",
            "modified_on": "2020-10-27T11:56:23+0000",
            "name": "parking lot",
            "description": "jaipur",
            "quantity": 2
        },
        "created_on": "2020-10-28T04:07:00+0000",
        "modified_on": "2020-10-28T04:14:24+0000",
        "name": "parking lot",
        "description": "on sell",
        "starts_at": "2020-10-28T03:53:54+0000",
        "ends_at": "2020-11-28T03:54:03+0000",
        "no_of_rounds": 10,
        "base_price": "10000.00",
        "registration_time_starts_at": "2020-10-28T03:54:17+0000",
        "registration_time_ends_at": "2020-11-18T03:54:21+0000",
        "emd_amount": "4000.00",
        "h1_payment_percent": "45.00",
        "h1_payment_end_date": "2020-10-28T03:54:39+0000"
    },
    "bidder": {
        "id": 1,
        "user": {
            "id": 1,
            "date_joined": "2020-10-22T11:32:12+0000",
            "date_invited": "2020-10-22T11:32:12+0000",
            "last_login": null,
            "username": "root",
            "email": "root@1123gamil.com",
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
    "created_on": "2020-10-29T10:23:54+0000",
    "modified_on": "2020-10-29T10:23:54+0000",
    "price": "2000000.00",
    "placed_at": "2020-10-29"
}

```
## Patch request  

- **input**

```


 {
        "price": "1000000.00"
    }

```
- **output**

```
{
    "id": 2,
    "auction": {
        "id": 2,
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
                "first_name": "rishikesh",
                "last_name": "yadav",
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
            "id": 4,
            "created_on": "2020-10-27T11:53:13+0000",
            "modified_on": "2020-10-27T11:56:23+0000",
            "name": "parking lot",
            "description": "jaipur",
            "quantity": 2
        },
        "created_on": "2020-10-28T04:07:00+0000",
        "modified_on": "2020-10-28T04:14:24+0000",
        "name": "parking lot",
        "description": "on sell",
        "starts_at": "2020-10-28T03:53:54+0000",
        "ends_at": "2020-11-28T03:54:03+0000",
        "no_of_rounds": 10,
        "base_price": "10000.00",
        "registration_time_starts_at": "2020-10-28T03:54:17+0000",
        "registration_time_ends_at": "2020-11-18T03:54:21+0000",
        "emd_amount": "4000.00",
        "h1_payment_percent": "45.00",
        "h1_payment_end_date": "2020-10-28T03:54:39+0000"
    },
    "bidder": {
        "id": 1,
        "user": {
            "id": 1,
            "date_joined": "2020-10-22T11:32:12+0000",
            "date_invited": "2020-10-22T11:32:12+0000",
            "last_login": null,
            "username": "root",
            "email": "root@1123gamil.com",
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
    "created_on": "2020-10-29T10:23:54+0000",
    "modified_on": "2020-10-29T10:26:04+0000",
    "price": "1000000.00",
    "placed_at": "2020-10-29"
}
```
