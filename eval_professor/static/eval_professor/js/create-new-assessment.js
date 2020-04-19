// Data Picker Initialization
$('.datepicker').pickadate();


// For add and delete question 
var i = 1;
$(document).ready(function() {
    $(".add-more").click(function(){
        var html = $(".copy").html();
        $(".after-add-more").after(html);
        // set dynamic id and name 
        var input_tag = document.getElementById("question-1");
        window.i++;
        console.log(window.i);
        var name_to_set = 'question-' + i;
        input_tag.name = name_to_set;
        input_tag.id = name_to_set;
    });
    $("body").on("click",".remove",function(){ 
        // $(this).parents(".control-group").remove();
        $(this).parents(".remove-this").remove();
    });
});