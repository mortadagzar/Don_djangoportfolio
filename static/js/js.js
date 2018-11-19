$(document).ready(function() {

    if ( $(window).width() <430 ) {
    
    $("#slide").hide();
    $(".bar").show();
    
    }
    
    else {
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