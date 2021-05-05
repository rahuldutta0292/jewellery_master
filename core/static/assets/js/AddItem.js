"use strict";
$(document).ready(function() {
    var wrapper = $('.field_wrapper'); //Input field wrapper
	$('#AddMoreItem').on('click', function () {
	var item=parseInt(document.getElementById("no_of_item").value);
    var fieldHTML = '<tr> <td> <select class="form-control input-sm" name="item_name" required="required" style="min-width:100px;"> <option selected disabled="disabled">Select Item</option> <option value=""></option> </select> </td> <td style="min-width:100px;"> <textarea rows="3" type="text" class="form-control input-sm" name="item_description" required></textarea> </td> <td> <input type="number" onkeyup="item_calc(); pymnt()" class="form-control input-sm weight" name="weight" required> </td> <td> <input type="number" onkeyup="item_calc(); pymnt()" class="form-control input-sm rate_per_gram" name="rate_per_gram" required> </td> <td> <input type="number" class="form-control input-sm metal_amount" readonly> </td> <td style="max-width:60px;"> <input type="number" onkeyup="item_calc(); pymnt()" class="form-control input-sm charge_per_gram" name="charge_per_gram" required> </td> <td> <input type="text" value="" class="form-control input-sm making_charge" readonly> </td> <td> <input type="text" value="" name="item_total" class="form-control input-sm total" readonly> </td><td> <button type="button" onclick="pymnt()" class="btn btn-sm RemoveItem"><span class="fa fa-minus fa-sm"></span></button> </td></tr>';
        $(wrapper).append(fieldHTML);
         document.getElementById("no_of_item").value=item+1;
         });
         $(wrapper).on('click','.RemoveItem',function(){
            var item=parseInt(document.getElementById("no_of_item").value);
            $(this).parent().parent().remove();
            document.getElementById("no_of_item").value=item-1;

        });
});

