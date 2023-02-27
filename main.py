from playwright.sync_api import Playwright, sync_playwright, expect
import json

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://solidportaldev.mwebaws.co.za/mwebcore/admin/login/login.jsp")
    page.locator("input[name=\"username\"]").press("CapsLock")
    page.locator("input[name=\"username\"]").fill("AM")
    page.locator("input[name=\"username\"]").press("CapsLock")
    page.locator("input[name=\"username\"]").fill("AMgaba")
    page.locator("input[name=\"password\"]").click()
    
    page.locator("input[name=\"password\"]").fill("AM22Feb@MWEB!")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Quick Search").click()
    page.locator("#s2id_autogen2_search").click()
    
    #looping through easch ticket number
    with open('dataorder.json', 'r') as file_order:

        data_order = json.load(file_order)

        # length_order = len(data)
        # print(length)
        
    with open('data.json', 'r') as file:
        
        data = json.load(file)

        length = len(data)
        # print(length)

        loop_var = [i for i in range(length)]

        for index, value in enumerate(loop_var):

            # Print the item
            # print(data[index][0])
            
            page.locator("#s2id_autogen2_search").fill(data[index][0])
            
            order_no = data_order[index][0]
            ticket_no = data[index][0]
            
            # print(order_no)
            # print(ticket_no)
            
            info_value = ticket_no + 'Open Delivery required for Order No: ' + order_no
            
            with page.expect_popup() as page1_info:
                
                page.get_by_title("Open").click()
        
                page1 = page1_info.value
                page1.get_by_role("cell", name="Edit Ticket Refresh Close Help Close").get_by_role(
                    "button", name="Edit Ticket").click()
                page1.get_by_role("cell", name="Allocate To Me Allocate Admin Update Ticket Refresh Back Help Close").get_by_role(
                    "button", name="Allocate To Me").click()
                page1.locator("#currentStatusDescription").click()
                page1.locator("#currentStatusDescription").fill("Renoir closing.")
                page1.get_by_role("cell", name="Stock Delivered Delivery Error Update Ticket Refresh Back Help Close").get_by_role(
                    "button", name="Delivery Error").click()
                page1.get_by_role("cell", name="Allocate To Me Allocate Admin Update Ticket Refresh Back Help Close").get_by_role(
                    "button", name="Allocate To Me").click()
                page1.locator("#currentStatusDescription").click()
                page1.locator("#currentStatusDescription").press("CapsLock")
                page1.locator("#currentStatusDescription").fill("R")
                page1.locator("#currentStatusDescription").press("CapsLock")
                page1.locator("#currentStatusDescription").fill("Renoir to cancel.")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)