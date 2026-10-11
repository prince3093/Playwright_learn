from playwright.sync_api import Page, expect, Playwright
ordersPayload = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}

class ApiUtils:

    def get_Token(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url = "https://rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/auth/login",
                                            data= {"userEmail": "rahulshetty@gmail.com", "userPassword": "Iamking@000"})
        assert response.ok
        responseBody = response.json()
        return responseBody["token"]
        
        
        
    def create_order(self, playwright: Playwright):
        token = self.get_Token(playwright)
        api_request_context = playwright.request.new_context(base_url = "https://rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/order/create-order",
                                            data = ordersPayload, 
                                            headers={"Authorization": token,
                                            "content-type": "application/json"})
        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId