import time
from playwright.sync_api import Page, expect, Playwright

def test_UIChecks(page:Page):
    #Hide/display and placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractise")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name='Hide').click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # #AlertBoxes
    page.on("dialog", lambda dialog : dialog.accept())
    page.get_by_role("button", name="Confirm")

    #MouseHover
    page.locator("#mousehover").click()
    page.get_by_role("link" , name="Top").click()

    #FrameHandling
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link", name="All Access plan").click()
    expect(page_frame.locator("body")).to_contain_text("Happy Subscibers")

    #Check the price of rice is equal to 37
    #Identify the price column
    #Identify the rice row
    #extract the price of the rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range (page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text='Price').count()>0:
            priceColValue = index
            print(f"price col value is {priceColValue}")
            break

    riceRow = page.locator("tr").filter(has_text='Rice')
    expect(riceRow.locator("td").nth(priceColValue)).to_have_text("37")
    time.sleep(2)