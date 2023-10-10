import boto3

resourece = boto3.resource('dynamodb', region_name='ap-northeast-2',aws_access_key_id = 'AKIAVVRFM7J7TM7CEHHL',
aws_secret_access_key = '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')

client = boto3.client('dynamodb')
# print(client.list_tables())
# table = client.describe_table(
#     TableName = 'lab-movie'
# )
# print(table)
table = resourece.Table('lab-movie')
item = {
    'Code' : '19780080',
    'Name' : 'Star Wars',
    'Genre' : 'SF',
    'Date' : '1978-04-12',
    'Director' : 'George Lucas',
    'Actor' : '마크 해밀, 캐리 피셔'
}
table.put_item(Item=item)