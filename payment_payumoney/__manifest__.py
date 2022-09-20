

{
    'name': 'PayuMoney Payment Acquirer',
    'version': '1.0',
    'category': 'Accounting/Payment Acquirers',
    'sequence': 375,
    'summary': 'Payment Acquirer: PayuMoney Implementation',
    'description': """
PayuMoney Payment Acquirer for India.

PayUmoney payment gateway supports only INR currency.
""",
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_payumoney_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'application': True,
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',
}
