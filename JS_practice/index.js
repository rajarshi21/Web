//$(document).ready(function () {
//    $("h1").css("color", "red");
//})

/*console.log($("h1").css("color", "blue"));*/

// Keep things separate
// Can also combine classes
/*$("h1").addClass("big-title another-class");*/
//Can also check if the class is present using .hasClass

//$("h1").text("Bye");
//$("button").text("Hey");
//$("button").html("<strong>Hey</strong>");

//Adding attributes
/*console.log($(".img").attr("src"));*/

//// Set attributes
//$("a").attr("href", "https://www.yahoo.com");

////Get class for an attribute
//console.log($("h1").attr("class"));

////small event listener code
//$("h1").click(function() {
//    $("h1").css("color", "purple");
//});


////big event listener code
//num_buttons = document.querySelectorAll("button").length;
//console.log(num_buttons);

//for (var i = 0; i < num_buttons; i++) {
//    document.querySelectorAll("button")[i].addEventListener("click", function () {
//        document.querySelector("h1").style.color = "purple";
//    });
//}


////small event listener code
//$("button").click(function() {
//    $("h1").css("color", "purple");
//});


////small event listener code
//$(document).keypress(function (event) {
//    console.log(event.key);
//    $("h1").text(event.key);
//}
//);

//Another way for event
$(document).on("keypress", function () {
    $("h1").text(event.key);
})

$("button").on("click", function () {
    $("h1").slideUp().slideDown().animate({ opacity: 0.5 });
})








