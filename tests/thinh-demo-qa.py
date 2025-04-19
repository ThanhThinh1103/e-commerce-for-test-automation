import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class SortableTest(unittest.TestCase):

    def setUp(self):
        # Khởi tạo trình duyệt
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/sortable")

    def test_sortable_list(self):
        driver = self.driver
        actions = ActionChains(driver)

        # Chuyển đến tab List
        list_tab = driver.find_element(By.ID, "demo-tab-list")
        list_tab.click()
        time.sleep(1)

        # Kéo item 1 xuống vị trí của item 4
        item_1 = driver.find_element(By.XPATH, "//div[@id='demo-tabpane-list']//div[@class='list-group-item list-group-item-action'][1]")
        item_4 = driver.find_element(By.XPATH, "//div[@id='demo-tabpane-list']//div[@class='list-group-item list-group-item-action'][4]")

        actions.drag_and_drop(item_1, item_4).perform()
        time.sleep(2)

    def test_sortable_grid(self):
        driver = self.driver
        actions = ActionChains(driver)

        # Chuyển đến tab Grid
        grid_tab = driver.find_element(By.ID, "demo-tab-grid")
        grid_tab.click()
        time.sleep(1)

        # Kéo item "One" đến vị trí của item "Nine"
        item_one = driver.find_element(By.XPATH, "//div[@id='demo-tabpane-grid']//div[text()='One']")
        item_nine = driver.find_element(By.XPATH, "//div[@id='demo-tabpane-grid']//div[text()='Nine']")

        actions.drag_and_drop(item_one, item_nine).perform()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
