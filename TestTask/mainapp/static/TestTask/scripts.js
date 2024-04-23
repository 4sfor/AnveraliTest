function handleProfileChange() {
    window.location.reload(true)
}

function handleSaveButtonClick() {
    $("#change_form").css('display', 'none');
    $("#changeInfo").css('display', 'flex');
    handleProfileChange();
}

window.addEventListener('DOMContentLoaded', (event) => {
    if (window.jQuery) {
        $(document).ready(function(){
            $("#changeInfo").click(function(){
                $("#change_form").css('display', 'flex');
                $("#changeInfo").css('display', 'none');
            });
            $("#out").click(function(){
                $("#change_form").css('display', 'none');
                $("#changeInfo").css('display', 'flex');
            });
            $("#save").click(handleSaveButtonClick);
        });
    } else {
        console.error('jQuery is not loaded');
    }
});

