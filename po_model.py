# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Page(object):
	'''基础类，用于页面对象类的继承'''
	login_url='http://localhost:8000/index'

	def __init__(self,selenium_driver,base_url=login_url):
		self.base_url=base_url
		self.driver=selenium_driver
		self.timeout=30

	def on_page(self):
		return self.driver.current_url==(self.base_url+self.url)

	def _open(self,url):
		url=self.base_url+url
		self.driver.get(url)
		assert self.on_page(),'Did not land on %s'%url

	def open(self):
		self._open(self.url)

	def find_element(self,*loc):
		return self.driver.find_element(*loc)

class LoginPage(Page):
	'''发布会登录页面模型'''
	url='/'
	#定位器
	username_loc=(By.NAME,"username")
	password_loc=(By.NAME,"password")
	submit_loc=(By.ID,"btn")

	#Action
	def type_username(self,username):
		self.find_element(*self.username_loc).send_keys(username)

	def type_password(self,password):
		self.find_element(*self.password_loc).send_keys(password)

	def submit(self):
		self.find_element(*self.submit_loc).click()

def test_user_login(driver,username,password):
	'''测试获取的用户名密码是否可以登录'''
	login_page=LoginPage(driver)
	login_page.open()
	login_page.type_username(username)
	login_page.type_password(password)
	login_page.submit()

def main():
	try:
		driver=webdriver.Chrome()
		print '111'
		username='admin'
		password='123456'
		test_user_login(driver,username,password)
		print '22'
		sleep(3)
		text=driver.find_element_by_xpath("/html/body/nav/div/div[1]/a").text
		assert(text=='Guest Manage System')
		print 'aa'
	except Exception as e:
		print e
		
	finally:
		driver.close()

if __name__=='__main__':
	main()













