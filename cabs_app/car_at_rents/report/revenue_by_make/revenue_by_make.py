# Copyright (c) 2024, Priyanshu and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        {
            "fieldname": "make",
            "fieldtype": "Data",
            "label": "Make"
        },
        {
            "fieldname": "total_revenue",
            "fieldtype": "Currency",
            "label": "Total Revenue",
            "options": "AED"
        }
    ]
    
    # Fetch data using an SQL query with a LEFT JOIN between Ride Booking and Vehicle
    data = frappe.db.sql("""
        SELECT v.make AS make, SUM(rb.total_amount) AS total_revenue FROM
            `tabRide Booking` AS rb
        LEFT JOIN
            `tabVehicle` AS v ON rb.vehicle = v.name
        GROUP BY
            v.make
    """, as_dict=True)

    # chart = {
    #         data:{
    #        "label" : [x.make for x in data],
    #        "datasets":[{ "values":[x.total_revenue for x in data]}],
            
    #         "type":"pie"
    #         },
    # }
    chart = {
    "data": {
        "labels": [x.make for x in data],  # Corrected from "label" to "labels"
        "datasets": [
            {
                "values": [x.total_revenue for x in data]
            }
        ]
    },
    "type": "donut"  # Specify the type of chart here
}

        
        
    return columns, data, "Here is The Report" ,chart


