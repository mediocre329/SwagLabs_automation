from Code.functionality import Swaglab
import time

with Swaglab() as swag:
    swag.land_first_page()
    swag.login()
    swag.filter()
    swag.get_item ()
    time.sleep(20)