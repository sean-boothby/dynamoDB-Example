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