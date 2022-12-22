from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import os
import pandas as pd;
import click
import json

class FatalException(Exception):
    pass

@click.group()
def main():
    pass

@main.command()
@click.argument("team")
def amazon(team):
    """Attempts to play autumn nation international rugbyb games from amazon
    """

    # Login
    # Go under sports <li class="av-retail-m-nav-main-item"><a Sports</a> </div>
    # Find autumn nations div <h2 class="_2NAHyi tst-carousel-header">Autumn Nations Series</h2> up 4 parents then next
    # is carousel (ui) 
    # find game div containing teamname: find <li> with <a> inside where aria-label contains {team}
    print(f"requesting Amazon for team: {team}")

@main.command
@click.argument("team")
def prtv(team):
    # Login
    # Watch Live section
    # Find 
    print(f"requesting prtv for team {team}")

@main.command
def heineken(request):
    """Heineken / Dodge stream
    """
    print("To update when season starts")


if __name__ == "__main__":
    main()