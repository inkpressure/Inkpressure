
$(window).on('load resize', function(){
    $('#mobile-logo-anim').height($(this).width());
    $('.web-modal').hide();
});

function closeModals() {
    $('.web-modal').hide();
}

function handleConfigClick() {
    $('#web-acct').toggle("visibility");
}

function handleConfigClose() {
    $('#web-acct').hide();
}
