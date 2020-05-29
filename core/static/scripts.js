let opened = false;

$('document').ready(function(){

    $('.burger-menu-mobile').on('click',(function(){
        $('.login-section-text a').css({'color' : '#5068a9'});
        $('.login-section').show();
        $('.nav-menu').css("display", "block");
        $('.login-section').show("slide");
        $('.burger-menu-mobile').hide();
        $('.burger-menu-mobile-quit').show();
        $('li .fas').replaceWith('<a href="" class="notification-replacement">Ð˜Ð·Ð²ÐµÑÑ‚Ð¸Ñ</a>');
        opened = true;
    }));
    $('.burger-menu-mobile-quit').on('click',(function(){
        $('.login-section').hide("slide");
        $(this).hide();
        $('.nav-menu').css("display", "none");
        // $('.burger-menu-mobile i').css("color", "#2c2c2c");
        $('.login-section-text a').css({'color' : '#2c2c2c'});
        $('.burger-menu-mobile').show();
        opened = false;

    }));

        $('main').on('click', (function () {
            if(opened === true) {
                $('.login-section').hide("slide");
                $('.burger-menu-mobile-quit').hide();
                $('.nav-menu').css("display", "none");
                // $('.burger-menu-mobile i').css("color", "#2c2c2c");
                $('.login-section-text a').css({'color': '#2c2c2c'});
                $('.burger-menu-mobile').show();
                opened = false;

            }
            if(notif_opened){
                notif_opened = false;
                $('#notifPanel').hide();
            }
            if(profile_opened){
                profile_opened = false;
                $('.login-menu').hide();
            }
        }));


});
