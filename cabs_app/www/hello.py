import frappe
# def get_context (context):
#     context.my_emoji ="👋"

@frappe.whitelist(allow_guest=True)
def throw_emoji():
    frappe.msgprint("The Document is going to insert ")