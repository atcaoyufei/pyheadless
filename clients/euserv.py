import asyncio
import re
import time

from libs.base import BaseClient


class Euserv(BaseClient):

    def __init__(self):
        super().__init__()
        self.url = 'https://support.euserv.com'

    async def handler(self, username, password, **kwargs):
        self.logger.info(f'{username} start login.')
        await self.page.type('input[name="email"]', username, {'delay': 30})
        await asyncio.sleep(0.5)
        await self.page.type('input[name="password"]', password, {'delay': 30})
        await asyncio.sleep(0.5)
        await self.page.click('input[name="Submit"]')
        await asyncio.sleep(10)

        await self.page.click('#kc2_order_customer_orders_tab_1')
        await asyncio.sleep(1)

        s = await self.page.Jeval('.kc2_order_extend_contract_term_container', 'el => el.textContent')
        self.logger.info(s)
        try:
            await self.page.click('.kc2_order_extend_contract_term_container')
            await asyncio.sleep(5)
            await self.page.click('.kc2_customer_contract_details_change_plan_item_action_button')
            await asyncio.sleep(5)
            await self.page.type('input[name="password"]', password, {'delay': 30})
            await asyncio.sleep(1)
            await self.page.click('#kc2_security_password_dialog_action_confirm')
            await asyncio.sleep(5)
            await self.page.click('input[value="Confirm"]')
            await asyncio.sleep(5)
        except Exception as e:
            self.logger.error(e)



