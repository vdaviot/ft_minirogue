# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Currency.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdaviot <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2016/12/01 00:46:12 by vdaviot           #+#    #+#              #
#    Updated: 2016/12/01 00:46:13 by vdaviot          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

CURRENCY_TYPE = ["Coin", "Pile"]
MONEY_TYPE = ["Platinium", "Gold", "Silver", "Copper"]
GEM_TYPE = ["Ruby", "Jade", "Emerald", "Diamond", "Saphire", "Citrine", "Topaz", "Amber"]
CONTAINER_TYPE = ["Jar", "Chest", "Purse", "Shelf", "Canteen"]


CURRENCY_UNIT = ["Platinium", "Gold", "Silver", "Copper", "Ruby", "Jade", "Emerald", "Diamond", "Saphire", "Citrine", "Topaz", "Amber"]
CURRENCY_PRICE = [10, 5, 3, 1, 5, 4, 3, 10, 7, 3, 3, 4]

class	CurrencyTable(Items):

	def	__init__(self):
		self._initCurrencyPriceTable()

	def	_initCurrencyPriceTable():
		self.currencyPriceTable = []
		for unit in range(CURRENCY_UNIT):
			self.currencyPriceTable.append(Items.__init__(self, CURRENCY_UNIT[i], CURRENCY_PRICE[i]))

