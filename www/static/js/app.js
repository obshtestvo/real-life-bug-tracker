$(function() {
    var $slider = $(".slider");
    console.log($slider, $slider.length)

    var slider = $slider.owlCarousel({
        navigation : true,
        pagination : true,
        slideSpeed : 400,
        itemsCustom : [
            [0, 1],
            [450, 1],
            [800, 2],
            [1100, 3],
            [1400, 3],
            [1600, 3]
        ],
        paginationSpeed : 400,
        afterInit : function(elem){
            var that = this
            that.owlControls.prependTo(elem)
        }
        // "singleItem:true" is a shortcut for:
        // items : 1,
        // itemsDesktop : false,
        // itemsDesktopSmall : false,
        // itemsTablet: false,
        // itemsMobile : false

    });
});