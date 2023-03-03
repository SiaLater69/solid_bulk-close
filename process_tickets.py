from playwright.sync_api import Playwright, sync_playwright, expect
import json
import asyncio
import pandas as pd
import typer
from rich.console import Console



def process_ticket(page):
        
          
        with page.expect_popup() as popup_info:
            
            page1 = popup_info.value

        page1 = popup_info.value
            
        page.pause()
            
        page1.get_by_role("cell", name="Edit Ticket Refresh Close Help Close").get_by_role("button", name="Edit Ticket").click()

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
        page1.close()
        page1.get_by_role("button", name="Close").click()
        page1.get_by_role("cell", name="Edit Ticket Refresh Close Help Close").get_by_role(
        "button", name="Edit Ticket").click()

        page1.locator("#currentStatusDescription").click()

        page1.locator("#currentStatusDescription").fill("Renoir closing.")