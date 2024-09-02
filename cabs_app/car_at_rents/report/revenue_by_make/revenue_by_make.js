// Copyright (c) 2024, Priyanshu and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue By Make"] = {
	"filters": [{
		"fieldname":"my_filter",
		"label":"filter",
		"fieldtype":"Link",

		"options":"Vehicle"
	}

	]
};
