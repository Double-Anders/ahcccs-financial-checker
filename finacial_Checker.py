from selenium import webdriver
browser = webdriver.Chrome()
type(browser)
ahcccsId = ""

def healthChoice(ahcccsId): # will open up the health choice website, login and check eligibility for all memebers of the next day(Could be changed to the next 2 weeks
    browser.get('https://www.healthchoicearizona.com/ProviderPortal/login/')#opens health choice website
    taxId = browser.find_element_by_name("id14")# finds text box for tax id entry
    type(taxId)#test to make sure element found
    taxId.send_keys('272206934')#eneters Dr's tax id number
    userId = browser.find_element_by_name("id3")#finds text box for User Id
    type(userId)#test to make sure element found
    userId.send_keys('kindred04')#types in user name
    password = browser.find_element_by_name("id4")
    type(password)
    password.send_keys('ksd@0115v')
    password.submit()
    memberId = browser.find_element_by_name("SearchViewModel.MemberId")
    memberId.send_keys(ahcccsId)
    memberId.submit()
    
healthChoice("A48120187")
