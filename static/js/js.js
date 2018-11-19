$(document).ready(function() {

    if ( $(window).width() <430 ) {
    $("#mobile_header").show();
    $("#slide").hide();
    $(".bar").show();
    
    $("#menue").hide();
    }
    
    else {
        $("#mobile_header").hide();
        $(".bar").hide();
    $("#slide").show();
    $("#menue").hide();
    
    }
    

    $("#bar").click(function(){
        $("#menue").show();
        $("#barb").show(); 
        $("#bar").hide(); 
         
});
$("#barb").click(function(){
    $("#barb").hide(); 
    $("#bar").show(); 
    $("#menue").hide();
     
});
   


    
    });