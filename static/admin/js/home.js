$(document).ready(function() {

  var colors = ["slide1", "slide2", "slide3"];
  var titles = ["<u>Schedule</u> an Appointment Today", "Manage Bookkeeping <u>With Us</u>", "File Your Taxes <u>Online</u>"];
  var styles = ["black" , "white" , "black"];
  var imges   = ["../static/admin/img/AccuracyFbla.png" , "../static/admin/img/AccuracyFbla2.png" , "../static/admin/img/AccuracyFbla.png"];
  var cycle = 0;

  var slider = setInterval( slide , 7500);

  function slide() {
  if (cycle != 0 && cycle < 3) {
        var randomColor = colors[colors.length - (cycle + 1)];
        jQuery('#slides').fadeOut( "slow", function() {
           jQuery(this).removeClass()
           $(".introTitle").html( titles[titles.length - (cycle)] );
           $(".introTitle").css("color" , styles[styles.length - (cycle)]);
           $(".descTitle").css("color" , styles[styles.length - (cycle)]);
           $(".menu").css("color" , styles[styles.length - (cycle)]);
           $(".menu a").css("color" , styles[styles.length - (cycle)]);
           $(".logo").attr("src" , imges[imges.length - (cycle)]);
        });
        jQuery('#slides').addClass( randomColor , "slow");
        jQuery('#slides').fadeIn( "slow");
        }
        cycle++;
        if (cycle > 3) {
         cycle = 0;
         jQuery('#slides').fadeOut( "slow", function() {
           jQuery(this).removeClass();
           $(".introTitle").html( titles[2] );
        $(".introTitle").css("color" , styles[2]);
        $(".descTitle").css("color" , styles[2]);
        $(".menu").css("color" , styles[2]);
        $(".menu a").css("color" , styles[2]);
        $(".logo").attr("src" , imges[2]);
           });
         jQuery('#slides').addClass( colors[2]);
         jQuery('#slides').fadeIn( "slow");
        }
    }

   jQuery('.but-1').click(function () {
      cycle = 0;
      clearInterval(slider);
         jQuery('#slides').fadeOut( "slow", function() {
           jQuery(this).removeClass();
           $(".introTitle").html( titles[2] );
        $(".introTitle").css("color" , styles[2]);
        $(".descTitle").css("color" , styles[2]);
        $(".menu").css("color" , styles[2]);
        $(".menu a").css("color" , styles[2]);
        $(".logo").attr("src" , imges[2]);
        jQuery(this).addClass( colors[2]);
           });
         jQuery('#slides').fadeIn( "slow");
      slider = setInterval( slide , 7500);
  });

  jQuery('.but-2').click(function () {
      cycle = 2;
      clearInterval(slider);
         jQuery('#slides').fadeOut( "slow", function() {
           jQuery(this).removeClass();
           $(".introTitle").html( titles[1] );
        $(".introTitle").css("color" , styles[1]);
        $(".descTitle").css("color" , styles[1]);
        $(".menu").css("color" , styles[1]);
        $(".menu a").css("color" , styles[1]);
        $(".logo").attr("src" , imges[1]);
        jQuery(this).addClass( colors[1]);
           });
         jQuery('#slides').fadeIn( "slow");
      slider = setInterval( slide , 7500);
  });

  jQuery('.but-3').click(function () {
      cycle = 3;
      clearInterval(slider);
         jQuery('#slides').fadeOut( "slow", function() {
           jQuery(this).removeClass();
           $(".introTitle").html( titles[0] );
        $(".introTitle").css("color" , styles[0]);
        $(".descTitle").css("color" , styles[0]);
        $(".menu").css("color" , styles[0]);
        $(".menu a").css("color" , styles[0]);
        $(".logo").attr("src" , imges[0]);
        jQuery(this).addClass( colors[0] );
           });
         jQuery('#slides').fadeIn( "slow");
      slider = setInterval( slide , 7500);
  });


// $(window).scroll(function(){
//		if ($(this).scrollTop()  > 200  ) {
//			$('.c2').fadeIn(3000).css("display" , "inline-block !important");
//		}
//		else {
//		   $('.c2').fadeOut().css("display" , "none");
//		}
//	});





















































});