$(document).ready(function() {

    var userprofilePk = JSON.parse(document.getElementById('pk').textContent);
    $(".likeButton").click(function() {
        var commentIdVar = $(this).val();
        $.ajax({
            url: '/posts/detail/' + userprofilePk,
            type: 'post',
            data: {
                commentID: commentIdVar,
                csrfmiddlewaretoken: csrftoken,
                action: 'post'
            },
            success: function(json) {
                document.getElementById("likeCount" + commentIdVar).innerHTML = json['result']
            },
        })
    })
})