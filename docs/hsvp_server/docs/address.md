# Sample request and response for Address API.

## Post request  

- **input**

```
  {
        "user":2,
        "type": "home",
        "line_1": "katka jhunsi allahabad",
        "line_2": "katka jhunsi allahabad",
        "pincode": "211020",
        "state": "uttar pradesh",
        "city": "allahabad",
        "country": "india",
        "contact_number": "+917390049066",
        "notes": "we are looking for relocate."
    }

```

- **output**

```
{
    "id": 7,
    "user": {
        "id": 5,
        "date_joined": "2020-10-22T12:15:27+0000",
        "date_invited": "2020-10-22T12:15:27+0000",
        "last_login": "2020-10-22T12:15:43+0000",
        "username": "Root",
        "email": "root@gmail.com",
        "contact_number": "+919923902382",
        "first_name": "root",
        "last_name": "root",
        "father_first_name": "root",
        "father_last_name": "root",
        "gst_no": "37893937",
        "otp": "3422",
        "otp_sent_at": "09:04"
    },
    "created_on": "2020-10-28T09:03:00+0000",
    "modified_on": "2020-10-28T09:03:00+0000",
    "type": "home",
    "line_1": "katka jhunsi jaipur",
    "line_2": "katka jhunsi jaipur",
    "pincode": "211020",
    "state": "rajasthan",
    "city": "Jaipur",
    "country": "india",
    "contact_number": "+917390049066",
    "notes": "we are looking for relocate."
}

```
## Patch request  

- **input**

```
  {
        "city": "jodhpur"
    }

```
- **output**

```
{
    "id": 7,
    "user": {
        "id": 5,
        "date_joined": "2020-10-22T12:15:27+0000",
        "date_invited": "2020-10-22T12:15:27+0000",
        "last_login": "2020-10-22T12:15:43+0000",
        "username": "Root",
        "email": "root@gmail.com",
        "contact_number": "+919923902382",
        "first_name": "root",
        "last_name": "root",
        "father_first_name": "root",
        "father_last_name": "root",
        "gst_no": "37893937",
        "otp": "3422",
        "otp_sent_at": "09:04"
    },
    "created_on": "2020-10-28T09:03:00+0000",
    "modified_on": "2020-10-28T09:03:00+0000",
    "type": "home",
    "line_1": "katka jhunsi jaipur",
    "line_2": "katka jhunsi jaipur",
    "pincode": "211020",
    "state": "rajasthan",
    "city": "Jaipur",
    "country": "india",
    "contact_number": "+917390049066",
    "notes": "we are looking for relocate."
}

```

