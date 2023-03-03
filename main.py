from playwright.sync_api import Playwright, sync_playwright, expect
import json
import typer 
import pandas as pd
from pathlib import Path
from rich.console import Console



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
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
    page.pause()
    page.get_by_role("link", name="Quick Search").click()
    page.locator("#s2id_autogen2_search").click()
    
   
   #opening the json files to get the ticket numbers and length to use for a loop
    with open('dataorder.json', 'r') as file_order:

        data_order = json.load(file_order)
        
    with open('data.json', 'r') as file:
        
        data = json.load(file)
        
        #length for loop
        length = len(data)
        
        length_test = 1
        
        loop_var = [i for i in range(length_test)]

        # looping through each ticket number
        for index, value in enumerate(loop_var):
            
            page.locator("#s2id_autogen2_search").fill("MWB11901026")
            
            with page.expect_popup() as page1_info:
                
                page.get_by_title("Open").click()
        
            page1 = page1_info.value
            page1.get_by_role("cell", name="Edit Ticket Refresh Close Help Close").get_by_role(
                "button", name="Edit Ticket").click()
            
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
            page1.locator("#currentStatusDescription").fill("Renoir to cancel.")
            
            page1.get_by_role("cell", name="Device delivered, invoice item Device not delivered, cancel order Error corrected, resubmit Continue tracking order Update Ticket Refresh Back Help Close").get_by_role(
                "button", name="Device not delivered, cancel order").click()
            page1.close()
            page1.get_by_role("button", name="Close").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
