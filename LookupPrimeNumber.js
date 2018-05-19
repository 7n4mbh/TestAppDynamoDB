var AWS = require("aws-sdk");

AWS.config.update({
    region: "ap-northeast-1"
});

var docClient = new AWS.DynamoDB.DocumentClient();

const num = 78;

console.log(`Querying for the ${num}th prime number.`);

const params = {
    TableName: 'PrimeNumbers',
    KeyConditionExpression: '#i = :i',
    ExpressionAttributeNames: {
        '#i': 'index'
    },
    ExpressionAttributeValues: {
        ':i': Number(num)
    }
};

docClient.query(params, function(err, data) {
    if (err) {
        console.error("Unable to query. Error:", JSON.stringify(err, null, 2));
    } else {
        console.log("Query succeeded.");
        var primenumber = data.Items[0].value;
        message = num + '番目の素数は' + primenumber + 'です。'; // 応答メッセージ文字列の作成
        console.log(message);
    }
});