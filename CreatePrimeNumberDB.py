# -*- coding: utf-8 -*-

import boto3
import csv

def create(dynamodb):
    table = dynamodb.create_table(
        TableName = 'PrimeNumbers',
        KeySchema=[
            {
                'AttributeName': 'index',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'value',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'index',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'value',
                'AttributeType': 'N'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    return table

def main(count):
    # データベースに接続
    # DynamoDB (Local Version) 使用時
    #dynamodb = boto3.resource('dynamodb', region_name = 'ap_nrotheast-1', endpoint_url = 'http://localhost:8000')
    # DynamoDB (Web) 使用時
    #dynamodb = boto3.resource('dynamodb', region_name = 'ap_northeast-1')
    dynamodb = boto3.resource('dynamodb')

    # テーブル作成
    #table = create(dynamodb)
    #print("Table status:", table.table_status)

    # デーブルにアイテム追加
    table = dynamodb.Table('PrimeNumbers')
    with open('./primes1.txt', newline = '') as f:
        reader = csv.reader(f, delimiter = ' ', skipinitialspace = True)
        for i in range(4):
            header = next(reader)
        i = 0
        for row in reader:
            for str in row:
                if len(str) > 0:
                    i = i + 1
                    val = int(str)
                    print('#%d: %d' % (i, val))
                    table.put_item(Item = {'index': i, 'value': val})
                if i >= count:
                    break
            if i >= count:
                break
                


if __name__ == '__main__':
    main(100)