# Sample request and response for Item API.

## Post request  

- **input**

```

 {
        "auction_detail": 1,
        "created_on": "2020-10-24T08:41:56+0000",
        "modified_on": "2020-10-27T12:04:19+0000",
        "name": "plot rohini sector ",
        "description": "on sell",
        "image_url": "plot.jpeg"
    }

```

- **output**

```
{
    "id": 15,
    "auction_detail": {
        "id": 1,
        "created_on": "2020-10-23T03:58:44+0000",
        "modified_on": "2020-10-23T04:00:40+0000",
        "name": "plot",
        "description": "description.",
        "quantity": 1
    },
    "created_on": "2020-11-02T10:46:47+0000",
    "modified_on": "2020-11-02T10:46:47+0000",
    "name": "plot rohini sector",
    "description": "on sell",
    "image_url": "plot.jpeg"
}
```
## Patch request  

- **input**
```

 {
        "description": "it's not affordable to you."
    }
```

- **output**

```

{
    "id": 15,
    "auction_detail": {
        "id": 1,
        "created_on": "2020-10-23T03:58:44+0000",
        "modified_on": "2020-10-23T04:00:40+0000",
        "name": "plot",
        "description": "this item is too cheap",
        "quantity": 1
    },
    "created_on": "2020-11-02T10:46:47+0000",
    "modified_on": "2020-11-02T10:50:53+0000",
    "name": "plot rohini sector",
    "description": "it's not affordable to you.",
    "image_url": "plot.jpeg"
}
```
