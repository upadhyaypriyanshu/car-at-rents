// Copyright (c) 2024, Priyanshu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {
        

	},
    rate(frm){
        frm.trigger("update_total_amount");

    },
    update_total_amount(frm){
        total_distance = 0;
        for(let item of  frm.doc.items){
            total_distance += item.distance
        }
      frm.set_value("total_amount",frm.doc.rate * total_distance);

    },

});

frappe.ui.form.on("Ride Booking Item",{
  refresh(frm){
},
  distance(frm,cdt,cdn){
   frm.trigger("update_total_amount");
 },
  items_add(frm){
    frm.trigger("update_total_amount");
},
  items_remove(frm){
    frm.trigger("update_total_amount");
  },
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
});
