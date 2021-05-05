"use strict";
    function item_calc()
    {
        var no_of_item = parseInt(document.getElementById("no_of_item").value);
                for(var i=0;i<no_of_item;i++)
                    {
                        var weight=document.getElementsByClassName("weight")[i].value;

                        var rate_per_gram=document.getElementsByClassName("rate_per_gram")[i].value;

                        var set_metal_amount=weight*rate_per_gram;

                        document.getElementsByClassName("metal_amount")[i].value=set_metal_amount.toFixed(2);

                        var get_metal_amount=document.getElementsByClassName("metal_amount")[i].value;

                        var charge_per_gram=document.getElementsByClassName("charge_per_gram")[i].value;

                        var set_making_charge=(weight*charge_per_gram);

                        document.getElementsByClassName("making_charge")[i].value=set_making_charge.toFixed(2);

                        var get_making_charge=document.getElementsByClassName("making_charge")[i].value;

                        var set_total=(parseFloat(get_metal_amount)+parseFloat(get_making_charge));

                        document.getElementsByClassName("total")[i].value=set_total.toFixed(2);
                    }
    }

function pymnt()
	  {
	  	var sum=0;
	  	$(".total").each(function(){
	  		sum+= +$(this).val();
	  		});
	  	$("#order_amount").val(sum);

			var order_amount=document.getElementById("order_amount").value;
			var discount=document.getElementById("discount").value;
			var taxable_amount=parseFloat(order_amount-discount);
//			if(disc>0){
//			document.getElementById("SubTotal").innerHTML="Amount after applying Discount: " +Calc;
//			}
//			else{
//			document.getElementById("SubTotal").innerHTML="";
//			}
	    	var tax_percent=document.getElementById("tax_percent").value;
	    	document.getElementById("tax_amount").value=(taxable_amount*(tax_percent/100)).toFixed(2);
	       	var cal_net_amount=parseFloat(taxable_amount)+parseFloat(taxable_amount*(tax_percent/100));
	      	document.getElementById("net_amount").value=cal_net_amount.toFixed();

	    	var net_amount=document.getElementById("net_amount").value
			var advance_amount=document.getElementById("advance_amount").value;
			var cal_remaining_amount=parseInt(net_amount-advance_amount);
			document.getElementById("remaining_amount").value=cal_remaining_amount;

	    	var remarks=document.getElementById("remarks");
	    	var remaining_amount=document.getElementById("remaining_amount").value;
	    	if(remaining_amount==0){
	    		remarks.value="CLEARED";
	    	}
	    	else{
	    		remarks.value="UNCLEARED";
	    	}
		}