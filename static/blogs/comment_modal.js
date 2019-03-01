$('#commentModal').on('show.bs.modal', function(event) {
    var sender = $(event.relatedTarget)
    var commentId = sender.data('comment_id')
    $('#id_comment_id').val(commentId)
})
