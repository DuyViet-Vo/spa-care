import requests


def online_payment(tien_coc, khach_hang):
    client_id = "Aer3kcrxPtgyWZ-cceHrx0_Feq1H2JtdFZaPBD_15XRgAySCRFSQrnZj_DxeydG72W8Tr_vOdFoo8e1N"
    client_secret = "EIBKuNbrUEnQJIWN_wfHihXRmEPOwyfJa6HYPPzzaN9RA2mMoIGR8-WyiVcwkIR9KemAWlrHJFKl__vk"

    # URL endpoint của PayPal để lấy token
    token_url = "https://api.sandbox.paypal.com/v1/oauth2/token"

    # Dữ liệu cần gửi để lấy token
    token_data = {"grant_type": "client_credentials"}

    # Xác thực và lấy token
    token_response = requests.post(
        token_url, data=token_data, auth=(client_id, client_secret)
    )

    if token_response.status_code == 200:
        # Lấy token từ phản hồi
        access_token = token_response.json()["access_token"]

        # Dữ liệu cần gửi lên PayPal
        payment_data = {
            "intent": "sale",
            "payer": {"payment_method": "paypal"},
            "transactions": [
                {
                    "amount": {"total": tien_coc, "currency": "USD"},
                    "description": "Tien coc cua khach ",
                }
            ],
            "redirect_urls": {
                "return_url": "https://example.com/return",
                "cancel_url": "https://example.com/cancel",
            },
        }

        # URL endpoint để tạo thanh toán
        payment_url = "https://api.sandbox.paypal.com/v1/payments/payment"

        # Gửi yêu cầu tạo thanh toán với token xác thực
        payment_response = requests.post(
            payment_url,
            json=payment_data,
            headers={"Authorization": f"Bearer {access_token}"},
        )
        return payment_response
    else:
        return token_response.status_code
