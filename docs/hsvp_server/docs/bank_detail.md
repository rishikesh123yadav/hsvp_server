# Sample request and response for Bank Detail API.

## Post request  

- **input**

```

 {
        "name": "root",
        "bank_name": "HDFC",
        "account_number": "336749837334",
        "ifs": "hdfc4849",
        "branch": "jhunsi"
    }
```

- **output**

```

{
    "id": 7,
    "created_on": "2020-11-03T07:14:00+0000",
    "modified_on": "2020-11-03T07:14:00+0000",
    "name": "root",
    "bank_name": "HDFC",
    "account_number": "336749837334",
    "ifs": "hdfc4849",
    "branch": "jhunsi"
}

```
## Patch request  

- **input**
```
 {
        "branch": "jaipur"
    }
```

- **output**

```

{
    "id": 7,
    "created_on": "2020-11-03T07:14:00+0000",
    "modified_on": "2020-11-03T07:16:15+0000",
    "name": "root",
    "bank_name": "HDFC",
    "account_number": "336749837334",
    "ifs": "hdfc4849",
    "branch": "jaipur"
}
```
