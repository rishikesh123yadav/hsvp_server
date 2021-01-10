# Sample request and response for EMD API.

## Post request  

- **input**

``` 
{
        "auction": 1,
        "quantity": 2,
        "processing_fees": "4000.00",
        "total_amount": "15000.00",
        "payment_mode": "O",
        "status": "S"
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
            "name": "root",
            "description": "parking is on sell",
            "quantity": 4
        },
        "created_on": "2020-10-28T03:54:41+0000",
        "modified_on": "2020-10-28T03:54:41+0000",
        "name": "plot",
        "description": "heavy discount sell",
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
    "created_on": "2020-10-29T04:58:27+0000",
    "modified_on": "2020-10-29T04:58:27+0000",
    "quantity": 2,
    "processing_fees": "4000.00",
    "total_amount": "15000.00",
    "payment_mode": "O",
    "status": "S"
}

```
## Patch request  

- **input**

```
 {
        "quantity": 3
      
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
            "name": "root",
            "description": "parking in on sell",
            "quantity": 4
        },
        "created_on": "2020-10-28T03:54:41+0000",
        "modified_on": "2020-10-28T03:54:41+0000",
        "name": "plot",
        "description": "heavy discount sell",
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
    "created_on": "2020-10-29T04:58:27+0000",
    "modified_on": "2020-10-29T05:00:24+0000",
    "quantity": 3,
    "processing_fees": "4000.00",
    "total_amount": "15000.00",
    "payment_mode": "O",
    "status": "S"
}
```
