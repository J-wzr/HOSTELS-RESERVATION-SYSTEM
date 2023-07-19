// my jquery designs
$(document).ready(function(){
    $(".introcomplete").slideDown(2000);
    $(".intro").mouseenter(function(){
        $(this).css({"opacity":"0.5"}).mouseleave(function(){
            $(this).css({"opacity":"1"});
        });
    });
    $(".munilogo").slideDown(1000).fadeOut(1000);
    $("span.introspan").fadeIn(1000);
    $(".viewhostelowners").click(function(){

    });
    $(".viewhostels").click(function(){
        
    });
    $(".addowners").click(function(){
        $(".addhostelowners").toggle(300);
    });
    $(".addhostels").click(function(){
        $(".addhostelsinfo").toggle(300)
    });
    $(".markread").click(function(){
        $(this).empty().append("seen").css({"outline":"1px solid green","padding":"4px","border":"none"});
    });
    $(".viewreport").click(function(){
        $(".reportsummary").toggle(200);
    });
    $('#logoutModal').modal('show');
});
