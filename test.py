from playwright.sync_api import Playwright, sync_playwright, expect
from pathlib import Path
import json
import pandas as pd
import yaml
import typer
from rich.console import Console

console = Console()
app = typer.Typer()


def read_config(configfile: Path):
    with open(configfile, 'r') as f:
        config = yaml.safe_load(f)

    return config


def read_data(datafile: Path):
    data = pd.read_excel(datafile)

    return data

@app.command()
def runapp(configfile: Path, datafile:Path, column: str):
    config = read_config(configfile)
    data =  read_data(datafile)

    run(config, data, column)

def run(config, data, column)-> None:
    username = config['solid']['username']
    password = config['solid']['password']
    base_url = config['solid']['base_url']
    headless = config['playwright']['headless']
    slowmo = config['playwright']['slow_mo']

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=headless, slow_mo=slowmo)
        context = browser.new_context()
        page = context.new_page()

        page.goto(base_url)

        page.locator("input[name=\"username\"]").fill(username)
        page.locator("input[name=\"password\"]").click()

        page.locator("input[name=\"password\"]").fill(password)
        page.get_by_role("button", name="Login").click()

        page.get_by_role("link", name="Quick Search").click()

        page.locator("#s2id_autogen2_search").click()

        Bulk_Data = data.loc[data['Status'] == 'Open', column]

        length_of_data = len(Bulk_Data)


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
                page1.close()
                page1.get_by_role("button", name="Close").click()
                page1.get_by_role("cell", name="Edit Ticket Refresh Close Help Close").get_by_role(
                "button", name="Edit Ticket").click()

                page1.locator("#currentStatusDescription").click()

                page1.locator("#currentStatusDescription").fill("Renoir closing.")

            elif value != 'Open':

                print('restarting')

    # ---------------------
    context.close()
    browser.close()

if __name__ == "__main__":
    app()

