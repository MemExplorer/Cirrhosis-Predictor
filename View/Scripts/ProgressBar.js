function UpdateProgressBarAnimate(id, p)
{
    let num = 0;
    UpdateProgressBar(id, 0);
    setInterval(function()
    {
        if (num <= p)
        {
            UpdateProgressBar(id, num++);
        }
    }, 15);
}

function UpdateProgressBar(id, p)
{
    $("#" + id + ".progress").each(function() {

    var value = $(this).attr('data-value') ?? p;
    var left = $(this).find('.progress-left .progress-bar');
    var right = $(this).find('.progress-right .progress-bar');
    var progValue = $(this).find('.progress-value .h2');
    var childTxt = progValue[0].childNodes[0];
    childTxt.data = p;
    if (value >= 0) {
        if (value <= 50) {
            right.css('transform', 'rotate(' + percentageToDegrees(value) + 'deg)')
            left.css('opacity', 0)
        } else {
            right.css('transform', 'rotate(180deg)')
            left.css('transform', 'rotate(' + percentageToDegrees(value - 50) + 'deg)')
            left.css('opacity', 100)
        }
    }

    });
}
function percentageToDegrees(percentage) {

return percentage / 100 * 360

}