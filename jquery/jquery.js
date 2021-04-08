$(".play").mouseover(function(){

    $(this).css({"cursor":"pointer"});

    $(this).click(function(){

        $(this).css({"visibility":"hidden"});

        $("iframe").attr("src","https://www.youtube.com/embed/M2ILKmWgW8I?rel=0&amp;autoplay=1");

    });

});


