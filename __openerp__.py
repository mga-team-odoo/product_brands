# -*- coding: utf-8 -*-
##############################################################################
#
#    product_brands module for OpenERP, Associate product with multiple brands
#    Copyright (C) 2013 MIROUNGA (<http://www.mirounga.fr/>)
#              Christophe CHAUVET <christophe.chauvet@mirounga.fr>
#
#    This file is a part of product_brands
#
#    product_brands is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    product_brands is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
	'name': 'Product Brands',
	'version': '1.0',
	'category': 'Product',
	'description': """ Associate products with compatible brands""",
	'author': 'Julien Thomazeau',
	'depends': [
		'product',
	],
	'images': [],
	'data': [
		'product_brands_view.xml'
	],
	'demo': [],
	'test': [],

}
