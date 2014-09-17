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
	
