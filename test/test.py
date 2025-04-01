import json

def handler(request):
    try:
        # Query parametrelerini al
        input_value = request.args.get('id') if hasattr(request, 'args') else None
        if not input_value:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Please provide a value using ?id="}),
                "headers": {"Content-Type": "application/json"}
            }

        # Girilen değerin sonuna "1" ekle
        output_value = input_value + "1"

        # Yanıt döndür
        return {
            "statusCode": 200,
            "body": json.dumps({"result": output_value}),
            "headers": {"Content-Type": "application/json"}
        }
    except Exception as e:
        # Hata durumunda log döndür
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {"Content-Type": "application/json"}
        }
