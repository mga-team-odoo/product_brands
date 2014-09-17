# -*- coding: utf-8 -*-
##############################################################################
#
#    product_brands module for OpenERP, Associate product with compatible brands
#    Copyright (C) 2014 ozytwyst Julien Thomazeau <ozydev@julienthomazeau.fr>
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

from openerp.osv import orm
from openerp.osv import fields

class product_brands(orm.Model):
	_name = 'product.brands'
	_columns = {
		'name': fields.char('Brand Name'),
		'description': fields.text('Description', translate=True),
		'logo': fields.binary('Logo File')
	}

class product_template(orm.Model):
	_inherit = 'product.template'
	_columns = {
		'brand_ids': fields.many2many(
			'product.brands',
			'product_brands_rel',
			'template_id',
			'brand_id',
			'Brands')
	}
	
