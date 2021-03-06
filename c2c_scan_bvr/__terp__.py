# -*- encoding: utf-8 -*-
#
#  c2c_scan_bvr
#
#  Created by Nicolas Bessi and Vincent Renaville 
#
#  Copyright (c) 2009 CamptoCamp. All rights reserved.
##############################################################################
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.     
#
##############################################################################
{
        "name" : "Wizard to Scan BVR for Invoice",
        "description" : """
        This module Will work with C-channel or other OCR scanner,
        the module will help you to create an invoice directly from the BVR Code
        , at this time it's work with BVR and BVR+
        """,
        "version" : "1.3",
        "author" : "Camptocamp",
        "category" : "Generic Modules/Others",
        "website": "http://www.camptocamp.com",
        "depends" : [
                        "l10n_ch"
                    ],
        "init_xml" : [],
        "update_xml" : [
                            "scan_bvr_wizard.xml",
                        ],
        "active": False,
        "installable": True
}
