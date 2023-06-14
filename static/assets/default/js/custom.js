
$(document).ready(function(){
	  var owl = $(".owl-carousel");
	  owl.owlCarousel({
	    items: 1,
	    margin: 10,
	    loop: true,
	    nav: false
	  });


	$('.scroll-to').each(function(i, obj) {
		var scroll_id = $(this).attr('href');
		var off_top = $(scroll_id).offset().top
		$(scroll_id).attr('off_top',off_top);
	});

})
 $(document).on('click', '.scroll-to',function (e) {
 	e.preventDefault()
 	var scroll_id = $(this).attr('href');
 	var height_offset = 0;
 	if($('.top-nav').length){
 		var topnav_height = $('.top-nav').outerHeight()
 		height_offset = height_offset + topnav_height
 	}
 	if($('.navbar').length){
 		var navbar = $('.navbar').outerHeight()
 		height_offset = height_offset + navbar
 	}
 	if(scroll_id){
 		var off_top = $(scroll_id).attr('off_top')
 		if(! off_top){
 			off_top = $(scroll_id).offset().top  
 		}
	 	$('html,body').animate({
            scrollTop: off_top - height_offset
        }, 500);
        return false;
 	}
 })