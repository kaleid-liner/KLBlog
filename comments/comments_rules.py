import rules


@rules.predicate
def is_comment_post_author(user, comment):
    return comment.post.author == user


@rules.predicate
def is_comment_author(user, comment):
    return comment.author == user


rules.add_perm('comments.add_comment', rules.is_authenticated)
rules.add_perm('comments.delete_comment', is_comment_post_author | is_comment_author)