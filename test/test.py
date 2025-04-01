import json
from http import HTTPStatus

def handler(request):
    # Query parametresinden 'id' değerini al
    input_value = request.args.get('id')
    
    # Eğer id parametresi yoksa hata döndür
    if not input_value:
        return {
            "statusCode": HTTPStatus.BAD_REQUEST,
            "body": '{"error": "Please provide a value using ?id="}'
        }

    # Girilen değerin sonuna "1" ekle
    output_value = input_value + "1"

    # JSON formatında yanıt döndür
    return {
        "statusCode": HTTPStatus.OK,
        "body": json.dumps({"result": output_value}),
        "headers": {"Content-Type": "application/json"}
    }
