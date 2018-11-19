$(document).ready(function() {

    if ( $(window).width() <430 ) {
    $("#mobile_header").show();
    $("#slide").hide();
    $(".bar").show();
    
    }
    
    else {
        $("#mobile_header").hide();
        $(".bar").hide();
    $("#slide").show();
    
    }
    

    $("#bar").click(function(){
        $("#slide").show(); 
        $("#barb").show(); 
        $("#bar").hide(); 
         
});
$("#barb").click(function(){
    $("#slide").hide(); 
    $("#barb").hide(); 
    $("#bar").show(); 
     
});
   


    
    });