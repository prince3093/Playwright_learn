import time
from playwright.sync_api import Page, expect, Playwright

def test_UIValiadationDynamicScript(page:Page):
    #iPhone X. Nokia Edge -> verify 2 items are showing in the cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button", name ="Sign In").click()

    iPhone_product = page.locator("app-card").filter(has_text="phone X")
    iPhone_product.get_by_role("button").click()
    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()

    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")

    with page.expect_popup() as newPage_info:
        #page.locator(".blinkingText").click()  # new page
        page.locator('a[href="https://rahulshettyacademy.com/documents-request"]').click()   # new page
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"

