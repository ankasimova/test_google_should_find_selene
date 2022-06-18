from selene import have, be
from selene.support.shared import browser

browser.open('https://www.google.com/')
browser.element('[name="q"]').should(be.blank).type('sun').press_enter()
browser.element('#search').should(have.text('The Sun: News, sport, celebrities and gossip'))

