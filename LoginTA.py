from selenium import webdriver
tiempo=3
d=webdriver.chrome(executable_path="C:\Users\PC-IVO\Desktop\uade\stesting\chromedirver.exe")#Chrome
d.get("https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jb2xsZWN0aW9ucy95b2dhLW5ldy5odG1s/")
time.sleep(7)
usr=d.findelement(ByXPATH,"< imput name="login[username]")".send_keys("roni_cost@example.com")
time.sleep(tiempo)
pw=d.findelement(ByXPATH,"< imput name="login[pasword]")".send_keys("roni_cost3@example.com")
time.sleep(tiempo)
botn=d.findelement(ByXPATH,"< button type=submit)(contains(.sing in))""
botn.click()
time.sleep(7)
print("testeo exitoso XD")

d.close()