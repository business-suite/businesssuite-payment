

{
    'name': 'Alipay Payment Acquirer',
    'category': 'Accounting/Payment Acquirers',
    'version': '1.0',
    'sequence': 345,
    'summary': 'Payment Acquirer: Alipay Implementation',
    'description': """Alipay Payment Acquirer""",
    'depends': ['payment'],
    'data': [
        'views/payment_alipay_templates.xml',
        'views/payment_views.xml',
        'data/payment_acquirer_data.xml',
    ],
    'application': True,
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',
}
