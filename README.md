# DynamoDB Upload Example

This is a simple example showing how to upload data to Amazon DynamoDB using Python.

## What is DynamoDB?

DynamoDB is Amazon's NoSQL database service. Think of it like a giant spreadsheet where each row (called an "item") can have different columns (called "attributes").

## The Script Explained

```python
import boto3
from datetime import datetime, timezone

# AWS setup
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# The item to upload
item = {
    "pk": {"S": "walmart#Video Games"},
    "category_code": {"S": "2636"},
    "category_id": {"S": "abcae3dd-6831-49af-8b4e-7baf0bfb238e"},
    "category_tree": {"S": "Video Games"},
    "created_at": {"S": datetime.now(timezone.utc).isoformat()},
    "depth": {"N": "0"},
    "is_leaf": {"BOOL": False},
    "name": {"S": "Video Games"},
    "parent_category_code": {"NULL": True},
    "parent_codes": {"L": []},
    "source": {"S": "walmart"},
    "updated_at": {"S": datetime.now(timezone.utc).isoformat()},
    "url": {"S": "/cp/video-games/2636"}
}

# Upload to DynamoDB
dynamodb.put_item(TableName='walmart-categories-sean-test', Item=item)
print("Item uploaded successfully!")
```

## Key Concepts

### 1. **boto3** - AWS Python SDK
```python
import boto3
dynamodb = boto3.client('dynamodb', region_name='us-east-1')
```
- `boto3` is Amazon's Python library for AWS services
- `region_name='us-east-1'` tells AWS which data center to use

### 2. **DynamoDB Data Types**
DynamoDB requires you to specify data types:
- `{"S": "text"}` = String
- `{"N": "123"}` = Number (must be string)
- `{"BOOL": true}` = Boolean
- `{"NULL": true}` = Null value
- `{"L": []}` = List

### 3. **Primary Key**
```python
"pk": {"S": "walmart#Video Games"}
```
- Every DynamoDB table needs a primary key to uniquely identify each item
- In our table, `pk` is the partition key

### 4. **The Upload Command**
```python
dynamodb.put_item(TableName='walmart-categories-sean-test', Item=item)
```
- `put_item()` adds or replaces an item in the table
- `TableName` specifies which table to use
- `Item` is the data to upload

## Prerequisites

1. **AWS Credentials**: You need AWS access keys set up in `~/.aws/credentials`
2. **DynamoDB Table**: The table `walmart-categories-sean-test` must exist
3. **Python Packages**: Install boto3 with `pip install boto3`

## Running the Script

```bash
python upload_single_item.py
```

## What Happens

1. Script connects to AWS DynamoDB in the us-east-1 region
2. Creates a data item with Walmart category information
3. Uploads it to the `walmart-categories-sean-test` table
4. Prints success message

## Viewing the Data

You can see your uploaded data in the AWS Console:
1. Go to DynamoDB service
2. Click on Tables
3. Click on `walmart-categories-sean-test`
4. Click "Explore table items"

The item will appear with `pk = "walmart#Video Games"`.

## Common Issues

- **Credentials Error**: Make sure your AWS credentials are properly configured
- **Table Not Found**: Ensure the table exists in the specified region
- **Permission Error**: Your AWS user needs `dynamodb:PutItem` permission 
