# Sample request and response for Auction API.

## Post request  

- **input**

```
{
    "seller":1,
    "name":"office",
    "no_of_rounds":2,
    "base_price":34343,
    "emd_amount":5454,
    "h1_payment_percent":34,
    "details":
    {
        "name": "cmm office",
        "description": "3 flore office ",
        "quantity": 2,
         "auction_items":[
            {
                "name":"ujdn",
                "description":"dhdu",
                "image_url":"djdkd"
            },
            {
                "name":"ujdrn",
                "description":"drhdu",
                "image_url":"kidjd"   
            }
        ]
    }, 
    "documents":
    [
        {
            "name":"adhar card",
            "doc_type":"jpg",
            "file_url_1":"dkdkd",
            "file_url_2":"djdjd"
        },
        {
            "name":"pan card",
            "doc_type":"jpg",
            "file_url_1":"djdj",
            "file_url_2":"dkdjf"
         }
    ]
   }
```

- **output**

```
{
    "id": 32,
    "seller": {
        "id": 1,
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
    "details":
    {
        "name": "cmm office",
        "description": "3 flore office ",
        "quantity": 2,
         "auction_items":[
            {
                "name":"ujdn",
                "description":"dhdu",
                "image_url":"djdkd"
            },
            {
                "name":"ujdrn",
                "description":"drhdu",
                "image_url":"kidjd"   
            }
        ]
    }, 
    "documents":
    [
        {
            "name":"adhar card",
            "doc_type":"jpg",
            "file_url_1":"dkdkd",
            "file_url_2":"djdjd"
        },
        {
            "name":"pan card",
            "doc_type":"jpg",
            "file_url_1":"djdj",
            "file_url_2":"dkdjf"
         }
    ]
   }
```
## Patch request  

- **input**
```
{
        "seller":3,
        "document": {
            "name": "pan card",
            "doc_type": "pan card",
            "file_url_1": "pancard2.jpg",
            "file_url_2": "pancard2.png"
        },
        "details": {
            "name": "office",
            "description": "sri lanka",
            "quantity": 2
        },
        "base_price": "80000.00",
        "registration_time_starts_at": "2020-11-19T18:20:25+0000",
        "registration_time_ends_at": "2020-11-19T18:20:31+0000",
        "emd_amount": "2765.00"
    }

```

- **output**

```
{
    "id": 32,
    "seller": {
        "id": 3,
        "user": {
            "id": 6,
            "date_joined": "2020-10-27T11:32:27+0000",
            "date_invited": "2020-10-27T11:32:27+0000",
            "last_login": null,
            "username": "root1",
            "email": "root1@gmail.com",
            "contact_number": "+919823992384",
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
    "document": {
        "id": 7,
        "created_on": "2020-11-22T13:30:07+0000",
        "modified_on": "2020-11-22T13:30:07+0000",
        "name": "pan card",
        "doc_type": "pan card",
        "file_url_1": "pancard2.jpg",
        "file_url_2": "pancard2.jpg"
    },
    "details": {
        "id": 7,
        "created_on": "2020-11-22T13:30:07+0000",
        "modified_on": "2020-11-22T13:30:07+0000",
        "name": "office",
        "description": "sri lanka",
        "quantity": 2
    },
    "created_on": "2020-11-22T13:30:07+0000",
    "modified_on": "2020-11-22T13:30:07+0000",
    "name": "root",
    "description": "root",
    "starts_at": "2020-11-19T17:10:38+0000",
    "ends_at": "2020-11-19T17:10:43+0000",
    "no_of_rounds": 3,
    "base_price": "80000.00",
    "registration_time_starts_at": "2020-11-19T17:10:52+0000",
    "registration_time_ends_at": "2020-11-19T17:10:54+0000",
    "emd_amount": "2765.00",
    "h1_payment_percent": "23.00",
    "h1_payment_end_date": "2020-11-19T17:11:08+0000"
```
