# -*- coding: utf-8 -*-

import os
from main.settings import PROJECT_ROOT, MEDIA_ROOT
from django.contrib.sites.models import Site

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


def take_advertising_space_prints(items):
    domain = Site.objects.get_current().domain

    driver = webdriver.PhantomJS(
        executable_path=os.path.join(
            PROJECT_ROOT,
            'node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs')
    )
    driver.set_window_size(1000, 842)

    count = items.count()
    for i, item in enumerate(items):
        print u'printin item<' + str(item.id) + u'> [' + str(100.*i/count) + u'%]'
        url = 'http://%s%s' % (domain, item.get_print_preview_url())
        driver.get(url)

        timeout = 7

        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.ID, 'its_a_print_page'))
            )
            driver.save_screenshot(item.get_print_image_path())
            item.save(from_printer=True)

        except NoSuchElementException:
            print "Element not found"
        except TimeoutException:
            print "Timed out waiting for page to load"
        except Exception, e:
            print e

    driver.close()
