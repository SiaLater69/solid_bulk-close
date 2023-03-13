from playwright.sync_api import Playwright, sync_playwright, expect
import json
import pandas as pd
import typer
from rich.console import Console


def Ticket(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://solidportaldev.mwebaws.co.za/mwebcore/admin/login/login.jsp")

    page.locator("input[name=\"username\"]").fill("AMgaba")
    page.locator("input[name=\"password\"]").click()

    page.locator("input[name=\"password\"]").fill("AM22Feb@MWEB!")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("link", name="Quick Search").click()

    page.locator("#s2id_autogen2_search").click()

    Bulk_Dt = pd.read_excel('Bulk closure 13-02-2023.xlsx', dtype='string')

    Bulk_Data = Bulk_Dt.loc[Bulk_Dt['Status'] == 'Open', 'Ticket No']

    length_of_data = len(Bulk_Data)

    len_test = 1

    print(length_of_data)

    # print(Bulk_Data[1])

    loop_var = [i for i in range(length_of_data)]

    # looping through each ticket number

    for index, value in enumerate(loop_var):

        page.locator("#s2id_autogen2_search").fill(Bulk_Data[index])

        print(Bulk_Data[index])

        page.pause()

        # with page.expect_popup() as popup_info:

        value = page.locator(".select-label").inner_text()

        print(value)

        if value == 'Open':

            page.locator(".select-label").click()

            with page.expect_popup() as popup_info:

                page1 = popup_info.value

            page1 = popup_info.value

            page1.pause()

            page1.get_by_role("cell", name="Edit Ticket Refresh Close Help Close").get_by_role("button",
                                                                                               name="Edit Ticket").click()

            page1.locator("#currentStatusDescription").click()

            page1.locator("#currentStatusDescription").fill("Renoir closing.")

            page1.get_by_role("cell", name="Allocate To Me Allocate Admin Update Ticket Refresh Back Help Close").get_by_role(
                "button", name="Allocate To Me").click()

            page1.locator("#currentStatusDescription").click()
            page1.locator("#currentStatusDescription").fill(
                "Renoir to cancel.")

            page1.get_by_role("cell", name="Stock Delivered Delivery Error Update Ticket Refresh Back Help Close").get_by_role(
                "button", name="Delivery Error").click()

            page1.get_by_role("cell", name="Allocate To Me Allocate Admin Update Ticket Refresh Back Help Close").get_by_role(
                "button", name="Allocate To Me").click()

            page1.locator("#currentStatusDescription").click()
            page1.locator("#currentStatusDescription").fill(
                "Renoir to cancel.")

            page1.get_by_role("cell", name="Device delivered, invoice item Device not delivered, cancel order Error corrected, resubmit Continue tracking order Update Ticket Refresh Back Help Close").get_by_role(
                "button", name="Device not delivered, cancel order").click()
            page1.get_by_role("button", name="Close").click()
            page1.close()
            page.get_by_role("link", name="Quick Search").click()
            page.locator("#s2id_autogen2_search").fill(Bulk_Data[index])
            page.locator(".select-label").click()


        elif value != 'Open':

            print('restarting')

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    Ticket(playwright)