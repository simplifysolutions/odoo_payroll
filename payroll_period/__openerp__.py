# -*- coding:utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 Savoir-faire Linux. All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Payroll Period',
    'version': '1.0.0',
    'license': 'AGPL-3',
    'category': 'Human Resources',
    'summary': "Add payroll periods",
    'author': "Savoir-faire Linux",
    'website': 'https://www.savoirfairelinux.com',
    'depends': [
        'payroll_base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/hr_period.xml',
        'views/hr_fiscalyear.xml',
        'views/hr_payslip.xml',
        'views/hr_payslip_line.xml',
        'views/hr_payslip_run.xml',
        'wizard/hr_payslip_employee.xml',
    ],
    'installable': True,
}
