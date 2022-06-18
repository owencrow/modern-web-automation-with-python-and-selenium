# %%
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
opts = Options()
#opts.headless = True
#assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://www.bandcamp.com')
#browser.find_element_by_class_name('playbutton').click()
browser.find_element(By.CLASS_NAME, value='playbutton').click()
tracks = browser.find_elements(By.CLASS_NAME, value='discover-item')
assert(len(tracks) == 8)
tracks[3].click()

discover_section = browser.find_element(By.CLASS_NAME, value='discover-results')
left_x = discover_section.location['x']
right_x = left_x + discover_section.size['width']
discover_items = browser.find_element(By.CLASS_NAME, value='discover_item')
tracks = [t for t in discover_items
              if t.location['x'] >= left_x and t.location['x'] < right_x]

assert len(tracks) == 8

next_button = [e for e in browser.find_elements(By.CLASS_NAME, value='item-page')]
next_button[-1].click()
# %%
